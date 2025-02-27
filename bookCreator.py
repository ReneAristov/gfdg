def guestBook():
    name = input("Sinu nimi: ")
    comment = input("sinu sõnum: ")
    text = f"Nimi: {name}, Sõnum:  {comment}"
    file = open("guestBook.txt", "a", encoding="utf-8")
    file.write(text)
    file.close()
    print("Sõnum oli salvestatud edukalt")