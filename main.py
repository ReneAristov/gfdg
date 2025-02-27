file = open("myFile.txt","w")
file.write("myText")

file.close()
import bookCreator as bookCreator
import bookActivity as bookActivity
import fileReader as reader
import save as save

def main():
    print("1 - külalisteraamat")
    print("2 - tegevusteraamat")
    print("3 - file lugemine")
    print("4 - save")
    userInput = input("Sinu valik: ")
    if userInput == "1":
        bookCreator.guestBook()
    elif userInput == "2":
        bookActivity.ActivityBook()
    elif userInput == "3":
        userFile = input("Milline file sa tahad lugeda?")
        reader.readFile(userFile)
    elif userInput == "4":
        save.save()
    
    else:
        print("vale valik")
        
main()
