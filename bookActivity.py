import datetime
def ActivityBook():
    name = input("Sinu nimi: ")
    action = input("sinu tegevus: ")
    time = datetime.datetime.now()
    text = f"Date: {time} Nimi: {name}, Tegevus:  {action}\n"
    file = open("ActivityBook.txt", "a", encoding="utf-8")
    file.write(text)
    file.close()
    print("Tegevus oli salvestatud edukalt")