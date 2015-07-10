def test_classification():
	classification(45,90,180) #This is not a triangle

def test_sum_angles():
	classification(60,60,60)

def test_right_angle():
	classification(90,45,45)

def classification(a,b,c):
	if a+b+c == 180:
		print("This IS a triangle")

		if a == 90 or b == 90 or c == 90:
			print("... by the way, it's also a RIGHT triangle")
		elif a == 60 and b == 60 and c == 60:
			print(", an equilateral triangle!")
	else:
    		print("This is not a triangle")
        
if __name__ == "__main__":
  print("Starting test")
  test_classification()
  test_sum_angles()
  test_right_angle()
  test_equilateral()
  print("Ending test")
