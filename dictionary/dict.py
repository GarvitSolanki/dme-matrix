import csv

with open('Balloon.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1] for rows in reader}
        # print(mydict)
        


# a__string ="Toffee,\nTransparent,\nTropical Black,\nTropical Henna,\nTurquoise,\nVanilla,\nVintage Blue,\nVintage Lace,\nWalnut,\nWatercolor Burst Multi,\nWatercolor Rose,\nWheat,\nWhite,\nWhite Block,\nWhite Film,\nWhite Grey,\nWhite Versaguard,\nWhite/Gray,\nWhite/Grey,\nWild Flower,\nWine,\nWisteria,\nWonderful,\nWood Berry,\nYellow,\nYellow/Red/Green,\nZebra,\n\nToffee,\nTransparent,\nTropical Black,\nTropical Henna,\nTurquoise,\nVanilla,\nVintage Blue,\nVintage Lace,\nWalnut,\nWatercolor Burst Multi,\nWatercolor Rose,\nWheat,\nWhite,\nWhite Block,\nWhite Film,\nWhite Grey,\nWhite Versaguard,\nWhite/Gray,\nWhite/Grey,\nWild Flower,\nWine,\nWisteria,\nWonderful,\nWood Berry,\nYellow,\nYellow/Red/Green,\nZebra,\n\nToffee,\nTransparent,\nTropical Black,\nTropical Henna,\nTurquoise,\nVanilla,\nVintage Blue,\nVintage Lace,\nWalnut,\nWatercolor Burst Multi,\nWatercolor Rose,\nWheat,\nWhite,\nWhite Block,\nWhite Film,\nWhite Grey,\nWhite Versaguard,\nWhite/Gray,\nWhite/Grey,\nWild Flower,\nWine,\nWisteria,\nWonderful,\nWood Berry,\nYellow,\nYellow/Red/Green,\nZebra,\n\n"
# a__string.replace("\n", "")
# print(a__string.strip())