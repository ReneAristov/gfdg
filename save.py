def save():
    name = input("Sinu nimi: ")
    action = input("sinu vanus: ")
    user_id = (int(open("last_id.txt").read()) + 1) if os.path.exists("last_id.txt") else 1
    text = f"Date: {time} Nimi: {name}, Vanus:  {action}\n"
    file = open("save.txt", "a", encoding="utf-8")
    file.write(text)
    file.close()
    print("Info oli salvestatud edukalt")