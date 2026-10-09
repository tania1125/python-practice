def calculate_love_score(name1, name2):
    name = (name1 + name2).lower()
    LoveScore = 0
    true_count = sum(name.count(char) for char in "true")
    love_count = sum(name.count(char) for char in "love")
    
    LoveScore = (true_count*10) + love_count
    print(f"Love percentage is: {LoveScore}%")
    
First_name = input("Type name of first person: \n")
Second_name = input("Type name of second person: \n")

calculate_love_score(First_name, Second_name)
            