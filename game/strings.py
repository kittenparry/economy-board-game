
def strings(s):
    str = {
        "no_money": "Not enough money.",
        #errors
        "err_pc": "Enter a number between 2-4 please.",
        "err_yn": "Enter y or n only.",
        "err_n": "Enter a number between 1-%d.",
        #die
        "roll_die": "%s rolled %d and %d, a total of %d.",
        "roll_3_d": "%s rolled 3 doubles back to back and will go to jail.",
        "roll_d": "%s rolled a double and will roll again.",
        #move
        "move_pass_GO": "%s passed GO and collected $%d as their salary.",
        "move_buy_prop": "%d: %s, costs $%d. Purchase? (y/n)",
        "move_pay_tax": "%s paid $%d in %s.",
        "move_visit_jail": "%s is visiting jail.",
        #pay_rent
        "rent_house": "%s has %d houses. Rent is $%d.",
        "rent_hotel": "%s has a hotel. Rent is $%d.",
        "rent_none": "Rent of %s is $%d.",
        "rent_station": "%s owns %d station(s). Rent is $%d.",
        "rent_util_2": "%s owns both of the utilities. Roll die and pay 10 times.",
        "rent_util_1": "%s owns one of the utilities. Roll die and pay 4 times.",
        "rent_pay": "%s has paid %s a total of $%d.",
        "rent_fail": "%s doesn't have enough money to pay the rent.",
        #maybe no_money instead?
        #auction
        "auction": "%s decides not to buy %s. An auction is now in session.\nHighest bidder gets the property.",
        "auc_bids": "Bids so far are:",
        "auc_list": "%s\t$%d",
        "auc_or_s": "Enter an amount between $%d-$%d. Or type \"s\" to skip.",
        "auc_win": "%s is the highest bidder with $%d.",
        #choose_mortgage
        "mort_need": "%s currently has $%d and need a total of $%d.",
        "mort_cho": "Choose one of the following to mortgage by typing its ID.",
        "mort_list_title": "ID\tValue\tColour\tName",
        "mort_list": "%d\t$%d\t%s\t%s",
        "mort_full": "%s mortgaged %s for $%d and paid their debt of $%d.",
        "mort_some": "%s mortgaged %s for $%d and paid some of their debt.",
        #bankruptcy
        "bankrupt": "%s didn't have the property or money to pay their debt and is bankrupt.",
        #build_house
        "house_max": "%s already has the max number of houses (4).",
        "house_none": "%s doesn't have any houses.",
        "house_some": "%s has %d house(s).",
        "house_question": "How many houses would you like to build?",
        "house_build": "%s paid $%d to build %d house(s) on %s.",
        "house_total": "It now has %d house(s) in total.",
        "house_colours": "%s needs all the properties of %s colour to build houses.",
        #cc_pay_for_houses_hotels
        "cc_hh_count": "%s has a total of %d house(s) and %d hotel(s).",
        "cc_hh_fee": "Total fee is %d.",

    }
    return str.get(s)
