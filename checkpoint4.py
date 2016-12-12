from pymongo import MongoClient
client = MongoClient()

if __name__ == '__main__':

	db = client.csci2963
	collection = db.definitions

	# find all
	print "====== FIND ALL ======"
	print [word_def for word_def in collection.find()]


	print "====== FIND ONE ======"
	print collection.find_one()


	print "====== FIND SPECIFIC (smile) ======"
	print collection.find_one({ "word": "smile" })


	print "====== FIND BY ID (smile) ======"
	print collection.find_one({ "_id" : "56fe9e22bad6b23cde07b8db" })


	print "====== INSERT (dog) ======"
	print collection.insert({ "word": "dog", "definition": " n. a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, and a barking, howling, or whining voice. It is widely kept as a pet or for work or field sports." })

