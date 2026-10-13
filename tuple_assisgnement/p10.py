 #Three sets of student names playing different sports
cricket = {"Aditya","shivam","Aayush","pratham"}
football = {"rahul","viom","Nitesh","pratham","Aditya"}
badminton = {"shreyansh","dhruv","pratham","shivam"}

print(f"Cricket players: {cricket}")
print(f"Football players: {football}")
print(f"Badminton players: {badminton}\n")

all_three = cricket & football & badminton
print(f"Students who play all three games: {all_three}")

at_least_two = (cricket & football) | (football & badminton) | (cricket & badminton)
print(f"Students who play at least two games: {at_least_two}")

all_players = cricket | football | badminton
only_one = all_players - at_least_two
print(f"Students who play only one game: {only_one}")
