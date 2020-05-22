s1 = int(input("Enter score of first player: "))
s2 = int(input("Enter score of second player: "))
s3 = int(input("Enter score of third player: "))
strike1 = s1 * 100/60
strike2 = s2 * 100/60
strike3 = s3 * 100/60
print("Strike rate of player 1 is: ", strike1)
print("Strike rate of player 2 is: ", strike2)
print("Strike rate of player 3 is: ", strike3)
ns1=s1*2
ns2=s2*2
ns3=s3*2
print("Score if they played 60 balls more-: ")
print("player 1- ",ns1)
print("player 2- ",ns2)
print("player 3- ",ns3)
print("Maximum sixes player 1 could have hit: ",(s1//6))
print("Maximum sixes player 2 could have hit: ",(s1//6))
print("Maximum sixes player 3 could have hit: ",(s1//6))
