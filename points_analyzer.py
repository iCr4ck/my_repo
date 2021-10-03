#Program to analyze the weekly homework points of a university module
import matplotlib.pyplot as plt

def points_sum(s: str) -> str:
    my_sum = 0
    max_sum = 0
    with open(s) as f:
        c = 0
        for line in f:
            if c > 0:
                for i in range(len(line)):
                    if line[i] == ",":
                        if line[i+1:i+6][-1] == ",":
                            my_sum += float(line[i+1:i+5])
                        elif line[i+1:i+6][-1] == "1":
                            my_sum += float(line[i+1:i+4])
                        else:
                            my_sum += float(line[i+1:i+6])
                        max_sum += float(line[-5:])
                        break
            c += 1
    return [my_sum,max_sum]


def point_perc(s:str)->str:
    l = points_sum(s)
    perc = round(l[0] / l[1],2) * 100
    return str(int(perc)) + "%"
    


def csv_to_list(s:str)->list:
    point_lst = []
    max_points_lst = []
    with open(s) as f:
        c = 0
        for line in f:
            if c > 0:
                for i in range(len(line)):
                    if line[i] == ",":
                        if line[i+1:i+6][-1] == ",":
                            point_lst.append(float(line[i+1:i+5]))
                        elif line[i+1:i+6][-1] == "1":
                            point_lst.append(float(line[i+1:i+4]))
                        else:
                            point_lst.append(float(line[i+1:i+6]))
                        max_points_lst.append(float(line[-5:]))
                        break
            c += 1
    return [point_lst,max_points_lst]

my_p = csv_to_list("c_points.csv")[0]
max_p = csv_to_list("c_points.csv")[1]

x = [x for x in range(1,len(my_p)+1)]

#plotting
plt.plot(x, my_p,label = "Erreichte Punkte",linestyle= "dashed",marker = "o")
plt.plot(x,max_p,label = "Maximal erreichbare Punkte")

#labeling
plt.xlabel("Blätter")
plt.ylabel('Punkte')
plt.title('Vorlesung: C')

plt.legend()
plt.show()



