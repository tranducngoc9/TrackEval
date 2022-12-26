with open ("/home/ngoc/Documents/TrackEval/data/gt/mot_challenge/MOT17-train/MOT17-02-DPM/gt/gt.txt","r") as f:
    data = f.read()
    data = data.split("\n")
    a = []
    for line in data:
        line = line.split(",")
        try:
            if line[7]=="1":
                a.append(line)
        except:
            pass

with open("a.txt", "w") as f:
    f.write(str(a))