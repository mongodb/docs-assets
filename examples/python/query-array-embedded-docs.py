# Tabbed Examples: Staged POC (the examples differ because we just needed something)
# https://docs-mongodbcom-staging.corp.mongodb.com/jdestefano/DOCSP-364/tutorial/insert-one.html



# 0. Insert documents that we'll query
#
#  db.inventory.insert( [
#    { item: "journal", instock: [ { warehouse: "A", qty: 5 }, { warehouse: "C", qty: 15 } ] },
#    { item: "notebook", instock: [ { warehouse: "C", qty: 5 } ] },
#    { item: "paper", instock: [ { warehouse: "A", qty: 60 }, { warehouse: "B", qty: 15 } ] },
#    { item: "planner", instock: [ { warehouse: "A", qty: 40 }, { warehouse: "B", qty: 5 } ] },
#    { item: "postcard", instock: [ { warehouse: "B", qty: 15 }, { warehouse: "C", qty: 35 } ] }
#  ]);







# 1A. Query for a document in an array
#
# db.inventory.find( { "instock": { warehouse: "A", qty: 5 } } )
#








# 1B. Order matters, so this won't find anything
#
#    db.inventory.find( { "instock": { qty: 5, warehouse: "A" } } )
#








# 2. Query with array index
#
#    db.inventory.find( { 'instock.0.qty': { $lte: 20 } } )





# 3. Use operator to find element
#
#    db.inventory.find( { 'instock.qty': { $lte: 20 } } )







# 4. $elemMatch 1
#
#   db.inventory.find( { "instock": { $elemMatch: { qty: 5, warehouse: "A" } } } )







# 5. $elemMatch 2
#
#    db.inventory.find( { "instock": { $elemMatch: { qty: { $gt: 10, $lte: 20 } } } } )
#








# 6A. Compound but not elemMatch
#
#    db.inventory.find( { "instock.qty": { $gt: 10,  $lte: 20 } } )
#







# 6B. Compound but not elemMatch
#
#    db.inventory.find( { "instock.qty": 5, "instock.warehouse": "A" } )
#






