# Lift Simulator
class lift():
  # Initialises with:
  # Capacity, floor (defaults to ground), and operation status (defaults to in operation)
  def __init__(self,capacity,currentFloor=0,inOperation=True):
    self.capacity = capacity
    self.currentFloor = currentFloor
    self.inOperation = inOperation

  # Returns the lift's curreent floor
  def getFloor(self):
    return self.currentFloor

  # Sets currentFloor to the floor specified
  def moveFloor(self, floor):
    self.currentFloor = floor

  # When cast to string, returns information about self as a string
  def __str__(self):
    return f"In Operation?:{self.inOperation}\nCurrent Floor:{self.currentFloor}\nCapacity:{self.capacity}\n"

# Creates a dict of 3 lifts and feeds capacities, defaults of floor 1 and inOp for other
lifts = {
  0:lift(10),
  1:lift(8),
  2:lift(12)
}

def main():
  global lifts
  uFloor = int(input("Welcome to the Grand Hotel. Please enter your current floor."))
  distanceToU = []
  for lift in lifts.values():
    if lift.inOperation:
        dist = lift.getFloor()
        dist = uFloor - dist
        dist = abs(dist)
        distanceToU.append(dist)
  uLift = lifts[distanceToU.index(min(distanceToU))]
  uLift.moveFloor(uFloor)
  print(uLift)

if __name__ == "__main__":
  main()