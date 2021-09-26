#Program to analyze the weekly homework points of a university module

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

def point_perc(s:str):
    l = points_sum(s)
    perc = round(l[0] / l[1],2) * 100
    return str(int(perc)) + "%"

print(point_perc("c_points.csv"))