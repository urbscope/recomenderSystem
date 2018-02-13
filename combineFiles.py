
def main():
    user_data = "user_data.txt"
    cordinates = "cordinates.txt"
    final_data = "data.txt"

    fr_data = open(user_data, "r")
    fr_cordinates = open(cordinates, "r")
    fw = open(final_data, "a+")

    user = fr_data.readlines()
    cord = fr_cordinates.readlines()

    for i in xrange(len(user)):
        data1 = user[i].split("|")
        data2 = cord[i].split("|")
        if data1[1] == data2[0]:
            fw.write(data1[0]+"|"+data2[0]+"|"+data2[1]+"|"+data2[2][:-1]+"|"+data1[2])

    fr_data.close()
    fr_cordinates.close()
    fw.close()

if __name__ == '__main__':
    main()
