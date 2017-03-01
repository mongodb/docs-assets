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
//   db.inventory.insert([
//      { _id: 1, item: null },
//      { _id: 2 }
//   ])







// Equals null
//
// db.inventory.find( { item: null } )
//








// Check type
//
//    db.inventory.find( { item : { $type: 10 } } )
//








// Check existence
//
//   db.inventory.find( { item : { $exists: false } } )


