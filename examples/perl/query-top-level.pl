# Tabbed Examples: Staged POC (the examples differ because we just needed something)
# https://docs-mongodbcom-staging.corp.mongodb.com/jdestefano/DOCSP-364/tutorial/insert-one.html


# **Action Requested**
# 
# Please provide equivalent examples in your driver language.
# 
# - If the examples are not relevant for your driver, omit but leave comment as to why,
# such as "key order is not guaranteed, however, you can enforce absolute key order via :some link: or something.
# This way we can display that instead.
# 
# - Include any additional comments that would be relevant for people using the driver for that example
# 



# 6
# db.inventory.insertMany([
#   { item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
#   { item: "notebook", qty: 50, size: { h: 8.5, w: 11, uom: "in" }, status: "A" },
#   { item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" },
#   { item: "planner", qty: 75, size: { h: 22.85, w: 30, uom: "cm" }, status: "D" },
#   { item: "postcard", qty: 45, size: { h: 10, w: 15.25, uom: "cm" }, status: "A" } ]);





# 7
# db.inventory.find( {} )




# 8
# db.inventory.find()



# 9
# db.inventory.find( { status: "D" } )




# 10
# db.inventory.find( { status: { $in: [ "A", "D" ] } } )




# 11
# db.inventory.find( { status: "A", qty: { $lt: 30 } } )




# 12
# db.inventory.find( { $or: [ { status: "A" }, { qty: { $lt: 30 } } ] } )





# 13
# db.inventory.find( { status: "A", $or: [ { qty: { $lt: 30 } }, { item: /^p/ } ] } )






