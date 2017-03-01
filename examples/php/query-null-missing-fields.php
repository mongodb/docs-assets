// Tabbed Examples: Staged POC (the examples differ because we just needed something)
// https://docs-mongodbcom-staging.corp.mongodb.com/jdestefano/DOCSP-364/tutorial/insert-one.html



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


