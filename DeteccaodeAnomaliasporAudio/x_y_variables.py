# Importando as bibliotecas
from tensorflow.python import keras
import numpy as np
from sklearn.model_selection import train_test_split
import seaborn as sns
sns.set()


# Abrindo o arquivo da variável X
def open_x():
  with open(r"C:\Users\liznm\PycharmProjects\DeteccaodeAnomaliasporAudio\x_y_variables\X_variable.npy", "rb") as f:
    a = np.load(f)
    return a

# Abrindo o arquivo da variável y
def open_y():
  with open(r"C:\Users\liznm\PycharmProjects\DeteccaodeAnomaliasporAudio\x_y_variables\y_variable.npy", "rb") as f2:
    b = np.load(f2)
    return b

# Definimos 80% dos dados para variável x_train
X_train, X_test, y_train, y_test = train_test_split(open_x(), open_y(), test_size=0.2, random_state=1)
