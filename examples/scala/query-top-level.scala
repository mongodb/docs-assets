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
//   db.inventory.insertMany([
//      { item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
//      { item: "notebook", qty: 50, size: { h: 8.5, w: 11, uom: "in" }, status: "A" },
//      { item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" },
//      { item: "planner", qty: 75, size: { h: 22.85, w: 30, uom: "cm" }, status: "D" },
//      { item: "postcard", qty: 45, size: { h: 10, w: 15.25, uom: "cm" }, status: "A" }
//   ]);
//







// 1A. Select all documents in collection
//
// db.inventory.find( {} )
//








// 1B. Select all documents in collection
//
//    db.inventory.find()
//








// 2. Specify equality
//
//    db.inventory.find( { status: "D" } )





// 3. In condition
//
//    db.inventory.find( { status: { $in: [ "A", "D" ] } } )








// 4. AND conditions
//
//   db.inventory.find( { status: "A", qty: { $lt: 30 } } )







// 5. OR conditions
//
//    db.inventory.find( { $or: [ { status: "A" }, { qty: { $lt: 30 } } ] } )
//








// 6. AND and OR conditions
//
//     db.inventory.find( {
//        status: "A",
//        $or: [ { qty: { $lt: 30 } }, { item: /^p/ } ]
//   } )
//









