"""
A poll...
Everyone responding to this poll chooses between a blue or red pill.

- if > 50% of people choose the blue pill, everyone lives
- if not, red pills live and blue pills die

In other words, if more than 50% of people choose the blue pill everyone lives.
If less than or equal to 50% choose the blue pill, everyone dies.

Blue pill > 50%: everyone lives
Blue pill <= 50%, blues die
"""
import random as random

# randomly generate an 100 count array of color blue, and color red as strings
## blue = 0, red = 1
## calculate % type(float) blue: red / blue 
# take data array in arg 
# calculate % red and % blue

def generate_zero_one():
    return int(random.randint(0,1))

def generate_array():
    sample = [generate_zero_one() for i in range(10000)]
    return sample

def tally():
    tally_sample = generate_array()
    tally_list = [0, 0]
    
    for number in tally_sample:
        if number == 0:
            tally_list[0] += 1
        else:
            tally_list[1] += 1
    return tally_list

def percentage():
    tally_list = tally()
    blue = tally_list.pop(0)
    percent_blue = ((blue / 10000) * 100)
    print(percent_blue)
    return percent_blue

def main():
    the_blue_pill = percentage()
    if the_blue_pill > 50.00:
        print(f"The Blue pillers voted {the_blue_pill:.2f}%. Everyone lives")
    else:
        the_red_pill = 100 - the_blue_pill
        print(f"The Red Pill voted {the_red_pill:.2f}%. Blue pillers die.")
    return


if __name__ == "__main__":
    main()