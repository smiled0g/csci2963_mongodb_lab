from pymongo import MongoClient
from random import randrange
import datetime
client = MongoClient()


def random_word_requester(collection):
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''

    all_words = [word for word in collection.find()]
    selected = all_words[randrange(len(all_words))]

    collection.update(
    	{ "_id": selected['_id'] },
    	{
    	  "$push": { "data": datetime.datetime.utcnow() }
    	}
    )

    selected = collection.find_one({ "_id": selected['_id'] })

    return selected


if __name__ == '__main__':

	db = client.csci2963
	collection = db.definitions

	print random_word_requester(collection)
