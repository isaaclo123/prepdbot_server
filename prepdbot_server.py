__author__ = "Isaac Lo"
__copyright__ = "Copyright 2015"
#PrepdBot Server

import socket
import feedparser
import pickle

#network information
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

#feed urls
RSSFeeds = [
["http://feeds.reuters.com/reuters/businessNews", "Buisness"],
["http://feeds.reuters.com/reuters/companyNews", "Companies"],
["http://feeds.reuters.com/reuters/environment", "Environment"],
["http://feeds.reuters.com/news/wealth", "Money"],
["http://feeds.reuters.com/Reuters/PoliticsNews", "Politics"],
["http://feeds.reuters.com/Reuters/domesticNews", "Domestic News"]
]

print "PrepdBot Server"
print "Server Info: " + str(TCP_IP) + ":" + str(TCP_PORT) + "\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

Cuts = 0

while True:
    for i in xrange(0,len(RSSFeeds)):
        links = feedparser.parse(RSSFeeds[i][0])

        for j in xrange(0,len(links["entries"])):
            conn, addr = s.accept()
            TheLink = links.entries[j]['link']
            FolderName = RSSFeeds[i][1]
            print "Client Address: ", addr
            print "Link: " + TheLink
            print "Folder Name: " + FolderName
            #send data
            conn.send(pickle.dumps([TheLink, FolderName]))
            #increment number of articles cut
            Cuts = Cuts + 1
            print "Articles Cut: " + str(Cuts) + "\n"
