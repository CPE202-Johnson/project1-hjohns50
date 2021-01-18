# int -> booelan
# Given integer n, returns True or False based on reachabilty of goal
def bears(n):
    #basecase
    if n == 42:
        return True
    #when n becomes less that 42 that trial is over
    elif n < 42:
        return False
    #tests n trying to have n equal to 42
    else:
        if n % 2 == 0 and bears(n/2):
            return True
        if (n % 3 == 0 or n % 4 == 0) and bears(n-((n%10)*((n%100)//10))):
            return True
        if n % 5 == 0 and bears(n - 42):
             return True
    return False