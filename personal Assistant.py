import speech_recognition as s_r
print("I have just born, Give some time for me to learn")
r = s_r.Recognizer()
my_mic_device = s_r.Microphone(device_index=1)
with my_mic_device as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
my_string=r.recognize_google(audio)
print(my_string)
if "hi" in my_string:
   print("hi there,mr torettos, i am thankful for creating me!")