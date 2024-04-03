# Asking the user their time spent on each event of a triathlon
swim = int(input("How long did you swim? "))
run = int(input("How long did you run? "))
cycle = int(input("How long did you cycle? "))

# Calculating the total time spent in a triathlon
totalTime = swim + run + cycle

# Determining the award

if totalTime <= 100:
    print("Award: Provincial Colours")
elif totalTime <= 105:
    print("Award: Provincial Half Colours")
elif totalTime <= 110:
    print("Award: Provincial Scroll")
else:
    print("No award")
