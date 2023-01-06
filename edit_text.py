with open("2022-10-05-09-30_cut.txt", "r") as f:
    data = f.read()
    lines = data.split("\n")
# for line in lines:
#     print(line)
#     line = line.split(" ")
#     for i in line:
#         with open("a.txt", "a+") as a:
#             a.write(i+", ")
#     with open("a.txt", "a+") as a:
#             a.write("\n")
for line in lines:
    print(line)
    print(line[:-18] + " 1,1,1")
    with open("a.txt","a+") as a:
        a.write(line[:-18] + " 1,1,1\n")