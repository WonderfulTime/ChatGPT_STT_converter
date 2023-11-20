import speech_recognition as speech_r
import pyaudio
import wave
import soundfile as sf
import librosa as librosa
import json



class Audio:

    def __init__(self, name_output_doneText: str, raw_name_file: str, path_cut_files: str, cut_files_name: str, path_files: str):

        self._name_output_doneText = name_output_doneText
        self._raw_name_file = raw_name_file
        self._path_cut_files = path_cut_files
        self._cut_files_name = cut_files_name
        self._path_files = path_files



    @property
    def name_output_doneText(self)-> str:
        return self._name_output_doneText

    @property
    def raw_name_file(self) -> str:
        return self._raw_name_file

    @property
    def path_cut_files(self) -> str:
        return self._path_cut_files

    @property
    def cut_files_name(self) -> str:
        return self._cut_files_name

    @property
    def path_files(self) -> str:
        return self._path_files





audio_1 = Audio('a','aboba', 'a', 'a', 'a')

print(audio_1.raw_name_file)

print(audio_1)

def audio_worker_func():
    ########    блок для изменения значений переменных
    name_output_doneText = 'output_10_new.txt'
    raw_name_file = 'GPT_test_24.05.wav'
    path_cut_files = 'A:/Programming/PyProj/Anna_tasks/handing/'
    cut_files_name = 'split_' #без номера
    path_files = '' #должно быть пусто, костыль
    ########

    # ### костыли
    # iteration_cut_file = 0 # инициализация
    # ###


    def cutting_module(raw_name_file) -> int:

        file_path = "A:/Programming/PyProj/Anna_tasks/handing/"
        file_path_full = "A:/Programming/PyProj/Anna_tasks/raw_audio/"

        file_name = file_path_full + str(raw_name_file)
        audio, sr = librosa.load(file_name)

        # Длина файла (после обрезки)
        buffer = 300 * sr

        samples_total = len(audio)
        samples_wrote = 0
        counter = 1

        while samples_wrote < samples_total:

            #check if the buffer is not exceeding total samples
            if buffer > (samples_total - samples_wrote):
                buffer = samples_total - samples_wrote

            block = audio[samples_wrote : (samples_wrote + buffer)]
            out_filename = file_path + "split_" + str(counter) + ".wav"

            # Write 2 second segment
            sf.write(out_filename, block, sr)
            counter += 1
            samples_wrote += buffer
        return counter

    r = speech_r.Recognizer()


    ################GPT_test_24.05.wav
    text = []


    def startConvertion(path= path_files) ->str:
        with speech_r.AudioFile(path) as source:
            # with sample as audio:
            # content = r.record(source)


            # r.adjust_for_ambient_noise(source)

            print('Получение файла')
            audio_text = r.listen(source)
            # Метод recoginize_() выдает ошибку запроса, если API недоступен, поэтому используется обработка исключений.
            try:
                # using google speech recognition
                print('Конверт аудио в текст...')
                text.append(r.recognize_google(audio_text, language="ru-RU"))
                print("Готово!")
                return text

            except:
                print('Произошла ошибка, требуется перезапуск')



    iteration_size = cutting_module(raw_name_file)

    ###цикл загона разделенных звуковых файлов для обработки через google API

    for i in range(1, iteration_size):

        path_files = f'{path_cut_files}{cut_files_name}{i}.wav'
        startConvertion(path_files)

    ###

    with open("A:\\Programming\\PyProj\\Anna_tasks\\done_text\\{0}".format(name_output_doneText), "w") as file:
        file.write(''.join(map(str, text))) # записываем наш массив из текста
        # json.dump(text, file)

    ###########################################################



