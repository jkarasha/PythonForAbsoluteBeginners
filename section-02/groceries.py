"""
Penne 16 oz Pack of 12 - $16.68
Arrabiata Pasta Sauce 24 oz - $6.98
Bag of 20 Organic Garlic Cloves - $16.78
Italian Seasoning 1.5 oz Bottle - $15.26
Artisan Baguettes Twin Pack - $3.00
12 oz Bag of Meatballs - $4.39
"""
penne = 16.68
pasta_sause = 6.98
garlic = 16.78
seasoning = 15.26
baguettes = 3.00
meatballs = 4.39

sub_total = (penne + pasta_sause + garlic + seasoning + baguettes + meatballs)
tax = sub_total * 0.06
#
total = sub_total + tax
#
print(total)
print(round(total, 2))