#module 1 : create a blockchain
#to be installed
# we need to install flask first. for that we use pip install Flask==0.12.2 in anaconda promt
#and then we install postman http client : www.postman.com

#import the libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify

#part 1 building a blockchain
    
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1,previous_hash = 'o')  #here the proof is given after mining and after mining the block will be created
        #these chain and create block are required to make a block after mining, but first lets create the function of this create block
        
        
    def create_block(self,proof,previous_hash): # this will take the prev arguments
    #lets take a variable called block and add all the things the block contains in the dic from as keys, they are  index, time,proof, date, hash, prev hash etc etc

        block={'index': len(self.chain) + 1, 
               'timestamp': str(datetime.datetime.now()), # in datetime lib inside datetime module we are accessing now function which will give us the exact date and time when the block is created
               'proof': proof, #later on we will add the proof of work function and link it to the prood here
               'previous_hash': previous_hash
               'data': }
         
        self.chain.append(block) #apending the blockc that is created to the chain in the form of list
        return block


#part 2 mining a blockchain

