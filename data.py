# import mysql.connector
# from dotenv import load_dotenv
# import os

# dotenv_path = "key.env" 

# load_dotenv(dotenv_path=dotenv_path)


# sqlpass = os.getenv('password')
# print(sqlpass)


movies = [(32281,"Your Name",8.8,2016,106,"CoMixWave","Drama"),
(38826,"Weathering With You",8.3,2019,112,"CoMixWave","Romance"),
(199,"Spirited Away",8.7,2001,124,"Ghibli","Adventure"),
(431,"Howl's Moving Castle",8.6,2004,119,"Ghibli","Adventure"),
(47,"Akira",8.1,1988,124,"TMS","Action"),
(31765,"Sword Art Online: Ordinal Scale",7.5,2017,119,"A1","Action"),
(28851,"A Silent Voice",8.9,2016,130,"Kyoani","Drama"),
(37987,"Violet Evergarden",8.9,2020,140,"Kyoani","Drama"),
(8487,"Legend of the Millennium Dragon",6.5,2011,98,"Pierrot","Action"),
(2236,"The girl who leapt through time",8.1,2006,99,"Madhouse","Supernatural")
]

staff = [
    (1870,"Miyazaki","Director",199),
    (1870,"Miyazaki","Director",431),
    (10801,"Itou","Director",2236),
    (10801,"Itou","Director",31765),
    (12411,"Kawasaki","Director",8487),
    (5067,"Hosoda","Director",2236),
    (1872,"Otomo","Director",47),
    (1872,"Otomo","Director",8487),
    (8129,"Ishidate","Director",28851),
    (8129,"Ishidate","Director",37987),
    (1117,"Shinkai","Original Story",32281),
    (1117,"Shinkai","Director",38826),
    (11466,"Kawahara","Original Story",31765)

]

studio = [
    (291,"CoMixWave",2007,2403),
    (21,"Ghibli",1985,9700),
    (56,"A1",2005,10492),
    (2,"Kyoani",1985,20099),
    (11,"Madhouse",1972,17731),
    (1,"Pierrot",1979,2630),
    (65,"TMS",1946,216)
]

'''
moviedb = mysql.connector.connect(host="localhost", user="root", password=sqlpass)
print(moviedb.connection_id) #check if we connected

'''