



#Part 1

class stadium:
   """Summarizes stadiums"""
    def __init__(self, name, city_state, capacity):
         """INITILIZES ATTRIBUTES OF A STADIUM"""
        self.name = name
        self.city_state = city_state
        self.capacity = capacity
       

    def describe_stadium(self):
        """simulates a decription of a stadium."""
        print("The" + self.name + "is located in" + self.city_name + "and holds" + self.capacity + "fans.")

    
    stadium1 = stadium("Mercedes Benz Arena", "Atlanta, GA", "70,000")



 @staticmethod
    def sports_played():
        """This method should accept one argument that specifies the sport that is played"""
        print("The following sport is mainly played in this stadium:" + stadium.sports_played)

@staticmethod 
    def seats_available():
        """specifies how many seats are available"""
        print("There are" + stadium.seats_available + "seats still available for tonight's game.")


stadium.describe_stadium()
print(stadium1)

stadium.sports_played()

stadium.seats_available()


#Each of the above method should print out a sentence using the argument provided (see step 4 for output)
#Using the stadium1 instance, call each of the new methods, providing the relevant arguments. As an example, if the following code to use the class were added:
#After running this program in your terminal, the output should be similar to the following:
#The Mercedes Benz Arena is in Atlanta, GA and holds 70000 fans.
#The following sport is mainly played in this stadium: Football
#There are 15000 seats still available for tonight's game.