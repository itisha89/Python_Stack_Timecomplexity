class Stack:
    size = -1  # Initialize Size of Stack to -1, Empty Stack

    def __init__(self, size):
        """
        Initialize an empty Stack
        """
        self.size = size
        self.data = []

    def push(self, value):
        """
        Pushes an element to a Stack
        """
        if len(self.data) < self.size:
            self.data.append(value)
        else:
            raise Exception("Can't push Element, Stack is Full")

    def pop(self):
        """
        Pops an element from the stack and return it.
        """
        if len(self.data) < 1:
            raise Exception("No elements to pop, Stack is Empty")
        else:
            removed_element = self.data[-1]
            del self.data[-1]
            return removed_element

    def isEmpty(self):
        """
        Returns if Stack is Empty or not
        """
        return len(self.data) < 1

    def __len__(self):
        """
        This is a special method of python classes and is called
        when we want to get the length of the object of the class eg: len(Stack())
        """
        return len(self.data)

inputFileHandle = open('inputPS02.txt', "r")  # Create Input File Handle to Read Contents.
inputFileLines = inputFileHandle.readlines()  # Reading All Lines from Input File.

outputFileHandle = open('outputPS02.txt', "w")

for inputFileLine in inputFileLines:
    elements = inputFileLine.translate({ord(i): None for i in '[]\n'}).split(',')  # Scrubbing to remove extra chars
    heightList = [int(element) for element in elements]  # List of Building Heights

    stack = Stack(len(heightList))  # Initializing Size = Num of Building as at Max all building can have river view

    maxHeight = heightList[-1]  # Setting Maximum Height to the Height of the First Building
    stack.push(len(heightList) - 1)  # Pushing the First Building as it will always have the River View

    for index in range(len(heightList) - 2, -1, -1):  # Irritating all building height in Reverse except first building
        if heightList[index] > maxHeight:
            stack.push(index)  # Push the new building to the Stack
            maxHeight = heightList[index]  # Update Max Height with the Height of the Newly Pushed Building

    reversedList = []  # Pop All Elements of Stack to Create a Reversed List / Increments of Index
    while not stack.isEmpty():
        reversedList.append(stack.pop())

    outputFileHandle.write(str(reversedList).replace(' ', '') + '\n')  # Write Increments of Index to File
outputFileHandle.close()  # Close File Handle
