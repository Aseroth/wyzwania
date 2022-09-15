one_mile = 1.6
dist_to_moon = 383400

daily_distance = 60*2*one_mile
weeks = 0
weekly_distance = 5*daily_distance
traveled_so_far = 0
while  traveled_so_far<= dist_to_moon*2:
    traveled_so_far+=weekly_distance
    weeks+=1

print(weeks/52, traveled_so_far)