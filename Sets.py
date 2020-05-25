##  ALL ABOUT SETS - Set is a collection which is unordered and unindexed. No duplicate members

import operator
import itertools

# SET Constructers
# ----------------

set0 = {}
set1 = set({'books', 'pens', 'pencils'})                           # Construct a SET from a SET
set2 = set(['hallo', 'goodbye', 'morning'])                        # Construct a SET from a LIST
set3 = set(('black', 'white', 'yellow'))                           # Construct a SET from a TUPLE
set4 = set('Good day Mate')                                        # Construct a SET from a STRING
set5 = set({1:'a', 3:'c', 2:'b'})                                  # Construct a SET from a DICTIONARY

xs = {'boatshed', 'launch', 'hook', 'rod', 'sinker', 'starboard', 'anchor', 'marina'}

print('Length of xs is : ', len(xs), ' - ', 'type is : ', type(xs))


# Create a copy of a SET
# ----------------------

set6 = set3.copy()

# difference - returns values of 1st SET where it differs from 2nd SET
# --------------------------------------------------------------------

set7 = {'a', 'd', 's', 'v', 'z'}
set8 = {'a', 's', 't', 'z', 'e'}
set9 = set7.difference(set8)

# difference_update - Update 1st SET with differences from 2nd SET
# ----------------------------------------------------------------

set7.difference_update(set8)

# intersection - Returns values of 1st SET where it corresponds with values of 2nd SET
# ------------------------------------------------------------------------------------

set10 = {'aaa', 'fff', 'rrr', 'ggg', 'www'}
set11 = {'www', 'ttt', 'bbb', 'aaa'}

set12 = set10.intersection(set11)

# intersection_update - Update 1st SET with values that corresponds with values of 2nd SET
# ----------------------------------------------------------------------------------------

set10.intersection_update(set11)

# isdisjoint - Returns True if no values corresponds else returns False
# ---------------------------------------------------------------------

set13 = {1, 4, 15, 7, 10, 3}
set14 = {12, 1, 19, 10, 8, 21}

ind = set13.isdisjoint(set14)

# issubset - Returns True if all items in 1st SET are present in 2nd SET else False
# ---------------------------------------------------------------------------------

set15 = {'bus', 'car', 'ship'}
set16 = {'tank', 'ute', 'bus', 'train', 'ship', 'plane', 'car'}

print('set15 is a subset of set16 - ', set15.issubset(set16))

# issuperset - Returns True if all items in 2nd SET are present in 1st SET else False
# -----------------------------------------------------------------------------------

set17 = {'bus', 'car', 'ship', 'tank', 'plane', 'train', 'ute'}
set18 = {'tank', 'ute', 'bus', 'train'}

print('set17 is a superset of set18 - ', set17.issuperset(set18))

# symmetric_difference - Returns all items from bots SETS where the SETS are differing
# ------------------------------------------------------------------------------------

set19 = {'bus', 'car', 'ship', 'tank', 'plane', 'train', 'ute'}
set20 = {'tank', 'ute', 'bus', 'train'}

set21 = set19.symmetric_difference(set20)

# symmetric_difference_update - update 1st SET with items where the SETS are differing
# ------------------------------------------------------------------------------------

set22 = {'car', 'ship', 'tank', 'plane', 'train', 'ute'}
set23 = {'tank', 'ute', 'bus', 'train'}
set22.symmetric_difference_update(set23)

# SET Iterations
# --------------

for i in xs:                                                        # Iterate through a SET
    print(i, end=',  ')
print()
print('launch' in xs)                                               # Result = True

# ADD Item(s) to SETS
# -------------------

xs.add("sailboat")                                                  # Add 1 item to the SET
xs.update(['Engine', 'lures', 'bait'])                              # Add more that 1 item to the SET
print(xs)

# SORTING SETS in 3 ways
# ----------------------

print('sorted ss with normal sort = ', sorted(xs))
cs = sorted(xs, key=lambda x: x[0])
print('sorted cs with lambda key = ', cs)
xs = sorted(xs, key=operator.itemgetter(0))
print('sorted xs with operator.itemgetter = ', xs)

# Join 2 SETS
# -----------
xs2 = {'towing', 'trucking', 'racing'}
xs3 = {'boating', 'fishing', 'skiing'}

xs2.update(xs3)
print('xs2 = ', xs2)
xs4 = xs2.union(xs)
print('xs4 is :', xs4)

# Remove item from a SET
# ----------------------

xs.remove('bait')                                                   # Remove item asked for in SET
set1.discard('books')                                               # Discard item asked for in SET
xs.pop()                                                            # Remove last item in SET

# Clear all items from a SET
# --------------------------

xs.clear()

# Delete the SET
# --------------

del xs

# SETS don't allow duplicates
# ---------------------------

r = {1, 4, 6, 6, 6, 7, 8, 1, 19, 4, 5, 10}
print('r sorted witk duplicates eliminated = ', sorted(r))

