import random 

dice_input = input('Please enter your desired dice roll in the proper dice notation; eg. n1d1m1 operation n2d2m2...:')
dice_list = dice_input.split()

rolled_dice_list = []
to_add_list = []

for i in dice_list: 
	if any(c.isalpha() for c in i): 
		rolled_dice = i.split('d')
		number_of_dice = int(rolled_dice[0])
		while number_of_dice != 0:
			rolled_dice_result = random.randint(1,int(rolled_dice[1]))
			to_add_list.append(rolled_dice_result)
			#print(to_add_list)
			number_of_dice = number_of_dice - 1 
		rolled_dice_sum = sum(to_add_list)
		rolled_dice_list.append(rolled_dice_sum)
	else: 
		rolled_dice_list.append(i)
		
final_dice_result = ''.join(str(j) for j in rolled_dice_list)
final_dice_result = (eval(final_dice_result)
print(final_dice_result) 

if str(final_dice_result).isdigit(): 
    print('Your final dice result is: ' + str(final_dice_result) + '. Yay!') 
else: 
	print('Boo, your input was incorrect. Please use an appropriate operator. The options are: \'+\', \'-\', \'*\', and \'/\'. If operator use was not the issue, please double check the rest of your notation.')

	  

	