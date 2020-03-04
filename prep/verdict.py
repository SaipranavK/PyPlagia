import globals
import sys

#Declaration Activity
def verdict(res,plagFactor):
    if(res):
        print('----------------------------------------------')
        print("Plagarised")
        if(plagFactor<=1):
            print("\nPercentage of Match = ",(plagFactor*100),"%","\nWith: ",globals.comparisionName)
        else:
            print("\nPercentage of Match = 100%","\nWith: ",globals.comparisionName)
        sys.exit()
    else:
        print('----------------------------------------------')
        print("Percentage = ", (plagFactor*100),"%\n")