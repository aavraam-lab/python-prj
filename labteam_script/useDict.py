#Python script to read data from a file and construct dictionaries with actions available on them.

import os


database = {}

def initiliaze_system():
    inputFile = open("inputTeams.txt","r+")
    line_buf = []

    while True:
        lineReading = inputFile.readline()
        if not lineReading: break
        
        line_buf = lineReading.split()
        
        try:
            database[line_buf[0]] = [line_buf[1], line_buf[2]]
        except:
            database[line_buf[0]] = [line_buf[1]]
    

def merge_odd():
    keys = database.keys()
    team_toCheck = []
    odd_teams = []

    for key in keys:
        team_toCheck = database[key]
        if(len(team_toCheck)==1):
            odd_teams.append(key)

    length = len(odd_teams)

    for i in range (0,length,2):
        try:
            new_team = [database[odd_teams[i]],database[odd_teams[i+1]]]
            del database[odd_teams[i+1]]
            new_team[0] = new_team[0][0]
            new_team[1] = new_team[1][0]
            database[odd_teams[i]] = new_team
        except:
            pass

def print_database():
    for key in database.keys():
        print(key + ": ", end = "")
        print(database[key])

def search_Team():
    
    key = input("\nWhat is the key of the team to search?: ")
    try:
        team = database[key]
        print("The members of the team: ",team)
    except:
        print("Team not found!")

def search_Student():

    studentCode = input("\nWhat is the student code to search?: ")
    keys = database.keys()

    for key in keys:
        team = database[key]
        try:
            team.index(studentCode)
            print("The team of the student is: ",key, " : ",team )
            print()
        except:
            pass

def main():

    initiliaze_system()

    while True:
        userSelection = int(input('Enter selection (1-5): '))

        if(userSelection==1):
            print("We are merging odd teams.....\n")
            merge_odd()
        elif(userSelection==2):
            print("Here's the database: ")
            print_database()
            print("")
        elif(userSelection==3):
            search_Team()
            print("")
        elif(userSelection==4):
            search_Student()
        elif(userSelection==5):
            print("\nGoodbye..")
            break
        else:
            pass

main()