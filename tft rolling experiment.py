"""
script to find the average gold needed to hit a better chosen than thresh at level 7
"""
import random


class Unit:
    def __init__(self, uid, name, cost, origin, trait, origin2=None):
        self.uid = uid
        self.name = name
        self.cost = cost
        self.origin = origin
        self.trait = trait
        self.origin2 = origin2
        self.chosen = False
        self.chosenbuff = None


def main():
    # initialize the unit pool
    one_costs = []
    two_costs = []
    three_costs = []
    four_costs = []
    five_costs = []
    for i in range(1, 30):
        # one cost initialization
        one_costs.append(Unit("diana" + str(i), "diana", 1, "moonlight", "assassin"))
        one_costs.append(Unit("elise" + str(i), "elise", 1, "cultist", "keeper"))
        one_costs.append(Unit("fiora" + str(i), "fiora", 1, "enlightened", "duelist"))
        one_costs.append(Unit("garen" + str(i), "garen", 1, "warlord", "vanguard"))
        one_costs.append(Unit("lissandra" + str(i), "lissandra", 1, "moonlight", "dazzler"))
        one_costs.append(Unit("maokai" + str(i), "maokai", 1, "elderwood", "brawler"))
        one_costs.append(Unit("nami" + str(i), "nami", 1, "enlightened", "mage"))
        one_costs.append(Unit("nidalee" + str(i), "nidalee", 1, "warlord", "sharpshooter"))
        one_costs.append(Unit("tahm kench" + str(i), "tahm kench", 1, "fortune", "brawler"))
        one_costs.append(Unit("twisted fate" + str(i), "twisted fate", 1, "cultist", "mage"))
        one_costs.append(Unit("vayne" + str(i), "vayne", 1, "dusk", "sharpshooter"))
        one_costs.append(Unit("wukong" + str(i), "wukong", 1, "divine", "vanguard"))
        one_costs.append(Unit("yasuo" + str(i), "yasuo", 1, "exile", "duelist"))

        # 2 costs
        if i < 23:
            two_costs.append(Unit("annie" + str(i), "annie", 2, "fortune", "mage"))
            two_costs.append(Unit("aphelios" + str(i), "aphelios", 2, "moonlight", "hunter"))
            two_costs.append(Unit("hecarim" + str(i), "hecarim", 2, "elderwood", "vanguard"))
            two_costs.append(Unit("janna" + str(i), "janna", 2, "enlightened", "mystic"))
            two_costs.append(Unit("jarvan iv" + str(i), "jarvan iv", 2, "warlord", "keeper"))
            two_costs.append(Unit("jax" + str(i), "jax", 2, "divine", "duelist"))
            two_costs.append(Unit("lulu" + str(i), "lulu", 2, "elderwood", "mage"))
            two_costs.append(Unit("pyke" + str(i), "pyke", 2, "cultist", "assassin"))
            two_costs.append(Unit("sylas" + str(i), "sylas", 2, "moonlight", "brawler"))
            two_costs.append(Unit("teemo" + str(i), "teemo", 2, "spirit", "sharpshooter"))
            two_costs.append(Unit("thresh" + str(i), "thresh", 2, "dusk", "vanguard"))
            two_costs.append(Unit("vi" + str(i), "vi", 2, "warlord", "brawler"))
            two_costs.append(Unit("zed" + str(i), "zed", 2, "ninja", "shade"))

        # 3 costs
        if i < 19:
            three_costs.append(Unit("akali" + str(i), "akali", 3, "ninja", "assassin"))
            three_costs.append(Unit("evelynn" + str(i), "evelynn", 3, "cultist", "shade"))
            three_costs.append(Unit("irelia" + str(i), "irelia", 3, "enlightened", "adept", "divine"))
            three_costs.append(Unit("jinx" + str(i), "jinx", 3, "fortune", "sharpshooter"))
            three_costs.append(Unit("kalista" + str(i), "kalista", 3, "cultist", "duelist"))
            three_costs.append(Unit("katarina" + str(i), "katarina", 3, "warlord", "assassin", "fortune"))
            three_costs.append(Unit("kennen" + str(i), "kennen", 3, "ninja", "keeper"))
            three_costs.append(Unit("kindred" + str(i), "kindred", 3, "spirit", "hunter"))
            three_costs.append(Unit("lux" + str(i), "lux", 3, "divine", "dazzler"))
            three_costs.append(Unit("nunu" + str(i), "nunu", 3, "elderwood", "brawler"))
            three_costs.append(Unit("veigar" + str(i), "veigar", 3, "elderwood", "mage"))
            three_costs.append(Unit("xin zhao" + str(i), "xin zhao", 3, "warlord", "duelist"))
            three_costs.append(Unit("yuumi" + str(i), "yuumi", 3, "spirit", "mystic"))

        # 4 costs
        if i < 13:
            four_costs.append(Unit("aatrox" + str(i), "aatrox", 4, "cultist", "vanguard"))
            four_costs.append(Unit("ahri" + str(i), "ahri", 4, "spirit", "mage"))
            four_costs.append(Unit("ashe" + str(i), "ashe", 4, "elderwood", "hunter"))
            four_costs.append(Unit("cassiopea" + str(i), "cassiopea", 4, "dusk", "mystic"))
            four_costs.append(Unit("jhin" + str(i), "jhin", 4, "cultist", "sharpshooter"))
            four_costs.append(Unit("morgana" + str(i), "morgana", 4, "enlightened", "dazzler"))
            four_costs.append(Unit("riven" + str(i), "riven", 4, "dusk", "keeper"))
            four_costs.append(Unit("sejuani" + str(i), "sejuani", 4, "fortune", "vanguard"))
            four_costs.append(Unit("shen" + str(i), "shen", 4, "ninja", "adept", "mystic"))
            four_costs.append(Unit("talon" + str(i), "talon", 4, "enlightened", "assassin"))
            four_costs.append(Unit("warwick" + str(i), "warwick", 4, "divine", "hunter", "brawler"))

        # 5 costs
        if i < 11:
            five_costs.append(Unit("azir" + str(i), "azir", 5, "warlord", "keeper"))
            five_costs.append(Unit("ezreal" + str(i), "ezreal", 5, "elderwood", "dazzler"))
            five_costs.append(Unit("kayn" + str(i), "kayn", 5, "tormented", "shade"))
            five_costs.append(Unit("lee sin" + str(i), "lee sin", 5, "divine", "duelist"))
            five_costs.append(Unit("lillia" + str(i), "lillia", 5, "dusk", "mage"))
            five_costs.append(Unit("sett" + str(i), "sett", 5, "boss", "brawler"))
            five_costs.append(Unit("yone" + str(i), "yone", 5, "exile", "adept"))
            five_costs.append(Unit("zillean" + str(i), "zillean", 5, "cultist", "mystic"))

    unit_pool = [one_costs, two_costs, three_costs, four_costs, five_costs]
    pity_timer = 0

    # function for rolling a chosen unit DOES NOT CHOOSE CHOSEN TRAIT
    def chosen_helper(units):
        """
        returns a chosen unit
        :return:
        :rtype: Unit
        """
        # take a random unit using chosen chances
        unit_cost = random.choices(units, weights=(0, 30, 40, 30, 0))[0]
        chosen = random.choice(unit_cost)
        chosen.chosen = True
        return chosen

    # rolling function with scaling pity timer. ONLY FOR LEVEL 7
    def roll(u_pool, p_timer):
        """
        simulate roll.
        chosen odds, then cost odds, then random unit.
        repeat 5 times for shop then return the 5 units in a list
        :return:
        :rtype: list
        """
        shop_chosen = True
        units = []
        for counter in range(5):
            # if chosen is available
            if shop_chosen:
                chosen_unit = bool(random.choices([0, 1], weights=(80 - p_timer, 20 + p_timer))[0])
                if chosen_unit:
                    shop_chosen = False
                    units.append(chosen_helper(u_pool))

                else:
                    # normal unit which ups the pity timer
                    unit_cost = random.choices(u_pool, weights=(19, 35, 30, 15, 1))[0]
                    units.append(random.choice(unit_cost))
            else:
                # always normal unit if chosen not available
                unit_cost = random.choices(u_pool, weights=(19, 35, 30, 15, 1))[0]
                units.append(random.choice(unit_cost))
        return units

    # going for just dusk riven
    acceptable_chosens = ["aatrox", "cassiopea", "jhin", "riven"]

    # going for any transitionw
    # acceptable_chosens = ["irelia", "jinx", "nunu", "veigar", "yuumi", "aatrox", "ahri", ashe", "cass", "jhin",
    # "morg", "riven", "sej", "shen", "talon", "warwick"]

    gold_needed = []
    # execute simulation
    num_trials = 10000
    for x in range(num_trials):
        # roll for units, check if a chosen is in the shop, check if the chosen is a dusk unit
        gold_spent = 0
        dusk_found = False
        while gold_spent < 1000:
            shop = roll(unit_pool, pity_timer)
            gold_spent += 2
            for unit in shop:
                # checks if a chosen is in the shop and resets the unit for the next roll
                if unit.chosen:
                    # checks
                    pity_timer = 0
                    if unit.name in acceptable_chosens:
                        dusk_found = True
                        unit.chosen = False
                        break
                    # not the right chosen unit
                    else:
                        unit.chosen = False
            # no chosen found so increased chance on next roll
            pity_timer += 1
            if dusk_found:
                break
        gold_needed.append(gold_spent)

    # print results
    print("trials: ", num_trials)
    print("acceptable chosens: ", acceptable_chosens)
    print("most gold needed", max(gold_needed))
    print("least gold needed", min(gold_needed))
    print("average gold needed: ", sum(gold_needed)/len(gold_needed))


if __name__ == "__main__":
    main()
