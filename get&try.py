# Get instance
import instaloader
import csv
import os.path
missing = answer = 0

L = instaloader.Instaloader()

with open('login/login+password.txt', 'r') as f:
    lines = f.readlines()
    username = str(lines[0][:-1])
    password = str(lines[1][:-1])
# Login or load session 
L.login(username, password)  # (login)
print("logged in")
# Obtain profile metadata
victimusername = input("Instagram victim username ?\n")

profile = instaloader.Profile.from_username(L.context,victimusername)
print("profile loaded")
# Print list of followees
follow_list = []
count = 0
followernum = profile.followers
followeenum = profile.followees
print("-")
with open('follower.csv', 'w') as f:
    for follower in profile.get_followers():
        follow_list.append(follower.username)
        f.write(follow_list[count])
        f.write("\n")
        count +=1
        print(f"creating follower.csv... {round(count*100/followernum,1)}%",end="")
        print("\r",end="")
count=0
print("follower.csv created             ")
with open('following.csv', 'w') as f:
    for follower in profile.get_followees():
        follow_list.append(follower.username)
        f.write(follow_list[count])
        f.write("\n")
        count +=1
        print(f"creating following.csv... {round(count*100/followeenum,1)}%",end="")
        print("\r",end="")
# (likewise with profile.get_followers())
print("following.csv created                    ")
print("-")
print("Done")

if os.path.isfile("follower.csv") == False:
    print("\"follower.csv\" is missing")
    missing=1
if os.path.isfile("following.csv") == False:
    print("\"following.csv\" is missing")
    missing=1
    
if missing == 1:
    print("Something went wrong, refer to \"readme.txt\" for further informations.")
    input()
    exit()

same = []
private = []

follower = []
with open('follower.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for ligne in spamreader:
        follower.append(ligne)
following = []
with open('following.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for ligne in spamreader:
        following.append(ligne)

if follower >= following:
    #print("more follower than following")
    biggest = follower
    smallest = following
else:
    #print("more following than follower")
    biggest = following
    smallest = follower

for i in range(len(biggest)):
    for j in range(len(smallest)):
        if biggest[i][0] == smallest[j][0]:
            same.append(biggest[i][0])
            pass
    print(f"checking follow back...{round((i+1)*100/len(biggest),1)}%",end="")
    print("\r",end="")
print("follow back - Done                                           ")
print("-")
print(f"Follow Back: {len(same)}\n----")

answer = input("save this result as  file ? y/n \n")
print("Follow Back:")

if answer == "y":
    with open('Follow Back.txt', 'w') as f:
        for i in range(len(same)):
            print(f"{same[i]} | https://www.instagram.com/{same[i]}/")
            f.write(f"{same[i]} | https://www.instagram.com/{same[i]}/ \n")
else:
    for i in range(len(same)):
        print(f"{same[i]} | https://www.instagram.com/{same[i]}/")

if answer == "y":
    print("\nFollow Back saved as \"Follow Back.txt\".\nDon't follow Back saved as \"X Follow Back.txt\".")
input("")

