def pool_tips(hours_s=8, hours_bb=12, hours_bar=12, tips_cc=500, manager=False, wage_bb=7.5, wage=3.33, wage_m=10):

    """F(X) POOLS TIPS OVER MULTIPLE EMPLOYEES WITH DIFFERENT HOURLY PAY RATES"""

    #server is paid $3.33/hr and works shorter hours than the bar staff(bartender or manager, barback)
    #bartender is paid $3.33/hr and works the same hours as the barback
    #barback is paid $7.5/hr and works the same hours as the bartender or manager
    #manager is paid $10/hr and works instead of the bartender

    assert type(float(hours_s)) == float, 'hours_s is invalid'
    assert type(float(hours_bb)) == float, 'hours_bb is invalid'
    assert type(float(hours_bar)) == float, 'hours_bar is invalid'
    assert type(float(tips_cc)) == float, 'tips_cc is invalid'
    assert type(bool(manager)) == bool, 'manager is invalid'
    assert type(float(wage_bb)) == float, 'wage_bb is invalid'
    assert type(float(wage)) == float, 'wage is invalid'
    assert type(float(wage_m)) == float, 'wage_m is invalid'
    #test value types enterted into function are correct

    hours_total = hours_s + hours_bar + hours_bb
    #sums total hours of all employees, bartender hours and managers hours are the same

    if manager == True:
        hours_s_adj = (wage_m-wage)*hours_s
        hours_bar_adj = (wage_m-wage_bb)*hours_bar
    else:
        hours_s_adj = (wage_bb-wage)*hours_s
        hours_bar_adj = (wage_bb-wage)*hours_bar

    tips_adj = tips_cc - (hours_s_adj + hours_bar_adj)
    #adjust total tips by the adjusted hour rate
    #this accounts for the different hourly rate of each employee based on the number of hours worked

    tips_total_s = (
        (tips_adj/hours_total)*hours_s) + hours_s_adj
    #sum server tips by hours worked, adjusted for pay rate
    if manager == True:
        tips_total_bar = (tips_adj/hours_total)*hours_bar
        tips_total_bb = (
            (tips_adj/hours_total)*hours_bb) + hours_bar_adj
    else:
        tips_total_bar = (
            (tips_adj/hours_total)*hours_bar) + hours_bar_adj
        tips_total_bb = (tips_adj/hours_total)*hours_bb
    #sum bar/barback tips by hours worked, adjusted for pay rate and if manager was present

    tips_total_bar_r = round(tips_total_bar, 2)
    tips_total_s_r = round(tips_total_s, 2)
    tips_total_bb_r = round(tips_total_bb, 2)
    #round curreny values to the hundreth decimal place (penny)

    rate_s = round(
        ( ( tips_total_s_r + ( wage * hours_s ) ) / hours_s ), 2)
    rate_bb = round(
        ( ( tips_total_bb_r + (wage_bb * hours_bb) ) / hours_bb ), 2)
    #calculate hourly rate by total tips, wage, and hours worked

    if manager == True:
        rate_bar = round(
            ( ( tips_total_bar_r + (wage_m * hours_bar) ) / hours_bar ), 2)
    else:
        rate_bar = round(
            ( ( tips_total_bar_r + (wage * hours_bar) ) / hours_bar ), 2)
    #calculate hourly rate by total tips, wage, hours worked, and if a manager was present

    assert rate_s == rate_bb == rate_bar, 'Hourly rate is incorrect, tips not pooled accurately'
    #assert that the hourly rate of each employee is equal

    rate = round(
        ( ( rate_s + rate_bb + rate_bar ) / 3 ), 2)
    #produce a variable for the hourly rate of all employees rounded to the hundreth decimal

    print('Bartender tips: ' + str(tips_total_bar_r) +
    '\n' + 'Barback tips: ' + str(tips_total_bb_r) +
    '\n' + 'Server tips: '  + str(tips_total_s_r) +
    '\n' + '\n' + 'Total tips: ' + str(tips_cc) +
    '\n' + 'Hourly rate: ' + str(rate))
    #display final pooled tip values for each employee

pool_tips(6, 9.5, 9.5, 549.1, True)
