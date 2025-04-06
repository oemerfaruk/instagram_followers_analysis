import json

# read JSON File
with open("data/following.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# collect all "value" (usernames) values from following.json
following = []
for item in data.get("relationships_following", []):
    for string_data in item.get("string_list_data", []):
        following.append(string_data.get("value"))


# read JSON File
with open("data/followers_1.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# collect all "value" (usernames) values from followers_1.json
followers = []
for item in data:
    for string_data in item.get("string_list_data", []):
        followers.append(string_data.get("value"))


# by comparing the two lists
# find users who are in following but not in followers
not_following_back = [user for user in following if user not in followers]

# print the result
print("Users you are following but not followed back:")
for user in not_following_back:
    print(user)
