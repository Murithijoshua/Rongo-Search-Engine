def main():
    
        avg_intgrs = open('numbers.txt','r')

        total = 0

        numb_of_lines=0

        line = avg_intgrs.readline()
        while line != '':
            numberoflines+=1

            total+= int(line)
            line = avg_intgrs.readline()

            average = total/numb_of_lines
            print(average)

            avg_intgrs.close()

        main()
