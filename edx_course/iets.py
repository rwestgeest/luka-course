print("ga ik doen")
schools = open("school_names.txt", "r") 
schools.seek(5,0)
print(schools.read(1))
schools.seek(3,1)
print(schools.read(1))
print("done")