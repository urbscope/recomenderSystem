import json
categoryName = []
categoryId = []
categoryParent  = []


def extractCategories(filename):

	rawList = open(filename,'r')

	listcontent = rawList.read()
	rawJson = json.loads(listcontent)

	categoriesList = rawJson['response']['categories']

	for parentCategory in categoriesList:
		parent = None
		catName = parentCategory['pluralName']
		catId = parentCategory['id']
		categoryName.append(catName)
		categoryId.append(catId)
		categoryParent.append(parent)
		levelId = catName

		lev1List = parentCategory['categories']
		for sub1Category in lev1List:
			parent = levelId
			catName = sub1Category['pluralName']
			catId = sub1Category['id']
			categoryName.append(catName)
			categoryId.append(catId)
			categoryParent.append(parent)
			level1Id = catName

			lev2List = sub1Category['categories']
			for sub2Category in lev2List:
				parent = level1Id
				catName = sub2Category['pluralName']
				catId = sub2Category['id']
				categoryName.append(catName)
				categoryId.append(catId)
				categoryParent.append(parent)
				level2Id = catName


	print categoryName

	with open('catIndex.txt', 'wb') as outfile:
		for i in range(0, len(categoryName)):
			outfile.write(str(categoryId[i]) + ":" +str(categoryName[i]) + ":" + str(categoryParent[i]) + "\n")
	with open('data.json', 'w') as outfile:
	    json.dump(categoriesList, outfile, indent = 4)
	    
extractCategories('categories_Urbscope.json')
