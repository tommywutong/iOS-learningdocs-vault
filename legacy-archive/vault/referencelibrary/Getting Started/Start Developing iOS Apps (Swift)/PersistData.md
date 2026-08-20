---
title: Start Developing iOS Apps (Swift)
apple_id: TP40015214
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2016-12-08'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/DevelopiOSAppsSwift/PersistData.html
archived_at: '2026-07-27T06:57:10.148966Z'
---
> 导航：[总目录](../../../README.md) · [referencelibrary](../../../_indexes/referencelibrary.md) · [Start Developing iOS Apps (Swift)](index.md)


[Next](Resources.md)[Previous](ImplementEditAndDeleteBehavior.md)

## Persist Data

In this lesson, you save a meal list across FoodTracker app sessions. Understanding and implementing data persistence is a vital part of iOS app development. iOS has many persistent data storage solutions; in this lesson, you’ll use `NSCoding` as the data persistence mechanism in the FoodTracker app. `NSCoding` is a protocol that enables a lightweight solution for archiving objects and other structures. Archived objects can be stored on disk and retrieved at a later time.

### Learning Objectives

At the end of the lesson, you’ll be able to:

- Create a structure to store string constants
- Understand the difference between static properties and instance properties
- Use the `NSCoding` protocol to read and write data

### Save and Load the Meal

In this step you’ll implement the behavior in the `Meal` class to save and load the meal. Using the `NSCoding` approach, the `Meal` class is in charge of storing and loading each of its [properties](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjy). It needs to save its data by assigning the value of each property to a particular key. It then loads the data by looking up the information associated with that key.

A key is simply a string value. You choose your own keys based on what makes the most sense in your app. For example, you might use the key `name` to store the value of the `name` property.

To make it clear which coding key corresponds to each piece of data, create a [structure](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjt) to store the key strings. This way, when you need to use the key in multiple places throughout your code, you can use the [constant](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomzt) instead of retyping the string (which increases the likelihood of mistakes).

__To implement a coding key structure__

1. Open `Meal.swift`.
2. In `Meal.swift`, below the `//MARK: Properties` section, add this structure:

   1. `//MARK: Types`
   3. `struct PropertyKey {`
   4. `}`
3. In the `PropertyKey` structure, add these properties:

   1. `static let name = "name"`
   2. `static let photo = "photo"`
   3. `static let rating = "rating"`

   Each constant corresponds to one of the three properties of `Meal`. The `static` keyword indicates that these constants belong to the structure itself, not to instances of the structure. You access these constants using the structure’s name (for example, `PropertyKey.name`).

Your `PropertyKey` structure should look like this:

1. `struct PropertyKey {`
2. `static let name = "name"`
3. `static let photo = "photo"`
4. `static let rating = "rating"`
5. `}`

To be able to encode and decode itself and its properties, the `Meal` class needs to [conform to](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomzs) the `NSCoding` [protocol](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjz). To conform to `NSCoding`, the `Meal` needs to [subclass](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomju) `NSObject`. `NSObject` is considered a [base class](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonzz) that defines a basic interface to the [runtime](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvoobr) system.

__To subclass NSObject and conform to NSCoding__

1. In `Meal.swift`, find the `class` line:

   1. `class Meal {`
2. After `Meal`, add a colon (`:`) and `NSObject` to subclass from the `NSObject` class:

   1. `class Meal: NSObject {`
3. After `NSObject`, add a comma (`,`) and `NSCoding` to adopt the `NSCoding` protocol:

   1. `class Meal: NSObject, NSCoding {`

   Now that `Meal` is a subclass of `NSObject`, the `Meal` class’s initializer must call one of the `NSObject` class’s designated initializers. Because the `NSObject` class’s only initializer is `init()`, the Swift compiler adds the call for you automatically, so you don’t need to change your code; however, feel free to add a call to `super.init()`, if you wish.

   > [!NOTE]
   >
   > For more information on the Swift initialization rules, see Class Inheritance and Initialization and Initialization in _The Swift Programming Language (Swift 3.0.1)_.

The `NSCoding` protocol declares two methods that any class that adopts to it must implement so that instances of that class can be encoded and decoded:

1. `encode(with aCoder: NSCoder)`
2. `init?(coder aDecoder: NSCoder)`

The `encode(with:)` method prepares the class’s information to be archived, and the [initializer](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomq) unarchives the data when the class is created. You need to implement both the `encode(with:)` method and the initializer for the data to save and load properly.

__To implement the encodeWithCoder NSCoding method__

1. In `Meal.swift`, before the last curly brace (`}`), add the following:

   1. `//MARK: NSCoding`

   This is a comment to help you (and anybody else who reads your code) know that the code in this section is related to data persistence.
2. Below the comment, add this method:

   1. `func encode(with aCoder: NSCoder) {`
   2. `}`
3. In the `encode(with:)` method, add the following code:

   1. `aCoder.encode(name, forKey: PropertyKey.name)`
   2. `aCoder.encode(photo, forKey: PropertyKey.photo)`
   3. `aCoder.encode(rating, forKey: PropertyKey.rating)`

   The NSCoder class defines a number of `encode(_:forKey:)` methods, each one taking a different type for the first argument. Each method encodes data of the given type. In the code shown above, the first two lines pass a String argument, while the third line passes an Int. These lines encode the value of each property on the `Meal` class and store them with their corresponding key.

The `encode(with:)` method should look like this:

1. `func encode(with aCoder: NSCoder) {`
2. `aCoder.encode(name, forKey: PropertyKey.name)`
3. `aCoder.encode(photo, forKey: PropertyKey.photo)`
4. `aCoder.encode(rating, forKey: PropertyKey.rating)`
5. `}`

With the encoding method written, implement the initializer to decode the encoded data.

__To implement the initializer to load the meal__

1. At the top of the file, import the unified logging system, just below where you import UIKit.

   1. `import os.log`
2. Below the `encodeWithCoder(_:)` method, add the following initializer:

   1. `required convenience init?(coder aDecoder: NSCoder) {`
   2. `}`

   The `required` modifier means this initializer must be implemented on every subclass, if the subclass defines its own initializers.

   The `convenience` modifier means that this is a secondary initializer, and that it must call a designated initializer from the same class.

   The question mark (`?`) means that this is a [failable initializer](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomzz) that might return [nil](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvoni).
3. Add the following code inside the initializer:

   1. `// The name is required. If we cannot decode a name string, the initializer should fail.`
   2. `guard let name = aDecoder.decodeObject(forKey: PropertyKey.name) as? String else {`
   3. `os_log("Unable to decode the name for a Meal object.", log: OSLog.default, type: .debug)`
   4. `return nil`
   5. `}`

   The `decodeObject(forKey:)` method decodes encoded information.

   The return value of `decodeObjectForKey(_:)` is an `Any?` optional. The guard statement both unwraps the optional and downcasts the enclosed type to a `String`, before assigning it to the `name` constant. If either of these operations fail, the entire initializer fails.
4. Below the previous code, add the following:

   1. `// Because photo is an optional property of Meal, just use conditional cast.`
   2. `let photo = aDecoder.decodeObjectForKey(PropertyKey.photo) as? UIImage`

   You downcast the value returned by `decodeObject(forKey:)` as a `UIImage`, and assign it to the `photo` constant. If the downcast fails, it assigns `nil` to the photo property. There is no need for a `guard` statement here, because the `photo` property is itself an optional.
5. Below the previous code, add the following:

   1. `let rating = aDecoder.decodeIntegerForKey(PropertyKey.rating)`

   The `decodeIntegerForKey(_:)` method unarchives an integer. Because the return value of `decodeIntegerForKey` is `Int`, there’s no need to downcast the decoded value and there is no optional to unwrap.
6. Add the following code at the end of the implementation:

   1. `// Must call designated initializer.`
   2. `self.init(name: name, photo: photo, rating: rating)`

   As a convenience initializer, this initializer is required to call one of its class’s designated initializers before completing. As the initializer’s [arguments](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonru), you pass in the values of the constants you created while archiving the saved data.

The new `init?(coder:)` initializer should look like this:

1. `required convenience init?(coder aDecoder: NSCoder) {`
3. `// The name is required. If we cannot decode a name string, the initializer should fail.`
4. `guard let name = aDecoder.decodeObject(forKey: PropertyKey.name) as? String else {`
5. `os_log("Unable to decode the name for a Meal object.", log: OSLog.default, type: .debug)`
6. `return nil`
7. `}`
9. `// Because photo is an optional property of Meal, just use conditional cast.`
10. `let photo = aDecoder.decodeObject(forKey: PropertyKey.photo) as? UIImage`
12. `let rating = aDecoder.decodeInteger(forKey: PropertyKey.rating)`
14. `// Must call designated initializer.`
15. `self.init(name: name, photo: photo, rating: rating)`
17. `}`

Next, you need a persistent path on the file system where data will be saved and loaded, so you know where to look for it.

__To create a file path to data__

- In `Meal.swift`, below the `//MARK: Properties` section, add this code:

  1. `//MARK: Archiving Paths`
  3. `static let DocumentsDirectory = FileManager().urls(for: .documentDirectory, in: .userDomainMask).first!`
  4. `static let ArchiveURL = DocumentsDirectory.appendingPathComponent("meals")`

  You mark these constants with the `static` keyword, which means they belong to the class instead of an instance of the class. Outside of the `Meal` class, you’ll access the path using the syntax `Meal.ArchiveURL.path`. There will only ever be one copy of these properties, no matter how many instances of the `Meal` class you create.

  The `DocumentsDirectory` constant uses the file manager’s `urls(for:in:)` method to look up the URL for your app’s documents directory. This is a directory where your app can save data for the user. This method returns an array of URLs, and the first parameter returns an optional containing the first URL in the array. However, as long as the enumerations are correct, the returned array should always contain exactly one match. Therefore, it’s safe to force unwrap the optional.

  After determining the URL for the documents directory, you use this URL to create the URL for your apps data. Here, you create the file URL by appending `meals` to the end of the documents URL.

  > [!NOTE]
  >
  > For more information on interacting with the file system in iOS, see _[File System Programming Guide](../../../documentation/File%20Management/File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_.

_Checkpoint:_ Build your app using Command-B. It should build without issues.

### Save and Load the Meal List

Now that you can save and load an individual meal, you need to save and load the meal list whenever a user adds, edits, or removes a meal.

__To implement the method to save the meal list__

1. Open `MealTableViewController.swift`.
2. In the `//MARK: Private Methods` section, just before the last curly brace (`}`), add the following method:

   1. `private func saveMeals() {`
   2. `}`
3. In the `saveMeals()` method, add the following line of code:

   1. `let isSuccessfulSave = NSKeyedArchiver.archiveRootObject(meals, toFile: Meal.ArchiveURL.path)`

   This method attempts to archive the `meals` array to a specific location, and returns `true` if it’s successful. It uses the constant `Meal.ArchiveURL` that you defined in the `Meal` class to identify where to save the information.

   But how do you quickly test whether the data saved successfully? Log messages to the [console](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvoobw) to indicate the result.
4. Add the following `if` statement:

   1. `if isSuccessfulSave {`
   2. `os_log("Meals successfully saved.", log: OSLog.default, type: .debug)`
   3. `} else {`
   4. `os_log("Failed to save meals...", log: OSLog.default, type: .error)`
   5. `}`

   This logs a debug message to the console if the save succeeds, and an error message to the console if the save fails.

Your `saveMeals()` method should look like this:

1. `private func saveMeals() {`
2. `let isSuccessfulSave = NSKeyedArchiver.archiveRootObject(meals, toFile: Meal.ArchiveURL.path)`
3. `if isSuccessfulSave {`
4. `os_log("Meals successfully saved.", log: OSLog.default, type: .debug)`
5. `} else {`
6. `os_log("Failed to save meals...", log: OSLog.default, type: .error)`
7. `}`
8. `}`

Now, implement a method to load meals.

__To implement the method to load the meal list__

1. In `MealTableViewController.swift`, before the last curly brace (`}`), add the following method:

   1. `private func loadMeals() -> [Meal]? {`
   2. `}`

   This method has a return type of an optional array of Meal objects, meaning that it might return an array of Meal objects or might return nothing (`nil`).
2. In the `loadMeals()` method, add the following line of code:

   1. `return NSKeyedUnarchiver.unarchiveObject(withFile: Meal.ArchiveURL.path) as? [Meal]`

   This method attempts to unarchive the object stored at the path `Meal.ArchiveURL.path` and downcast that object to an array of `Meal` objects. This code uses the `as?` operator so that it can return `nil` if the downcast fails. This failure typically happens because an array has not yet been saved. In this case, the `unarchiveObject(withFile:)` method returns `nil`. The attempt to downcast `nil` to [Meal] also fails, itself returning `nil`.

Your `loadMeals()` method should look like this:

1. `private func loadMeals() -> [Meal]? {`
2. `return NSKeyedUnarchiver.unarchiveObject(withFile: Meal.ArchiveURL.path) as? [Meal]`
3. `}`

With these methods implemented, you need to add code to save and load the list of meals whenever a user adds, removes, or edits a meal.

__To save the meal list when a user adds, removes, or edits a meal__

1. In `MealTableViewController.swift`, find the `unwindToMealList(sender:)` action method:

   1. `@IBAction func unwindToMealList(sender: UIStoryboardSegue) {`
   2. `if let sourceViewController = sender.source as? MealViewController, let meal = sourceViewController.meal {`
   4. `if let selectedIndexPath = tableView.indexPathForSelectedRow {`
   5. `// Update an existing meal.`
   6. `meals[selectedIndexPath.row] = meal`
   7. `tableView.reloadRows(at: [selectedIndexPath], with: .none)`
   8. `}`
   9. `else {`
   10. `// Add a new meal.`
   11. `let newIndexPath = IndexPath(row: meals.count, section: 0)`
   13. `meals.append(meal)`
   14. `tableView.insertRows(at: [newIndexPath], with: .automatic)`
   15. `}`
   16. `}`
   17. `}`
2. Right after the `else` clause, add the following code:

   1. `// Save the meals.`
   2. `saveMeals()`

   This code saves the `meals` array whenever a new one is added or an existing one is updated. Make sure this line of code is inside of the outer `if` statement.
3. In `MealTableViewController.swift`, find the `tableView(_:commit:forRowAt:)` method:

   1. `// Override to support editing the table view.`
   2. `override func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCellEditingStyle, forRowAt indexPath: IndexPath) {`
   3. `if editingStyle == .delete {`
   4. `// Delete the row from the data source`
   5. `meals.remove(at: indexPath.row)`
   6. `tableView.deleteRows(at: [indexPath], with: .fade)`
   7. `} else if editingStyle == .insert {`
   8. `// Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view`
   9. `}`
   10. `}`
4. After the `meals.removeAtIndex(indexPath.row)` line, add the following line of code:

   1. `saveMeals()`

   This code saves the `meals` array whenever a meal is deleted.

Your `unwindToMealList(_:)` action method should look like this:

1. `@IBAction func unwindToMealList(sender: UIStoryboardSegue) {`
2. `if let sourceViewController = sender.source as? MealViewController, let meal = sourceViewController.meal {`
4. `if let selectedIndexPath = tableView.indexPathForSelectedRow {`
5. `// Update an existing meal.`
6. `meals[selectedIndexPath.row] = meal`
7. `tableView.reloadRows(at: [selectedIndexPath], with: .none)`
8. `}`
9. `else {`
10. `// Add a new meal.`
11. `let newIndexPath = IndexPath(row: meals.count, section: 0)`
13. `meals.append(meal)`
14. `tableView.insertRows(at: [newIndexPath], with: .automatic)`
15. `}`
17. `// Save the meals.`
18. `saveMeals()`
19. `}`
20. `}`

And your `tableView(_:commit:forRowAt:)` method should look like this:

1. `// Override to support editing the table view.`
2. `override func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCellEditingStyle, forRowAt indexPath: IndexPath) {`
3. `if editingStyle == .delete {`
4. `// Delete the row from the data source`
5. `meals.remove(at: indexPath.row)`
6. `saveMeals()`
7. `tableView.deleteRows(at: [indexPath], with: .fade)`
8. `} else if editingStyle == .insert {`
9. `// Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view`
10. `}`
11. `}`

Now that meals are saved at the appropriate times, make sure that meals get loaded at the appropriate time. The appropriate place to load the stored data is in the table view’s `viewDidLoad` method.

__To load the meal list at the appropriate time__

1. In `MealTableViewController.swift`, find the `viewDidLoad()` method:

   1. `override func viewDidLoad() {`
   2. `super.viewDidLoad()`
   4. `// Use the edit button item provided by the table view controller.`
   5. `navigationItem.leftBarButtonItem = editButtonItem`
   7. `// Load the sample data.`
   8. `loadSampleMeals()`
   9. `}`
2. After setting up the edit button (`navigationItem.leftBarButtonItem = editButtonItem`), add the following `if` statement:

   1. `// Load any saved meals, otherwise load sample data.`
   2. `if let savedMeals = loadMeals() {`
   3. `meals += savedMeals`
   4. `}`

   If `loadMeals()` successfully returns an array of `Meal` objects, this condition is `true` and the `if` statement gets executed. If `loadMeals()` returns `nil`, there were no meals to load and the `if` statement doesn’t get executed. This code adds any meals that were successfully loaded to the `meals` array.
3. After the if statement, add an `else` clause and move the call to `loadSampleMeals()` inside of it:

   1. `else {`
   2. `// Load the sample data.`
   3. `loadSampleMeals()`
   4. `}`

   This code adds any meals that were loaded to the `meals` array.

Your `viewDidLoad()` method should look like this:

1. `override func viewDidLoad() {`
2. `super.viewDidLoad()`
4. `// Use the edit button item provided by the table view controller.`
5. `navigationItem.leftBarButtonItem = editButtonItem`
7. `// Load any saved meals, otherwise load sample data.`
8. `if let savedMeals = loadMeals() {`
9. `meals += savedMeals`
10. `}`
11. `else {`
12. `// Load the sample data.`
13. `loadSampleMeals()`
14. `}`
15. `}`

_Checkpoint_: Run your app. If you add a few new meals and quit the app, the meals you added will be there next time you open the app.

### Wrapping Up

In this lesson, you added the ability to save and load the app’s data. This lets the data persist across multiple runs. Whenever the app launches, it loads the existing data. When the data is modified, the app saves it. The app can terminate safely without losing any data.

This also completes the app. Congratulations! You now have a fully functional app.

> [!NOTE]
>
> To see the completed sample project for this lesson, download the file and view it in Xcode.
>
> （原归档配图未能恢复：`WWDR_download_icon_withPadding_2x.png`）[Download File](https://developer.apple.com/sample-code/swift/downloads/09_PersistData.zip)

[Implement Edit and Delete Behavior](ImplementEditAndDeleteBehavior.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqojnknltc)

[Where to Go from Here](Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjvfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-12-08](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqojzfvjvomi)

[Next](Resources.md)[Previous](ImplementEditAndDeleteBehavior.md)
