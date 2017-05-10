import argparse
import pymongo
from pymongo import MongoClient

import store_data_LEAVE
import store_data_RETURN


client = MongoClient()
db = client['STUDENT_INFO']
collection = db["id_student"]
collection2 = db["student_log"]


def is_Match(ID, collection):
    if(find_id(collection, ID)):
        #return true
        print "ID FOUND"
        return True
    else:
        print "NO MATCH FOUND"
        return False
#connect to Mongo above
#search for a matching ID from mongo database
#report results

def find_id(collection_name, id_arg):
    '''
    If specified ID is in the collection the find_one function
    will return it.
    '''
    id_entry = collection_name.find_one({'id' : id_arg})
    return id_entry


def is_id_trash(ID):
   '''calls the appropriate script based on whether or not the ID passed from David is actually .
   :param ___: takes a
   :return: calls appropriate scrip based on the true/false options
   '''
   # use regex
    if  for x in ID:
            #make x be the ascii value
        if(ord(x) >= 48 and ord(x) <= 57) and len(ID) == 5:
        return False
        #the string is not trash
    else:
        return True
        #the string is trash
        # will prompt the user to re enter ID

        #If it does return false, I think this is where it would call one of David's functions
        #prompting the user to re-enter their ID

        # this is just for testing



def main(args):
    enteredID = args["ID"]
    #rework
    if is_id_trash(enteredID)
        #call David with error message
        return 1

    if !is_Match(enteredID, collection)
        return 1
        #do reporting
    if(args["returning"]):
        pass
        return store_data_LEAVE.main(args)
        #call haley returning

    else:
        #call haley leaving
        return store_data_RETURN.main(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ID", help="student ID must match the one in the file")
    parser.add_argument("returning", help="default is true, false if leaving", store_action=False)
    #change these arguments
    args = vars(parser.parse_args())
    main(args)
