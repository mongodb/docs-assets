# Tabbed Examples: Staged POC (the examples differ because we just needed something)
# https://docs-mongodbcom-staging.corp.mongodb.com/jdestefano/DOCSP-364/tutorial/insert-one.html



# 0. Insert documents to update in the examples
# db.inventory.insert( [
#     { item: "canvas", qty: 100, size: { h: 28, w: 35.5, uom: "cm" }, status: "A" },
#     { item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
#     { item: "mat", qty: 85, size: { h: 27.9, w: 35.5, uom: "cm" }, status: "A" },
#     { item: "mousepad", qty: 25, size: { h: 19, w: 22.85, uom: "cm" }, status: "P" },
#     { item: "notebook", qty: 50, size: { h: 8.5, w: 11, uom: "in" }, status: "P" },
#     { item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" },
#     { item: "planner", qty: 75, size: { h: 22.85, w: 30, uom: "cm" }, status: "D" },
#     { item: "postcard", qty: 45, size: { h: 10, w: 15.25, uom: "cm" }, status: "A" },
#     { item: "sketchbook", qty: 80, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
#     { item: "sketch pad", qty: 95, size: { h: 22.85, w: 30.5, uom: "cm" }, status: "A" }
# ]);








# 1. Update One
# db.inventory.updateOne(
#     { item: "paper" },
#     {
#         $set: { "size.uom": "cm", status: "P" },
#         $currentDate: { lastModified: true }
#     }
# )






# 2. Update Many
# db.inventory.updateMany(
#     { "qty": { $lt: 50 } },
#     {
#         $set: { "size.uom": "in", status: "P" },
#         $currentDate: { lastModified: true }
#     }
# )







# 3. Update (single)
#
# db.inventory.update(
#     { "status": "P" } ,
#     {
#         $set: { status: "D" },
#         $currentDate: { lastModified: true }
#     }
# )








# 4. Update (multi)
#
# db.inventory.update(
#    { "status": "P" },
#    {
#      $set: { status: "D" },
#      $currentDate: { lastModified: true }
#    },
#    { multi: true }
# )







# 5. Replace
# db.inventory.replaceOne(
#     { item: "paper" },
#     { item: "paper", instock: [ { warehouse: "A", qty: 60 }, { warehouse: "B", qty: 40 } ] }
# )







# 6. Replace via update
# db.inventory.update(
#     { item: "postcard" },
#     { item: "postcard", instock: [ { warehouse: "B", qty: 15 }, { warehouse: "C", qty: 35 } ] }
# )






