with open("input.txt", "r") as file:
    sum = 0
    
    for line in file:
        numbers = []
        for char in line:
            if char.isnumeric():                
                numbers.append(int(char))
        if len(numbers)>1:
            number = int(str(numbers[0]) +str(numbers[-1]))
        else:
            number = int(str(numbers[0]) +str(numbers[0]))
        sum = sum + int(number)
            
        print(numbers)
        print("total" , sum)
    
            
