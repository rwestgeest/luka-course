mean_temps= open("mean_temp.csv","a+")
mean_temps.write ("Rio de Janeiro,Brazil,30.0,18.0\n")
mean_temps.seek(0)
headings= mean_temps.readline()
headings=headings.split(",")

city_temp=[]
line=mean_temps.readline()
while line != "":
    city_temp.append(line.split(","))
    line=mean_temps.readline()

for city in city_temp:
    print(headings[0].capitalize() +" of "+ city[0] + " "+ headings[2]+ " is "+city[2]+" Celsius")

mean_temps.close()