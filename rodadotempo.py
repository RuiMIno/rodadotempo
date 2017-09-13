# rules for description O: Output   I: input
import calendar                                                # We use the calendar functions modules
calend_text = calendar.TextCalendar()                           # Create a Calendar in Text format
calend = calendar
inpresult = 0
ly = 0
rly = 0
firstWeekDay = 0
# How to find the Weekday any day from 1900 to 2108
# The strategy is based in the knowledge of the especial years which hold a specific feature:
#   be a leap year which first weekday of the years is a Monday. they happen any 28 years.
#   we use the year 1912 as the inicial BASE YEAR for calculation.
print("\n          How to find the   WEEKDAY NAME   of any day from 1912 to 2080   MENTALLY  . \n")
print("     The strategy is based in the knowledge of specials years which hold an specific feature:")
print("     Be an   LEAP YEAR   which   FIRST WEEKDAY  of the years is a Monday..")
print("     These situation only happen every 28 years for an 100 year interval. ")
print("     We use the year   2080   as the initial   BASE LEAP YEAR   to do the calculations \n")
print("     This allow us to find out the FIRST WEEKDAY of the year between the years 1912 - 2080  easily")
print("             So  ...  Lets star.   GIVE ME AN DATE   and lets try find the   WEEKDAY NAME for that date \n")

anoBiRef = int(1901)
anoRange = [anoBiRef, 2080]

while True:                                                 # I: Repeat until input is complete
    inpDia = int(input('Dia: '))                            # I:(inpDia)
    inpMes = int(input('Mes: '))                            # I:(inpMes)
    inpAno = int(input('Ano: '))                            # I:(inpAno)
    if anoBiRef >= inpAno or inpAno >= anoRange[1]:         # T: if year input is in range(1912, 2100)
        print(" The year must be between 1900 and 2080 \n")
        continue                                             # F: back to WHILE statement
    elif 0 >= inpMes or inpMes >= 12:                        # T: if month input is in range(1 - 12)
        print(" The month must be between 1 and 12 \n")
        continue                                             # F: back to WHILE statement
    elif 0 >= inpDia or inpDia >= calendar.monthrange(inpAno, inpMes)[1]:  # T: if day input is valid for month and year
        print(" The day of monthh ", inpMes, " of ", inpAno, " must be between 1 and",
              calendar.monthrange(inpAno, inpMes)[1], "\n")
        continue
    else:
        break

print(" Good, Lets do it step by step.\n")
print(" First: How many years there are between the BASE LEAP YEAR ", anoRange[1], " and   OUR YEAR DATE   ", inpAno)
print(" ", anoRange[1], "-", inpAno, "= \n")

testeFunc = True
while testeFunc:
    testeFunc = False
    inpresult = int(input("\n Enter Result "))
    if inpresult != (anoRange[1] - inpAno):
        testeFunc = True
        continue
    else:
        break

print(" Well, now we gonna find out how many   LEAP YEARS(LY)   are")
print(" by the expression: ", inpresult, "// 4 \n")

print(" And how many days left ")
print(" by the expression: ", inpresult, "% 4\n")

testeFunc = True
while testeFunc:
    testeFunc = False
    inply = int(input(" result for numbers of LEAP YEARS: "))
    inprly = int(input(" result for number of years left: "))
    ly = int(divmod(inpresult, 4)[0])
    rly = int(divmod(inpresult, 4)[1])
    if inply == ly and inprly == rly:
        break
    else:
        print(" Not good, try again!")
        testeFunc = True
        continue

print(' Next step we gonna find the   FIRST WEEKDAY of OUR YEAR DATE.')
print(" using the expression = [ ( number of LEAP YEARS * 2 ) - ( numbers of years left ) ] % 7 .\n")
print(" between LEAP YEARS the FIRST WEEK DAY shift 2 days: ( number of LEAP YEARS * 2 )")
print(" then we subtract the number of years left and apply the arithmetic modulo for 7 ( number of days in a week)")
print(" and VOILA, we should have the   FIRST WEEK DAYS   of the year for our date")

testeFunc = True
while testeFunc:
    testeFunc = False
    inpresult = int(input(" Can you give me these number? "))
    firstWeekDay = (ly*2 - rly) % 7
    if inpresult != firstWeekDay:
        testeFunc = True
        continue

print("  thats it...!\n")
print("  the number: ", firstWeekDay, " is  the   FIRST WEEKDAY   of our year date ", inpAno, "...")
print("  ... and represents the number of days after MONDAY as showed in the table below.  \n")
print("  0 = Monday, 1 = Tuesday, 2 = Wednesdays, 3 = Thursday, 4 = Friday, 5 = Saturday, 6 = Sunday")
checkCalend = calend.day_name[firstWeekDay]
print("  so, day ", firstWeekDay, "is ", checkCalend, "\n")
justwait = input("hit enter to continue")

print("  \n")
print(" Now we gonna find the WEEKDAY of our date.")
print(" For that we will use one of the two tables depending of our year being or not a LEAP YEAR. ")
print(" the  TABLES  represents for a given month as index the shifts in days from the   FIRST WEEKDAY of the year.\n")
print("              Month = [-, J, F, M, A, M, J, J, A, S, O, N, D, J]")
print(" For NON LEAP YEARS = [0, 0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5, 1]\n")
print("          Month = [-, J, F, M, A, M, J, J, A, S, O, N, D, J]")
print(" For LEAP YEARS = [0, 0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6, 2]\n")
inpMesname = calendar.month_name[inpMes]
a = calendar.isleap(inpAno)
print("having Day =", inpDia, ",Month =", inpMesname,
      ",FIRST WEEKDAY of year =", firstWeekDay, ",is LEAP DAY?", a, "\n")
print(" using the expression: (TABLE[our MONTH date] + FIRST WEEK DAY of  year + our DAY date) % 7 ")

twheel = [0, 0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5, 1]
twheelly = [0, 0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6, 2]

if calendar.isleap(inpAno):
    weekdaydate = (twheelly[inpMes] + firstWeekDay + inpDia) % 7
else:
    weekdaydate = (twheel[inpMes] + firstWeekDay + inpDia) % 7

testeFunc = True
while testeFunc:
    testeFunc = False
    inpresult = int(input(" Can you tell me the final value for WEEKDAY of our date? \n"))
    if not inpresult == weekdaydate:
        testeFunc = True
        print(" Noooo, keep trying")
        continue

checkCalend = calend.day_name[weekdaydate]
print(" YES,  is the number", weekdaydate, "and it represents one", checkCalend, "\n")

print(" We Start with the follow knowledge:")
print(" We find the WEEKDAY for our date by tracking the shifts of WEEKDAY  between years from a initial situation")
print(" BASE LEAP YEAR: 2080,      FIRST WEEKDAY of BASIC LEAP YEAR = MONDAY")
print(" LEAP YEARS happens each 4 years, that is why divide the difference between the years by 4")
print(" Between LEAP YEARS there is a shift of 2 day in the WEEKDAY that is why we multiply by 2")
print(" We use a table to easily find out the shift inside the year ")
print(" And time to time we calculate the mod by 7 to reduce the shift count to a weekday range ")
