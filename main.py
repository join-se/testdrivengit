def test_classification():
  classification(45,90,180) #This is not a triangle

def test_sum_angles():
  classification(60,60,60)

def classification(a,b,c):
  if a+b+c == 180:
    print("This IS a triangle")
  else:
    print("This is not a triangle")
        
if __name__ == "__main__":
  print("Starting test")
  test_classification()
  test_sum_angles()
  print("Ending test")
