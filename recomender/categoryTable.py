import json
import unicodedata as uni

def findUniqueValues(dict):
    n = 0
    items = []
    for key in dict:
        if dict[key] not in items:
            items.append(dict[key])
            n = n + 1
    print n

def helper(child, dict, id, categories):
    par = uni.normalize('NFKD', id).encode('ascii','ignore')
    chi = uni.normalize('NFKD', child["id"]).encode('ascii','ignore')
    if par in categories:
        if chi in categories:
            dict[chi] = chi
            for ch in child["categories"]:
                helper(ch, dict, child["id"], categories)
        else:
            dict[chi] = par
            for ch in child["categories"]:
                helper(ch, dict, id, categories)

def makeProperJson(file, fileOut):
    with open(file, "rb") as fin:
        content = json.load(fin)
    with open(fileOut, "wb") as fout:
        json.dump(content, fout, indent=1)

def readCategories(file):
    arr = []
    f = open(file, "r")
    for line in f:
        arr.append(line.split(":")[0])

    return arr

def main():

        #### Available categories ####
    categories = readCategories("categories.txt")
    #print len(categories)
    #Check points: up until index 10 it is touristic sites. 15-18 Travel and transport
    dict = {}
    data = json.load(open("all_cats_json.json"))
    parents = data["response"]["categories"]
    for parent in parents:
        id = parent["id"]
        for child in parent["categories"]:
            helper(child, dict, id, categories)


    #categories = ["4d4b7104d754a06370d81259", "4d4b7105d754a06374d81259", "4d4b7105d754a06376d81259", "4d4b7105d754a06377d81259", "4d4b7105d754a06379d81259"]
    # for key in dict.keys():
    #     if dict[key] not in categories:
    #         del dict[key]
        # elif dict[key] == categories[0]:
        #     dict[key] = "56aa371be4b08b9a8d5734db,4fceea171983d5d06c3e9823,4bf58dd8d48988d1e2931735,5032792091d4c4b30a586d5c,56aa371be4b08b9a8d573532,4deefb944765f83613cdba6e,4bf58dd8d48988d181941735,507c8c4091d498d9fc8c67a9,4bf58dd8d48988d184941735,4bf58dd8d48988d17b941735"
        # elif dict[key] == categories[-1]:
        #     dict[key] = "4bf58dd8d48988d1ed931735,4bf58dd8d48988d1fe931735,4f4530164b9074f6e4fb00ff,4bf58dd8d48988d129951735"

    findUniqueValues(dict)

    with open('file.txt', 'w') as file:
        file.write(json.dumps(dict))

    makeProperJson("file.txt", "newmf.json")
    #print "\n" + str(len(dict))

if __name__ == '__main__':
    main()
