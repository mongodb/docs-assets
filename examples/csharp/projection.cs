// Tabbed Examples: Staged POC (the examples differ because we just needed something)
// https://docs-mongodbcom-staging.corp.mongodb.com/jdestefano/DOCSP-364/tutorial/insert-one.html

// **Action Requested**
//
// Please provide equivalent examples in your driver language.
//
// - If the examples are not relevant for your driver, omit but leave comment as to why,
// such as "key order is not guaranteed, however, you can enforce absolute key order via :some link: or something.
// This way we can display that instead.
//
// - Include any additional comments that would be relevant for people using the driver for that example
//


// 0. Insert documents that we'll query
//
//  db.inventory.insert( [
//     { item: "journal", status: "A", size: { h: 14, w: 21, uom: "cm" }, instock: [ { warehouse: "A", qty: 5 } ] },
//     { item: "notebook", status: "A",  size: { h: 8.5, w: 11, uom: "in" }, instock: [ { warehouse: "C", qty: 5 } ] },
//     { item: "paper", status: "D", size: { h: 8.5, w: 11, uom: "in" }, instock: [ { warehouse: "A", qty: 60 } ] },
//     { item: "planner", status: "D", size: { h: 22.85, w: 30, uom: "cm" }, instock: [ { warehouse: "A", qty: 40 } ] },
//     { item: "postcard", status: "A", size: { h: 10, w: 15.25, uom: "cm" }, instock: [ { warehouse: "B", qty: 15 }, { warehouse: "C", qty: 35 } ] }
//  ]);
//







// 1. Return all fields
//
// db.inventory.find( { status: "A" } )
//








// 2. Return specified fields + _id
//
//    db.inventory.find( { status: "A" }, { item: 1, status: 1 } )
//








// 3. Suppress _id
//
//    db.inventory.find( { status: "A" }, { item: 1, status: 1, _id: 0 } )
//




// 4. Return all but the excluded fields
//
//    db.inventory.find( { status: "A" }, { status: 0, instock: 0 } )
//







// 5. Projection on embedded field
//
//   db.inventory.find(
//      { status: "A" },
//      { item: 1, status: 1, "size.uom": 1 }
//   )







// 6. Projection on embedded field (exclude)
//
//    db.inventory.find(
//       { status: "A" },
//       { "size.uom": 0 }
//   )
//








// 7. Project field from  array of documents
//
//     db.inventory.find( { status: "A" }, { item: 1, status: 1, "instock.qty": 1 } )
//






// 8. Use $slice projection operator
//
//    db.inventory.find( { status: "A" }, { name: 1, status: 1, instock: { $slice: -1 } } )
//









