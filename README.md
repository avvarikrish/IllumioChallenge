# IllumioChallenge

# How I tested the solution: 
I first did the tests that were provided in the instructions. After, I focused on edge cases such as the values that are at the port or ip ranges or false cases. Lastly, I tested the amount of my my code took by using the Python time feature and hardcoding 500,000 test rules into my rules.csv file. These tests were done using the main executable script that I used and I hardcoded some rules in the rules.csv file.

# Design
The main structure that I used to store the rules was a dictionary within a dictionary. I decided to split the direction of the packet as 2 separate keys. Within each key, I had another dictionary where I separated 
the protocols. Although this takes up space to store, this would help with time because the program would not have to search through the entire list of rules, just the ones
with the specified direction and protocol. The reason I decided to use direction and protocol as my keys is because they were single
strings as opposed to ports and ip's which had both single values and ranges. I also wanted to point out that I split everything up into
classes because it was easier to implement and in the case that another programmer wanted to expand on this project, it would be easier
for them to understand the code.

# Future improvements
Given more time, I would definitely have done more proper testing with unit tests. This would help me keep my tests
more organized. Another major improvement I would try to make is the data structure that I used. Even though I split up the directions and 
protocols with Python dictionaries, I could split it up even further by separating ranges and single values for port and ip values. I would utilize a 2 Hashmaps: 1 for
single value ports and another for range ports. The keys would be hash values for the port and the values would be lists of ip values that fall
under the same rule as the port values. The main challenge would be coming up with a clever way of storing hash values for port ranges and 
how we would compare the port-to-check hash value with the Hashmap keys. This definitely increases the speed because instead of looping through
all the rules of a specific direction and protocol, we can get the hash value of the port we're trying to search for and simply check if it exists.

# Additional Info
I definitely enjoyed this project and I wanted to thank the Illumio team for taking the time to read through my application and coding challenge.

# Teams
Platform (I believe I was given the challenge directly from this team)
