with open('data.txt') as f:
    source = f.read().splitlines()

    dest = open("processed_data.csv", "w")
    dest.write("\"city\",latitude,longitude,population\n")

    #print("name,latitude,longitude")

    for line in source:
        fields = line.split('\t')

        if int(fields[14]) > 100000:
        	dest.write("\""+fields[1]+"\","+fields[4]+","+fields[5]+","+fields[14]+"\n")
        #print(fields[1], fields[4], fields[5], sep=",")

print("Done!")