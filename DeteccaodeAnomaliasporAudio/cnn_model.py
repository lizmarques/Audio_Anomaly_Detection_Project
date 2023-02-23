# Importando as bibliotecas
import numpy as np
import pandas as pd
import librosa
from tqdm import tqdm                           # para gerar a barra de progresso durante a execução das tarefas
from tensorflow.python import keras
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.layers import Activation, Conv1D, Dense, Dropout, Flatten, MaxPooling1D
from sklearn.model_selection import train_test_split
from pathlib import Path
from collections import namedtuple
import seaborn as sns
sns.set()
import warnings
warnings.filterwarnings("ignore")

# Percorrendo os diretórios, puxando o nome dos arquivos e seu caminho

# "namedtuple" = é como se fosse um container de dicionários que carrega chaves e valores
File = namedtuple("File", "full_path, path_parts")

# Criação de uma lista vazia irá receber os dados
files = []

# "p" = variável que indica o caminho do dataset
p = Path(r"C:\Users\liznm\PycharmProjects\DeteccaodeAnomaliasporAudio\MIMII_dataset")

# Iteração através dos caminhos de pastas/sub pastas para encontrar os arquivos .wav
# e adicioná-los em uma lista
for item in p.glob("**/*"):
  # Verifica o que está após o ponto "."
  if item.suffix in ([".wav"]):
    # Retorna o caminho do arquivo
    full_path = Path.resolve(item)

    # Retorna o caminho do arquivo divido em partes
    path_parts = item.parts

    # Adcionando os caminhos na lista
    files.append(File(full_path, path_parts))

# Criando e visualizando o dataframe
df = pd.DataFrame(files)

# Ajustando os dados do dataframe

# Separando as colunas com os dados respectivos
df_adjust_1 = df.join(pd.DataFrame(df["path_parts"].to_list()))
df_adjust_1.set_axis(["full_path", "path_parts", "OUT1", "OUT2", "OUT3", "OUT4", "OUT5", "OUT6","dB", "machine_type","typeID", "class", "audio_file"], axis='columns', inplace=True)

# Deletando as colunas desnecessárias
df_adjust_2 = df_adjust_1.drop(["OUT1", "OUT2", "OUT3","OUT4","OUT5","OUT6"], axis=1)


# Ordenando as colunas de forma mais coerente
df3 = df_adjust_2.reindex(columns=["machine_type", "typeID", "dB","audio_file", "class","full_path"])

# Pré processamento
# Função que garante a extração das características
def features_extractor(file_paths):
  data, sample_rate = librosa.load(file_paths, sr=None, res_type="kaiser_fast")
  # "mfcc_features" = Extraindo características mfcc. Y = amostras de áudio; sr = taxa de amostragem do arq que será carregado; "n_mfcc" = número de mfccs
  # O ideal é iniciar o treinamento do modelo com n_mfcc = 40. Caso não tenha bons resultados, posso ir aumentando esse número
  mfccs_features = librosa.feature.mfcc(y=data, sr=sample_rate, n_mfcc=40)
  mfcss_features_scaled = np.mean(mfccs_features.T, axis=0)
  return mfcss_features_scaled

extracted_features = []
# Percorrendo de cada um dos arquivos
for path in tqdm(df3["full_path"].values):
  data = features_extractor(path)
  extracted_features.append([data])

# Neste seguimento, faremos os ajustes para deixar os dados aptos para a rede neural
extracted_features_df = pd.DataFrame(extracted_features, columns=["feature"])

# Dividindo entre atributo classe e atributos previsores
# Quando trabalhamos com aprendizagem de máquina, é comum denominarmos o X com os atributos previsores
# Neste caso, as características mfccs.
X = np.array(extracted_features_df["feature"].tolist())

# E no Y as informações relacionadas com a Classe
y = np.array(df3["class"].tolist())


# Utilizamos o One Hot Encoder, pois temos um problema de classificação com mais de 2 classes
# Conversão das variáveis categóricas (string) para numérica na variável Y
labelencoder = LabelEncoder()
y = to_categorical(labelencoder.fit_transform(y))

# Salvando as variáveis X e y
def save_x_y(X,y):
  with open(r"C:\Users\liznm\PycharmProjects"
                         r"\DeteccaodeAnomaliasporAudio\x_y_variables\X_variable.npy", 'wb') as f:
    np.save(f, X)

  with open(r"C:\Users\liznm\PycharmProjects"
                         r"\DeteccaodeAnomaliasporAudio\x_y_variables\y_variable.npy", 'wb') as f2:
    np.save(f2, y)

  return

save_x_y(X,y)

# Separando o dataset em treino, teste e validação

# Definimos 80% dos dados para variável x_train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)
X_test, X_val, y_test, y_val = train_test_split(X_test, y_test, test_size = 0.5, random_state=1)

# Adicionando uma nova dimensão (np.newaxis).
# Os dois pontos (:) indica que vamos manter esses dados, a quantidade de registros
# e a quantidade de colunas e adicionamos uma dimensão no final
X_train = X_train[:,:,np.newaxis]
X_test = X_test[:,:,np.newaxis]
X_val = X_val[:,:,np.newaxis]

#Criando o modelo o model
model = Sequential()
model.add(Conv1D(64, kernel_size=(10), activation="relu", input_shape=(X_train.shape[1], 1)))
model.add(Dropout(0.4))
model.add(MaxPooling1D(pool_size=(4)))
model.add(Conv1D(128, 10, padding="same",))
model.add(Activation("relu"))
model.add(Dropout(0.4))
model.add(MaxPooling1D(pool_size=(4)))
model.add(Flatten())
model.add(Dense(units = 64))
model.add(Dropout(0.4))
model.add(Dense(units = 2))
model.add(Activation("sigmoid"))

# Compilando a rede neural
model.compile(loss= "binary_crossentropy", metrics = ["accuracy"], optimizer = "adam")

# Treinando o modelo
# Total de épocas do treinamento
num_epochs = 40

# Enviar para a rede neural de 32 em 32 áudios
num_batch_size = 32

# Salvando os modelos com os melhores resultados
checkpointer = ModelCheckpoint(filepath="saved_models/audio_anomaly_detection.hdf5",
                               verbose=1, save_best_only=True)

# Definindo o earlystopping para evitar o overfitting
callback = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=3)

# Treinamento do modelo
model.fit(X_train, y_train, batch_size=num_batch_size, epochs = num_epochs,
                    validation_data=(X_val, y_val), callbacks=[checkpointer, callback], verbose=1)

# Salvando o modelo
model.save("saved_models/audio_anomaly_detection.h5")
