class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        # The idea of this is to use list sorting with a flag(while True)
        # We first create the flag/indefinate loop while True
        # We could have used the on/off button for the flag, but it would make our
        # algorithm way too long. at least when I tried this at first.
        # Notice that the very first item the robot holds is a None object
        # We must swap the None object before we start the loop
        # We then move right swapping while possible. our goals are:
        # Goals:
        # 1. Sort all items
        # 2. Push None object at the very right-most end of the list
        # 3. Hold the greatest item to be swaped with None object on #2
        # 4. break the indefinent loop when all is sorted

        # Tip: the best way to visualize this is to make physical cards to sort
        #       it was the only way I could figure all of this out!

        # you start off with None object so you must swap to proceed with sorting
        self.swap_item()

        while True:
            #while moving right is valid...
            while self.move_right():
                #print(self._list)
                # swap items if condition is met
                if self.compare_item() >=1:
                    self.swap_item()
                    #print(f'Swap: {self._item}')
                    #print(self._list)

                    #if you are at the end of the list AND the item to be compared is none
                    # swap the items and break the loop
            if self.can_move_right() == False and self.compare_item() == None:
                self.swap_item()
                #print(f'Swap none: {self._item}')
                #print(self._list)
                break
            while self.move_left():
                if self.compare_item() == None:
                    self.swap_item()
                    self.move_right()
                    self.swap_item()
                    break # to avoid infinite loop
                    
##  some sorta pseudo code from the start               
##        swap_happened = True
##        while swap_happened:
##            swap_happened = False
##            for num in range(len(self._list)-1):
##                if self.compare_item() == 1:
##                    swap_happened = True
##                    self.swap_item()
##                    return self._list
                    
                    
                    
        



if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    #l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]
    l = [12,5,1]
    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
