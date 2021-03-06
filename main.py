def test_classification():
    classification(45,90,180) #This is not a triangle

def test_sum_angles():
    classification(60,60,60)

def test_right_angle():
    classification(90,45,45)

def test_acute():
    classification(80, 40, 60)

def classification(a,b,c):
    if a+b+c == 180:
        print("This IS a triangle")
        if a == 90 or b == 90 or c == 90:
            print("... by the way, it's also a RIGHT triangle")
        if a < 90 and b < 90 and c < 90:
            print("... by the way, it's also an ACUTE triangle")
    else:
        print("This is not a triangle")
        
if __name__ == "__main__":
  print("Starting test")
  test_classification()
  test_sum_angles()
  test_right_angle()
  test_acute()
  print("Ending test")
