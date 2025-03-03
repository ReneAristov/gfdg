def generate_report(data):
    ip_count = data[0]
    error_count = data[1]
    print(data[0])
    print(data[1])
    with open("report.txt","w") as file:
        file.write("Loogianalüüs raport \n")
        file.write("Kõige aktiivsem ip oli: \n")
        for ip,count in ip_count.items():
          file.write(f"{ip}: {count} korda \n")
          
        file.write("\nKõige sagedasemad vead: \n")
        for error, count in error_count.items():
            file.write(f"{error}: {count} korda \n")