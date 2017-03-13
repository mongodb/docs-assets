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


# 0. Insert documents to update in the examples
# db.inventory.insertMany( [
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











# 5. Replace
# db.inventory.replaceOne(
#     { item: "paper" },
#     { item: "paper", instock: [ { warehouse: "A", qty: 60 }, { warehouse: "B", qty: 40 } ] }
# )








