#UNHOUS = UNHOUS
#EH = EARLHM
#WARREN
#EDWARD
#MARSHL
#OA = OLVEYA
#MILLS
#Hoerner = HOERNR
#EXEMPT
#WILSON
#RUSSEL
#HICKS
#OFF-C
def main():
    fopen = open("Data.txt","r")
    fout = open("Results.txt","w")
    test = False
    for line in fopen:
        if "img" in line:
            line_save_2 = line
        if "a href" in line and "earlham.edu" not in line:
            line_save = line
        if "UNHOUS " in line:
            #fout.write(line_save)
            fout.write(line_save_2)

    fopen.close()
    fout.close()
main()





fopen = open("Results.txt","r")
fout = open("Results.html","w")
for line in fopen:
    check = False
    url = ""
    count = 0
    for word in line:
        if word == '"':
            check = not check
            count += 1
        elif check == True:
            url += word
        if count == 2:
            break
    url = '<img src="https://tentram.earlham.edu:8250' + url + '"/>\n'
    fout.write(url)
