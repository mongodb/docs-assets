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


// 29. Insert documents that we'll query
//
//  db.inventory.insertMany( [
//    { item: "journal", instock: [ { warehouse: "A", qty: 5 }, { warehouse: "C", qty: 15 } ] },
//    { item: "notebook", instock: [ { warehouse: "C", qty: 5 } ] },
//    { item: "paper", instock: [ { warehouse: "A", qty: 60 }, { warehouse: "B", qty: 15 } ] },
//    { item: "planner", instock: [ { warehouse: "A", qty: 40 }, { warehouse: "B", qty: 5 } ] },
//    { item: "postcard", instock: [ { warehouse: "B", qty: 15 }, { warehouse: "C", qty: 35 } ] }
//  ]);







// 30. Query for a document in an array
//
// db.inventory.find( { "instock": { warehouse: "A", qty: 5 } } )
//








// 31. Order matters, so this won't find anything
//
//    db.inventory.find( { "instock": { qty: 5, warehouse: "A" } } )
//








// 32. Query with array index
//
//    db.inventory.find( { 'instock.0.qty': { $lte: 20 } } )





// 33. Use operator to find element
//
//    db.inventory.find( { 'instock.qty': { $lte: 20 } } )







// 34. $elemMatch 1
//
//   db.inventory.find( { "instock": { $elemMatch: { qty: 5, warehouse: "A" } } } )







// 35. $elemMatch 2
//
//    db.inventory.find( { "instock": { $elemMatch: { qty: { $gt: 10, $lte: 20 } } } } )
//








// 36. Compound but not elemMatch
//
//    db.inventory.find( { "instock.qty": { $gt: 10,  $lte: 20 } } )
//







// 37. Compound but not elemMatch
//
//    db.inventory.find( { "instock.qty": 5, "instock.warehouse": "A" } )
//






