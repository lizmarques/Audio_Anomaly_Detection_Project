# Importações necessárias
import streamlit as st
import os
from pathlib import Path
import json
from PIL import Image
import time
from streamlit_lottie import st_lottie, st_lottie_spinner
import librosa.display as ld
import librosa
import numpy as np
import matplotlib.pyplot as plt
import tensorflow
# from x_y_variables import X_test, y_test


# Função para carregar os arquivos com animações do Lottie
@st.experimental_memo
def load_lottiefile(path: str):
    with open(path, "r", errors="ignore") as f:
        data = json.load(f)
    return data


# Logo na sidebar do Streamlit
st.sidebar.image((Image.open(r"C:\Users\liznm\PycharmProjects"
                             r"\DeteccaodeAnomaliasporAudio\imagens"
                             r"\logo_sidebar.png")).resize((900, 700)), use_column_width=True)


# Menu do sidebar no Streamlit
paginaSelecionada = st.sidebar.selectbox("Menu",["Introdução","Case Real", "Detector de Anomalias"])

# Página de Introdução no Streamlit
if paginaSelecionada == "Introdução":

    # Imagem - Carregando logo interativa - Lottie json
    lottie_file = r"C:\Users\liznm\PycharmProjects\DeteccaodeAnomaliasporAudio" \
                  r"\lottie_animations\main_logo_lf30_editor_nczzeanh.json"
    lottie_json = load_lottiefile(lottie_file)
    st_lottie(lottie_json, height=80)

    # Título - "Detecção de Anomalias por Áudio"
    st.title("Detecção de Anomalias por Áudio")

    # Aplicação do CSS no Streamlit - selecionando o tamanho da fonte
    st.markdown("""
    <style>
    .big-font {
        font-size:17px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Texto - contextualizando o cenário e a importância da ferramenta
    st.markdown("<p class='big-font'> Inserida no contexto de Smart Factory - indústrias "
                "com um alto nível de digitalização que facilitam a coleta de dados e "
                "informações, por meio dos dispositivos tecnológicos - a ferramenta de detecção "
                "de anomalias por áudio tem como principal objetivo reduzir os custos com manutenção, "
                "otimizar a produção, ou seja, reduzir interrupções não planejadas  e aumentar a produtividade "
                "do maquinário no setor industrial.</p>", unsafe_allow_html=True)

    st.markdown("<p class='big-font'> O modelo atual foi desenvolvido com foco em identificar "
                "anomalias de ventiladores industriais. No entanto, é possível aplicá-lo em "
                "diferentes tipos de maquinários como: bombas, válvulas ou até mesmo trilhos "
                "deslizantes. Para isso, basta ter os dados correspondentes.</p>", unsafe_allow_html=True)

    st.markdown("<p class='big-font'>Atualmente a ferramenta se encontra na primeira "
                "versão e estão sendo realizados testes iniciais, a fim de validar seus "
                "respectivos resultados.</p>", unsafe_allow_html=True)

# Página com a Case Real
elif paginaSelecionada == "Case Real":
    # Título - "Case Real"
    st.title("Case Real")
    st.subheader("Empresa Bramburky - República Tcheca")

    # Imagem - logo da empresa Bramburky
    col1, col2, col3 = st.columns([1, 6, 1])

    with col1:
        st.write("")

    with col2:
        st.image((Image.open(r"C:\Users\liznm\PycharmProjects\DeteccaodeAnomaliasporAudio\imagens"
                         r"\bramburky_product_image.png")), width=500)

    with col3:
        st.write("")


    # Texto - explicação do Case Bramburky
    st.markdown("""
    <style>
    .big-font2 {
        font-size:17px !important;
    }
    .big-font3 {
        font-size:22px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("<p class='big-font3'><strong>Contexto</strong>:</p>", unsafe_allow_html=True)
    st.markdown("<p class='big-font2'>- 3ª empresa produtora de batatas chips "
                "na República Tcheca</p>", unsafe_allow_html=True)
    st.markdown("<p class='big-font2'>- Produz batatas chips há 17 anos</p>", unsafe_allow_html=True)
    st.markdown("<p class='big-font2'>- Qualquer tempo de inatividade significa uma perda de milhares "
                "de euros</p>", unsafe_allow_html=True)
    st.markdown("<p class='big-font2'>- Se alguma das máquinas falhar, a empresa perde cerca de "
                "5 caminhões de chips</p>", unsafe_allow_html=True)

    # "Adicionando espaço"
    st.text(" ")

    st.markdown("<p class='big-font3'><strong>Problemas</strong>:</p>", unsafe_allow_html=True)
    st.markdown("<p class='big-font2'>- Falta de profissionais de manutenção qualificados na empresa "
                "</p>", unsafe_allow_html=True)
    st.markdown("<p class='big-font2'>- Ajuda na produção contínua e manutenção remota de "
                "máquinas "
                "</p>", unsafe_allow_html=True)

    st.markdown("<p class='big-font2'>- Parte crucial do fluxo de produção: bomba que leva o óleo "
                "de fritura quente ao forno para fritar as batatas </p>", unsafe_allow_html=True)

    st.markdown("<p class='big-font2'>-<strong> Problemática principal</strong>: parafuso que dá suporte a bomba constantemente se solta, "
                "causando um perda de equilíbrio no eixo de acionamento e danificando a bomba "
                "</p>", unsafe_allow_html=True)

    # "Adicionando espaço"
    st.text(" ")

    st.markdown("<p class='big-font3'><strong>Soluções:</strong> "
                "</p>", unsafe_allow_html=True)
    st.markdown("<p class='big-font2'>-<strong> Solução tradicional</strong>: Monitoramento por Análise de Vibração"
                "</p>", unsafe_allow_html=True)
    st.markdown("<p class='big-font2'>-<strong> Solução otimizada</strong>: Sistema de Diagnóstico Sonoro que ajuda a "
                "detectar falhas mais cedo empregando Inteligência Artificial"
                "</p>", unsafe_allow_html=True)

    # "Adicionando espaço"
    st.text(" ")

    st.markdown("<p class='big-font3'><strong>Resultados:</strong> "
                "</p>", unsafe_allow_html=True)
    st.markdown("<p class='big-font2'>- <strong>Solução tradicional</strong>: alerta acionado somente quando "
                "o parafuso já estava solto a 270º</p>", unsafe_allow_html=True)
    st.markdown("<p class='big-font2'>- <strong>Solução otimizada</strong>: detecção imediata do problema. "
                "O sistema relatou uma anomalia na primeira volta de 90° do parafuso</p>", unsafe_allow_html=True)

    # "Adicionando espaço"
    st.text(" ")
    st.text(" ")

    st.markdown("<p class='big-font2'><strong>Fonte</strong>: https://www.neuronsw.com/case-studies"
                "/successful-diagnosis-of-a-pump-fault-using-sound-and-ai/ "
                "</p>", unsafe_allow_html=True)

    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        list-style-position: inside;
    }
    </style>
    ''', unsafe_allow_html=True)

# Página com a Ferramenta de Detecção no Streamlit
elif paginaSelecionada == "Detector de Anomalias":

    # Subtítulo - "Detector de Anomalias por Classificação de Áudio"
    st.subheader("Detector de Anomalias por Classificação de Áudio")

    # Fazendo o upload do arquivo de áudio
    uploaded_file = st.file_uploader("Escolha o arquivo de áudio que você deseja classificar:",
                                     type=[".wav", ".wave", ".mp3"], accept_multiple_files=False)

    # Tocando o arquivo
    if uploaded_file is not None:
        # Título - "Detector de Anomalias"
        st.subheader("Ouvir áudio")
        audio_bytes = uploaded_file.read()
        st.audio(audio_bytes, format="audio/wav")

        # Botão para gerar a classificação do áudio
        if st.button("Enviar"):
            # "Adicionando espaço"
            st.text(" ")

            lottie_file = r"C:\Users\liznm\PycharmProjects\DeteccaodeAnomaliasporAudio" \
                                  r"\lottie_animations\loading_soundwave_lf30_editor_32f2qhtv.json"

            lottie_json = load_lottiefile(lottie_file)
            with st_lottie_spinner(lottie_json, height=300):
                time.sleep(5)

                # Salvando o arquivo de som no caminho determinado
                def save_file(sound_file):
                    with open(os.path.join(r"C:\Users\liznm\PycharmProjects"
                                           r"\DeteccaodeAnomaliasporAudio\audio_file_upload", sound_file.name), 'wb') as f:
                        f.write(sound_file.getbuffer())
                        p = r"C:\Users\liznm\PycharmProjects" \
                            r"\DeteccaodeAnomaliasporAudio\audio_file_upload\{}".format(sound_file.name)
                        #print(p)
                    return p

                final_audio = save_file(uploaded_file)
                #print(final_audio)

                final_model = tensorflow.keras.models.load_model(r"C:\Users\liznm\PycharmProjects"
                                                 r"\DeteccaodeAnomaliasporAudio"
                                                 r"\saved_models\audio_anomaly_detection.h5")

                #loss, acc = final_model.evaluate(X_test, y_test)
                #print(acc)

                # Testando o modelo em arquivos de áudio
                def get_info(data, sample_rate):
                    st.write("Canais: ", str(len(data.shape)))
                    st.write("Taxa de amostragem: ", str(sample_rate))
                    st.write("Duração: ", str(len(data) / sample_rate))
                    return


                def predict_sound(arquivo_audio, info=False, plot_waveform=False, plot_spectrogram=False):
                    # Fazendo o pré-processamento dos dados
                    # Carregando o áudio
                    audio, sample_rate = librosa.load(arquivo_audio, sr=None, res_type="kaiser_fast")

                    # Extração de características MFCCs
                    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)

                    # Aplicando a normalização
                    mfccs_scaled_features = np.mean(mfccs_features.T, axis=0)

                    # Convertendo de vetor para matriz; pois precisamos enviar os dados para o Tensorflow
                    mfccs_scaled_features = mfccs_scaled_features.reshape(1, -1)

                    #  Adicionando a 3ª dimensão (cor)
                    mfccs_scaled_features = mfccs_scaled_features[:, :, np.newaxis]

                    # Gerando as probabilidades para cada classe, já que estamos usando a softmax
                    prediction = final_model.predict(mfccs_scaled_features)

                    # Extraindo o maior valor; argmax(axis=1) = para considerar as colunas
                    prediction = prediction.argmax(axis=1)

                    # astype(int) = Convertendo para inteiro; flatten() = transformando para vetor
                    prediction = prediction.astype(int).flatten()

                    # Dicionário com as classes
                    class_labels = {0:"abnormal", 1:"normal"}

                    # List Comprehension que gera o label(rótulo) da previsão
                    result = [audio for (number, audio) in class_labels.items() if prediction == number]
                    #print(result)

                    # Exibindo o resultado no streamlit
                    final_result = [st.markdown("Classificação/resultado: " + i) for i in result]

                    get_info(audio, sample_rate)

                    # Gerando a waveform
                    plt.figure(figsize=(14, 5))
                    plt.title("Tipo de som: {}".format(result[0].upper()), size=16)
                    plt.xlabel("Tempo")
                    plt.ylabel("Amplitude")
                    ld.waveshow(audio, sr=sample_rate)

                    # Salvando o waveplot como uma imagem
                    plt.savefig(r"C:\Users\liznm\PycharmProjects"
                                r"\DeteccaodeAnomaliasporAudio\waveplot_mfcc\waveplot.png")
                    st.write("Waveplot: ")
                    st.image((Image.open(r"C:\Users\liznm\PycharmProjects"
                                         r"\DeteccaodeAnomaliasporAudio\waveplot_mfcc\waveplot.png")), width=700)

                    # MFCC
                    # Gerando o mfcc
                    # y = corresponde as amostras de áudio
                    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)

                    # Gerando o espectograma
                    plt.figure(figsize=(14, 5))
                    mfccs_db = librosa.amplitude_to_db(np.abs(mfccs))
                    plt.title("Tipo de som: {}".format(str(result[0]).upper()), size=16)
                    ld.specshow(mfccs_db, x_axis="time", y_axis="log", cmap="Spectral")
                    plt.colorbar(format='%+2.f dB')

                    # Salvando o espectograma (mfcc) como uma imagem
                    plt.savefig(r"C:\Users\liznm\PycharmProjects"
                                r"\DeteccaodeAnomaliasporAudio\waveplot_mfcc\spec.png")
                    st.write("MFCC: ")
                    st.image((Image.open(r"C:\Users\liznm\PycharmProjects"
                                         r"\DeteccaodeAnomaliasporAudio\waveplot_mfcc\spec.png")), width=700)
                    return


                # Fazendo a previsão
                st.subheader("Previsão:")
                predict_sound(final_audio, info=True, plot_waveform=True, plot_spectrogram=True)

                # Função para deletar os arquivos de áudio da pasta
                def deleting_audio_files():
                    path_1 = Path(r"C:\Users\liznm\PycharmProjects\DeteccaodeAnomaliasporAudio"
                                  r"\audio_file_upload")
                    for item in path_1.glob("**/*"):
                        # Verifica o que está após o ponto "."
                        if item.suffix in ([".wav"]):
                            # Apaga os arquivos da pasta
                            os.remove(item)
                deleting_audio_files()

                # Função para deletar os mfccs da pasta
                def deleting_mfccs():
                    path_2 = Path(r"C:\Users\liznm\PycharmProjects\DeteccaodeAnomaliasporAudio"
                                  r"\waveplot_mfcc")
                    for item in path_2.glob("**/*"):
                        # Verifica o que está após o ponto "."
                        if item.suffix in ([".png"]):
                            # Apaga os arquivos da pasta
                            os.remove(item)
                deleting_mfccs()