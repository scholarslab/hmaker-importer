import json

missing = 0
birthlocs = {}
with open("PoliticalBios.json","r") as biosjson:
    bios = json.load(biosjson)
    for url in bios:
        if "Birth Location:" in bios[url]:
            name = bios[url]["name"]
            birthloc = bios[url]["Birth Location:"]
            if birthloc in birthlocs:
                birthlocs[birthloc].append(url)
            else:
                birthlocs[birthloc] = [url]


    count2 = 0
    for k in sorted(birthlocs, key=lambda k: len(birthlocs[k]), reverse=True):
        if len(birthlocs[k])>1:
            print("\n\n\n")
            count2+=1
            print(k)
            print("<strong>"+str(len(birthlocs[k]))+" PoliticalMakers"+"</strong>")
            print("<ul>")
            for url in birthlocs[k]:
                print("<li><a href=\""+url+"\">"+bios[url]["name"]+"</a></li>")
            print("</ul>")