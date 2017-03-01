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


// 1A. Insert One
//
//   db.inventory.insertOne(
//      { item: "canvas", qty: 100, tags: ["cotton"], size: { h: 28, w: 35.5, uom: "cm" } }
//   )
//



// 1B. Query the inserted document
//
//   db.inventory.find( { item: "canvas" } )
//






// 2. Insert Many
//
//   db.inventory.insertMany([
//      { item: "journal", qty: 25, tags: ["blank", "red"], size: { h: 14, w: 21, uom: "cm" } },
//      { item: "mat", qty: 85, tags: ["gray"], size: { h: 27.9, w: 35.5, uom: "cm" } },
//      { item: "mousepad", qty: 25, tags: ["gel", "blue"], size: { h: 19, w: 22.85, uom: "cm" } }
//   ])
//









// 3. Insert single
//
//   db.inventory.insert(
//      { item: "notebook", qty: 50, tags: ["red", "hard cover", "plain"], size: { h: 8.5, w: 11, uom: "in" } }
//   )
//





// 4. Insert array of docs
//
//   db.inventory.insert([
//      { item: "paper", qty: 100, tags: ["red", "blank", "plain"], size: { h: 11.69 , w: 16.53, uom: "in" } },
//      { item: "planner", qty: 75, tags: ["blank", "red"], size: { h: 22.85, w: 30, uom: "cm" } },
//      { item: "postcard", qty: 45, tags: ["blue"], size: { h: 10, w: 15.25, uom: "cm" } }
//   ])
//



