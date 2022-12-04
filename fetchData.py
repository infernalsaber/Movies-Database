import requests, json

def getDuration(
    duration: str, episodes: int
)-> int:
    """Generate the duration in minutes from the duration string and no of episodes

    Args:
        duration (str): duration string to be parsed
        episodes (int): no of episodes

    Returns:
        int: total duration of series in minutes
    """
    duration = duration.split(" ")
    try:
        time = int(duration[0])*60 + int(duration[2])
    except ValueError:
        time = int(duration[0])
    # print("Time is ", time)
    
    # episodes = episodes.split(" ")[0]
    
    return time*episodes

def fetchDataStaff(
    staffId: int, role: str
)-> tuple:
    """A function to generate the details of a staff member

    Args:
        staffId (int): id of the staff member
        role (str): their role in the production

    Returns:
        tuple: output tuple with their details
    """
    query = requests.get(f"https://api.jikan.moe/v4/people/{staffId}")
    print(query)
    query = query.json()["data"]
    q1 = []
    q1.append(int(staffId))
    q1.append(query["name"])
    q1.append(role)
    q1.append(query["favorites"])
    print(tuple(q1))


def fetchDataStudio(
    studioId: int
)-> tuple:
    """A function to generate the details of a studio corresponding to a particular series

    Args:
        studioId (int): ID of the studio whose details are required

    Returns:
        tuple: A tuple containing the id, title, year of establishment and favourites of the studio
    """
    query = requests.get(f"https://api.jikan.moe/v4/producers/{studioId}").json()["data"]
    q1 = []
    q1.append(int(studioId))
    q1.append(query["titles"][0]["title"])
    q1.append(query["established"].split("-")[0])
    q1.append(query["favorites"])
    print(tuple(q1))
    


def fetchDataAnime(
    aniId: int
)-> tuple:
    """A function to find out details of a particular anime series/movie using its ID

    Args:
        aniId (int): ID of the series on MAL

    Returns:
        tuple: A tuple containing the id, name, rating, year, 
        duration (mins), studio and primary genre of the entity
    """
    try:
        query = requests.get(f"https://api.jikan.moe/v4/anime/{aniId}/full").json()["data"]
    except KeyError:
        print("\nNo entry exists for the given id, try another.")
        return
    q1 = []
    q1.append(aniId)
    q1.append(query["title"])
    q1.append(query["score"])
    q1.append(query["year"] or query["aired"]["from"].split("-")[0])
    q1.append(getDuration(query["duration"], query["episodes"])) #needs work
    q1.append(query["studios"][0]["name"])
    q1.append(query["genres"][0]["name"])
    print(tuple(q1))
    
    #Get the details of the corresponding studio
    fetchDataStudio(query["studios"][0]["url"].split("/")[-2])
    
    # for i in range(1000):
    #     pass
    
    #Get details of important staff members
    import time
    numStaff = 2 #no of staff members
    for i in range(numStaff):
        x = requests.get(f"https://api.jikan.moe/v4/anime/{aniId}/staff").json()
        # print(x)
        x = x["data"]
        # print("Getting details of member ", i)
        
        # fetchDataStaff(x[i]["person"]["mal_id"], x[i]["positions"][0]) #kinda imp
        
        # print("Got details of member ", i)
        
        qt = (x[i]["person"]["mal_id"], x[i]["person"]["name"], x[i]["positions"][0], int(aniId))
        print(qt)
        
        time.sleep(0.3) #In order to handle API rate limitation

if __name__ == "__main__": 
    x = None
    while(not x):
        try:
            x = int(input("Enter id: "))
            fetchDataAnime(x)
        except ValueError:
            print('\nEnter a valid integer value.')