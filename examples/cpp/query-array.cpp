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


// 20. Insert documents that we'll query
//
//   db.inventory.insertMany([
//       { item: "journal", qty: 25, tags: ["blank", "red"], dim_cm: [ 14, 21 ] },
//       { item: "notebook", qty: 50, tags: ["red", "blank"], dim_cm: [ 14, 21 ] },
//       { item: "paper", qty: 100, tags: ["red", "blank", "plain"], dim_cm: [ 14, 21 ] },
//       { item: "planner", qty: 75, tags: ["blank", "red"], dim_cm: [ 22.85, 30 ] },
//       { item: "postcard", qty: 45, tags: ["blue"], dim_cm: [ 10, 15.25 ] }
//   ]);







// 21. Match an array
//
// db.inventory.find( { tags: ["red", "blank"] } )
//








// 22. Find array that contains, among other things and regardless of order, specified elements
//
//    db.inventory.find( { tags: { $all: ["red", "blank"] } } )
//








// 23. Query for an element
//
//    db.inventory.find( { tags: "red" } )





// 24. Use operator to find element
//
//    db.inventory.find( { dim_cm: { $gt: 25 } } )







// 25. compound conditions
//
//   db.inventory.find( { dim_cm: { $gt: 15, $lt: 20 } } )







// 26. $elemMatch
//
//    db.inventory.find( { dim_cm: { $elemMatch: { $gt: 22, $lt: 30 } } } )
//








// 27. By array index
//
//     db.inventory.find( { "dim_cm.1": { $gt: 25 } } )
//







// 28. By array length
//
//    db.inventory.find( { "tags": { $size: 3 } } )
//






