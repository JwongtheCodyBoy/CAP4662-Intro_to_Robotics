Things for grader (because my file hierarchy kind of bad)

	HW4 Q1 File	-	"RRTPlanner.py"
				Path beings at 46 seconds
	
	HW 4 Q2 File	-	"InterpolatingPolynomial.py"
				The Interpolated Path begins at 00:01:01	(1 min 1 sec) 


	Joint angles start and end
		Start Position = [0, 0, 0, 0, 0, 0]  
		End Position = [45, 45, 45, 45, 45, 0]



Minor Documentation stuff

	To change step size (how big each movement of RRT should be)
		+ go to "class RRTPlanner" -> "def __init__" -> Change step_size
		+ bigger number = faster program runs but less detail path
		+ smaller number = slower program run but more detailed

	RRTPlanner
		Random_sample: Randomly create new angles between -180 and 180, 10% chance to just pass the end goal's angle


		Nearest_node: Find nearest node from current position


		Steer: Function that creates new nodes and add them to the tree


		Plan: Uses iteration to begin the RRT


		Extract_path: use back tracking to retrieve the path as a list from the tree



	InterpolatingPolynomial:
		Calculate_coefficients: using Lecture 12 formulas and Start end goal to find coefficents

		
		Interpolate_segment: generates interpolated angles for each segment

		
		Execute_path: tell robot to follow the interpolated path
