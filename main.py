from audio_worker import *
import openai



# вызов функции STT
# audio_worker_func()


####### блок с переменными

file_text = 'output_10_new — копия.txt'
file_text_path = 'A:\\Programming\\PyProj\\Anna_tasks\\done_text\\'
name_output_doneText = 'outpug_gpt_prompt.txt'



#задание того, что должен сделать бот
prompt_text = 'Резюмируй текст записи собрания, выдели основные тезисы и разбей по пунктам текст:'

# Replace YOUR_API_KEY with your OpenAI API key
openai.api_key = ""

# text-davinci-003 - модель gpt-3 {gpt-3.5-turbo-0301, text-davinci-003 }
model_engine = "text-davinci-003"

#######

with open("{0}{1}".format(file_text_path, file_text), "r") as file:
    text = file.read()

# задаем промпт
# prompt = f'{prompt_text}\n{text}'

# задаем макс кол-во слов(токенов, отношение НЕ 1 к 1), только 4097 токенов
max_tokens = 4097

# генерируем ответ

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": f'{prompt_text}\n{text}'}]
)



# completion = openai.Completion.create(
#     engine=model_engine,
#     prompt=prompt,
#     max_tokens=1024,
#     temperature=0.5,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
# )








# выводим ответ
print('ответ бота:')
print(completion.choices[0].message.content)

with open("A:\\Programming\\PyProj\\Anna_tasks\\done_text\\{0}".format(name_output_doneText), "w") as file:
    # file.write(completion.response_ms[0].text) # для openai.Completion.create
    file.write(completion.choices[0].message.content)







