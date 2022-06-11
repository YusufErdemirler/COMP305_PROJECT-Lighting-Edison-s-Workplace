# COMP305_PROJECT-Lighting-Edison-s-Workplace
Lighting Edison’s Workplace Algorithm Problem

Name: Yusuf Erdemirler ID: 68910
Name: Filiz Koç ID:69625

• The algorithm you designed to solve the problem, the choices of the data structures you used and your reasoning. 

My getLightedRoom() function counts how much of the area can be lit given x,y and Radius of the light source. It takes into account of being near a border and whether the area should be lit or is a wall. We then calculated how many areas needed to be lit and then found the maximum number of bulbs that should be used so as not to place more than that. We then brute-force calculated by stepping through the area one by one, checking how many of the area can be lit by placing in that position. If the light can be placed then we moved the position by a radius amount so as not to overlap the lights. We also checked if the cost of cable and bulb would not go over the budget. For our algorithm we did not use any special data structures aside from 2-D arrays.

• In addition to your actual code, write a pseudo code for your algorithm 

currCost = 0
totalNumberOfLit = 0

func getCost(i, j):
	return BulbCost + (EXcoord-i + EYcoord-j)*CableCost

for i = 0 to Rows:
	for j = 0 to Columns:
		getLitNumber = placeBulb(i, j)
		costOfBulb = getCost(i, j)
		if costOfBulb + currCost < Budget:
			totalNumberOfLit += getLitNumber
			currCost += costOfBulb
			i += LightRadius
			j += LightRadius 
print(totalNumberOfLit)

• Compare it with another algorithmic approaches 

When compared with a recursive approach we believe it performs better time-wise but doesn’t give as correct a solution. When compared with a graph traversal algorithm It performs the same time-wise but doesn’t give as correct a solution.

• The time complexity of your algorithm (and the space complexity if applicable) 

Since it is a greedy approach, the time complexity of our algorithm is 0(n*m*R*R) where n and m are the rows and columns, R is the radius of light. This is due to us checking every space to put a lightbulb. The space complexity is only O(n*m) because we only stored the Area into an array.

• Prove that your algorithms gives correct results 

We are sure our algorithm works near correctly as it is a greedy approach. We make sure that when placing a new light bulb that the budget constraint is satisfied and by checking the max number of lightbulbs that can be placed in theory, We make sure we do not create extra bulbs.

• Further improvements that can be done as future work

To improve the algorithm a DFS strategy could be used to isolate different rooms and then apply an algorithm to each room separately. This is useful to ensure that light doesn’t travel past enclosed spaces which we couldn’t find a solution to. Another improvement can be made to the way bulbs are placed by changing the map to make lit areas into “-“. A final improvement can be made as a recursive solution to make bulb placement more efficient by passing through the area again.
