---
title: Start Developing iOS Apps (Swift)
apple_id: TP40015214
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2016-12-08'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/DevelopiOSAppsSwift/ImplementEditAndDeleteBehavior.html
archived_at: '2026-07-27T06:57:10.078692Z'
---
> 导航：[总目录](../../../README.md) · [referencelibrary](../../../_indexes/referencelibrary.md) · [Start Developing iOS Apps (Swift)](index.md)


[Next](PersistData.md)[Previous](ImplementNavigation.md)

## Implement Edit and Delete Behavior

In this lesson, you focus on adding behavior that allows the user to edit and delete meals in the FoodTracker app.

### Learning Objectives

At the end of the lesson, you’ll be able to:

- Differentiate between push and modal navigation
- Dismiss view controllers based on their presentation style
- Use segue identifiers to determine which segue is occurring
- Enable a table view controller’s editing mode.

### Enable Editing of Existing Meals

Currently, the FoodTracker app gives users the ability to add a new meal to a list of meals. In this lesson, you’ll enable the editing of existing meals.

When the user tap on a meal in the list [scene](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonrs), you’ll display that meal in the detail scene. The user can then makes changes to the meal. If they tap the Save button, you’ll update both the meal’s data in the model and its appearance in the meal list. Note that this won’t save the model data. Every time the app launches, it starts over with the initial sample data. Still, the user can modify the data while the app is running.

Start by setting up the segues between meal list items and the meal detail scene.

__To configure the table view cell__

1. If the [assistant editor](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonzw) is open, return to the standard editor by clicking the Standard button.

   （原归档配图未能恢复：`standard_toggle_2x.png`）
2. Open your [storyboard](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvooa), `Main.storyboard`.
3. On the [canvas](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonq), select the table view cell in the meal list (Your Meals) scene.
4. Control-drag from the table view cell to the meal detail scene.

   （原归档配图获取待重试：`IEDB_drag_tabletomealscene_2x.png`）

   A shortcut menu titled Selection Segue appears in the location where the drag ended.

   （原归档配图获取待重试：`IEDB_seguemenu_2x.png`）
5. Choose Show from the Selection Segue menu. This causes the navigation controller to push the meal detail scene onto the navigation controller’s stack.
6. Drag down the [navigation controller](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvoojx) between the meal list scene and the meal detail scene so you can see the new [segue](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonrv).

   （原归档配图获取待重试：`IEDB_drag_navcontroller_2x.png`）

   If you want, you can zoom out using the zoom command at the bottom of the canvas.
7. On the canvas, select the newly added segue (the segue that runs directly from the meal list (Your Meals) scene to the meal detail (New Meal) scene).

   （原归档配图获取待重试：`IEDB_selectsegue_2x.png`）
8. In the [Attributes inspector](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjz), type `ShowDetail` in the Identifier field. Press Return.

   （原归档配图获取待重试：`IEDB_inspector_attributes_segue_2x.png`）

   You use the identifier when referring to the segue in code.

When the user taps a row in the meal list, this segue is triggered. The segue pushes the [view controller](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvony) for the meal detail scene onto the [navigation stack](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjt) that contains the meal list scene. The app then animates the transition from the meal list scene to the meal detail scene.

_Checkpoint:_ Run your app. Tap on a meal from the meal list. The app navigates to the meal detail scene. Note: Unlike when you pushed a scene onto the navigation stack in the last lesson, the system does not automatically provide a back button. This is because you added your own bar button to the left side of the navigation bar.

（原归档配图获取待重试：`IEDB_firstcheckpoint_2x.png`）

Creating new meals and editing existing meals are very similar operations. Therefore, you’ll use the same interface to perform both tasks. Of course, you’ll need to make some modifications both to the scene’s appearance and its behavior. You need a way to identify when the user is adding a new meal and when they are editing an existing one.

Recall from earlier that the `prepare(for:sender:)` method is called before any segue gets executed. You can use this method to identify which segue is occurring, and display the appropriate information in the meal detail scene. You’ll differentiate the segues based on the identifiers you assign to them: `AddItem` when adding new meals and `ShowDetail` when editing an existing meal.

__To identify which segue is occurring__

1. Open `MealTableViewController.swift`.
2. At the top of the file, immediately following the import of UIKit, import the unified logging system.

   1. `import os.log`
3. In `MealTableViewController.swift`, find and uncomment the `prepareForSegue(_:sender:)` method. (To uncomment the method, remove the `/*` and `*/` characters surrounding it.)

   After you do that, the template implementation looks like this:

   1. `//MARK: - Navigation`
   3. `// In a storyboard-based application, you will often want to do a little preparation before navigation`
   4. `override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {`
   6. `// Get the new view controller using segue.destinationViewController.`
   7. `// Pass the selected object to the new view controller.`
   8. `}`

   Because `MealTableViewController` is a subclass of `UITableViewController`, the template implementation comes with a skeleton for `prepare(for:sender:)`.
4. Delete the two lines of [comments](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomzr), and replace them with a call to the superclass’s implementation.

   1. `super.prepare(for: segue, sender: sender)`
5. After the call to `super.prepare(for:sender:)`, add this `switch` statement:

   1. `switch(segue.identifier ?? "") {`
   3. `}`

   A `switch` statement considers a value and compares it against several possible matching patterns. It then executes an appropriate block of code, based on the first pattern that matches successfully. Use `switch` statements instead of `if` statements when selecting between multiple options.

   The code above examines the segue’s identifier. If the identifier is `nil`, the nil-coalescing operator (`??`) replaces it with an empty string (`""`). This simplifies the switch statement’s logic, since you won’t need to deal with optionals inside the cases.
6. Add the `AddItem` case to the switch.

   1. `case "AddItem":`
   2. `os_log("Adding a new meal.", log: OSLog.default, type: .debug)`

   If the user is adding an item to the meal list, you don’t need to change the meal detail scene’s appearance. Just log a simple debug message to the console. This will help you track the app’s flow if you have to debug your code.
7. Add the `ShowDetail` case to the switch.

   1. `case "ShowDetail":`
   2. `guard let mealDetailViewController = segue.destination as? MealViewController else {`
   3. `fatalError("Unexpected destination: \(segue.destination)")`
   4. `}`
   6. `guard let selectedMealCell = sender as? MealTableViewCell else {`
   7. `fatalError("Unexpected sender: \(sender)")`
   8. `}`
   10. `guard let indexPath = tableView.indexPath(for: selectedMealCell) else {`
   11. `fatalError("The selected cell is not being displayed by the table")`
   12. `}`
   14. `let selectedMeal = meals[indexPath.row]`
   15. `mealDetailViewController.meal = selectedMeal`

   If you are editing an existing meal, you need to display the meal’s data in the meal detail scene. This code starts by getting the destination view controller, the selected meal cell, and the index path of the selected cell. The guard statements check that all the downcasts work as expected, and all optionals contain non-`nil` values. Here, the guard statements simply act as a sanity check. If your storyboard is set up correctly, none of these `guard` statements will fail.

   As soon as you have the index path, you can look up the meal object for that path and pass it to the destination view controller.
8. Add the default case.

   1. `default:`
   2. `fatalError("Unexpected Segue Identifier; \(segue.identifier)")`

   Again, if your storyboard is set up correctly, the default case never executes. However, if you later add another segue from your Your Meals scene and forget to update the `prepare(for:sender:)` method, the new segue’s identifier won’t match either the `AddItem` or the `ShowDetail` case. In this case, the switch statement prints an error message to the console and terminates the app.

Your `prepare(for:sender:)` method should look something like this:

1. `override func prepare(for segue: UIStoryboardSegue, sender: Any?) {`
3. `super.prepare(for: segue, sender: sender)`
5. `switch(segue.identifier ?? "") {`
7. `case "AddItem":`
8. `os_log("Adding a new meal.", log: OSLog.default, type: .debug)`
10. `case "ShowDetail":`
11. `guard let mealDetailViewController = segue.destination as? MealViewController else {`
12. `fatalError("Unexpected destination: \(segue.destination)")`
13. `}`
15. `guard let selectedMealCell = sender as? MealTableViewCell else {`
16. `fatalError("Unexpected sender: \(sender)")`
17. `}`
19. `guard let indexPath = tableView.indexPath(for: selectedMealCell) else {`
20. `fatalError("The selected cell is not being displayed by the table")`
21. `}`
23. `let selectedMeal = meals[indexPath.row]`
24. `mealDetailViewController.meal = selectedMeal`
26. `default:`
27. `fatalError("Unexpected Segue Identifier; \(segue.identifier)")`
28. `}`
29. `}`

Now that you have the logic implemented, open `MealViewController.swift` and make sure the [user interface (UI)](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjy) updates correctly. Specifically, when an [instance](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvona) of `MealViewController` (the meal detail scene) gets created, its views should be populated with data from its `meal` property, if that data exists. You do this type of setup work is in the `viewDidLoad()` method.

__To update the implementation of viewDidLoad__

1. Open `MealViewController.swift`.
2. In `MealViewController.swift`, find the `viewDidLoad()` method.

   1. `override func viewDidLoad() {`
   2. `super.viewDidLoad()`
   4. `// Handle the text field’s user input through delegate callbacks.`
   5. `nameTextField.delegate = self`
   7. `// Enable the Save button only if the text field has a valid Meal name.`
   8. `updateSaveButtonState()`
   9. `}`
3. Below the `nameTextField.delegate` line, add the following code. If the `meal` property is non-`nil`, this code sets each of the views in `MealViewController` to display data from the `meal` property. The `meal` property will only be non-`nil` when an existing meal is being edited.

   1. `// Set up views if editing an existing Meal.`
   2. `if let meal = meal {`
   3. `navigationItem.title = meal.name`
   4. `nameTextField.text = meal.name`
   5. `photoImageView.image = meal.photo`
   6. `ratingControl.rating = meal.rating`
   7. `}`

Your `viewDidLoad()` method should look something like this:

1. `override func viewDidLoad() {`
2. `super.viewDidLoad()`
4. `// Handle the text field’s user input through delegate callbacks.`
5. `nameTextField.delegate = self`
7. `// Set up views if editing an existing Meal.`
8. `if let meal = meal {`
9. `navigationItem.title = meal.name`
10. `nameTextField.text = meal.name`
11. `photoImageView.image = meal.photo`
12. `ratingControl.rating = meal.rating`
13. `}`
15. `// Enable the Save button only if the text field has a valid Meal name.`
16. `updateSaveButtonState()`
17. `}`

_Checkpoint:_ Run your app. Click a meal from the meal list to navigate to the meal detail scene. The detail scene should be prepopulated with data about the meal. Unfortunately, the Save button does not work yet. If you click Save, the app does not update the meal. Instead, it adds a new meal. You’ll fix that next.

（原归档配图未能恢复：`IEDB_sim_editmeal_2x.png`）

To update an existing meal, you’ll need to modify the `unwindToMealList(sender:)` action method to handle the two different cases: adding a new meal and editing an existing one. Recall that this method is only called when a user taps the Save button, so you don’t need to account for the Cancel button in this method.

__To update the implementation of unwindToMealList(sender:) to both add and edit meals__

1. Open `MealTableViewController.swift`.
2. In `MealTableViewController.swift`, find the `unwindToMealList(sender:)` method.

   1. `@IBAction func unwindToMealList(sender: UIStoryboardSegue) {`
   2. `if let sourceViewController = sender.source as? MealViewController, let meal = sourceViewController.meal {`
   4. `// Add a new meal.`
   5. `let newIndexPath = IndexPath(row: meals.count, section: 0)`
   7. `meals.append(meal)`
   8. `tableView.insertRows(at: [newIndexPath], with: .automatic)`
   9. `}`
   10. `}`
3. At the beginning of the first `if` statement, add this `if` statement:

   1. `if let selectedIndexPath = tableView.indexPathForSelectedRow {`
   2. `}`

   This code checks whether a row in the table view is selected. If it is, that means a user tapped one of the table views cells to edit a meal. In other words, this `if` statement gets executed when you are editing an existing meal.
4. In this `if` statement, add the following code:

   1. `// Update an existing meal.`
   2. `meals[selectedIndexPath.row] = meal`
   3. `tableView.reloadRows(at: [selectedIndexPath], with: .none)`

   The first line updates the `meals` array. It replaces the old `meal` object with the new, edited `meal` object. The second line reloads the appropriate row in the table view. This replaces the current cell with a new cell that contains the updated `meal` data. As a result, when the table view reappears, the row that the user selected now shows the edited meal.
5. After the `if` statement, add an `else` clause and wrap it around the last four lines in the method. Make sure the lines in the `else` clause are indented properly by selecting all of them and pressing Control-I.

   1. `else {`
   2. `// Add a new meal.`
   3. `let newIndexPath = IndexPath(row: meals.count, section: 0)`
   5. `meals.append(meal)`
   6. `tableView.insertRows(at: [newIndexPath], with: .automatic)`
   7. `}`

   The `else` clause executes when there’s no selected row in the table view, which means a user tapped the Add button to get to the meal detail scene. In other words, this `else` statement executes when the user adds a new meal.

Your `unwindToMealList(sender:)` action method should look like this:

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

_Checkpoint:_ Run your app. You should be able to click a table view cell to navigate to the meal detail scene, and see it prepopulated with data about the meal. If you click Save, the changes you made should be displayed in the meal list.

（原归档配图获取待重试：`IEDB_sim_overwritemeal_2x.png`）

### Cancel an Edit to an Existing Meal

A user might decide not to keep edits to a meal, and want to return to the meal list without saving any changes. For this, you’ll update the behavior of the Cancel button to dismiss the scene appropriately.

The type of dismissal depends on how the scene was presented. You’ll implement a check that determines how the current scene was presented when the user taps the Cancel button. If it was presented modally (the user tapped the Add button), it’ll be dismissed using `dismissViewControllerAnimated(_:completion:)`. If it was presented with push navigation (the user tapped a table view cell), it will be dismissed by the navigation controller that presented it.

> [!NOTE]
>
> Different presentation styles have different uses. Present scenes modally when they represent a task that the user must either complete or cancel before continuing (for example, adding a new meal). Present scenes using a navigation controller when the user is navigating through hierarchical data (for example, selecting a meal from a list of meals).
>
> For more information, see Interaction > Modality and Interaction > Navigation in _iOS Human Interface Guidelines_.

__To change the implementation of the cancel action__

1. Open `MealViewController.swift`.
2. In `MealViewController.swift`, find the `cancel(_:)` action method.

   1. `@IBAction func cancel(_ sender: UIBarButtonItem) {`
   2. `dismiss(animated: true, completion: nil)`
   3. `}`

   This implementation is only using the `dismiss(animated:completion:)` method to dismiss the meal detail scene because you’ve only had to account for the Add button so far.
3. In the `cancel(_:)` action method, before the existing line of code, add the following code:

   1. `// Depending on style of presentation (modal or push presentation), this view controller needs to be dismissed in two different ways.`
   2. `let isPresentingInAddMealMode = presentingViewController is UINavigationController`

   This code creates a Boolean value that indicates whether the view controller that presented this scene is of type `UINavigationController`. As the constant name `isPresentingInAddMealMode` indicates, this means that the meal detail scene is presented by the user tapping the Add button. This is because the meal detail scene is embedded in its own navigation controller when it’s presented in this manner, which means that the navigation controller is what presents it.
4. After the line you just added, add the following `if` statement, and move the line that calls `dismissViewControllerAnimated` inside of it:

   1. `if isPresentingInAddMealMode {`
   2. `dismiss(animated: true, completion: nil)`
   3. `}`

   Before you always called the `dismiss(animated:completion:)` method when the user tapped the Cancel button; however, `dismiss(animated:completion:)` only works when the user is adding a new meal. Therefore, the code now checks to make sure the user was adding a new meal before calling `dismiss(animated:completion:)`.

   Note that this still does not dismiss the scene when the user is editing a meal. You’ll add that code next.
5. Right after the `if` statement, add this `else` clause:

   1. `else if let owningNavigationController = navigationController{`
   2. `owningNavigationController.popViewController(animated: true)`
   3. `}`

   The `else` block is called if the user is editing an existing meal. This also means that the meal detail scene was pushed onto a navigation stack when the user selected a meal from the meal list. The `else` statement uses an `if let` statement to safely unwrap the view controller’s `navigationController` property. If the view controller has been pushed onto a navigation stack, this property contains a reference to the stack’s navigation controller.

   The code within the `else` clause executes a method called `popViewController(animated:)`, which pops the current view controller (the meal detail scene) off the navigation stack and animates the transition. This dismisses the meal detail scene, and returns the user to the meal list.
6. Add a second else statement immediately below the first:

   1. `else {`
   2. `fatalError("The MealViewController is not inside a navigation controller.")`
   3. `}`

   This `else` case executes only if the meal detail scene was not presented inside a modal navigation controller (for example, when adding a new meal), and if the meal detail scene was not pushed onto a navigation stack (for example, when editing a meal). If your app’s navigation flow is set up properly, this `else` case should never execute. If it does, it indicates a bug in your app. The else case prints an error message to the console and terminates the app.

Your `cancel(_:)` action method should look like this:

1. `@IBAction func cancel(_ sender: UIBarButtonItem) {`
2. `// Depending on style of presentation (modal or push presentation), this view controller needs to be dismissed in two different ways.`
3. `let isPresentingInAddMealMode = presentingViewController is UINavigationController`
5. `if isPresentingInAddMealMode {`
6. `dismiss(animated: true, completion: nil)`
7. `}`
8. `else if let owningNavigationController = navigationController{`
9. `owningNavigationController.popViewController(animated: true)`
10. `}`
11. `else {`
12. `fatalError("The MealViewController is not inside a navigation controller.")`
13. `}`
14. `}`

_Checkpoint:_ Run your app. When you select a meal, you can click Cancel to return to the meal list without saving any changes to the meal. Additionally, when you click the Add button (`+`) and click Cancel instead of Save, the navigation should take you back to the meal list without adding a new meal.

### Support Deleting Meals

Next, you’ll give users the ability to delete a meal from the meal list. You need a way to let users put the table view into an editing mode from which they can delete cells. You accomplish this by adding an Edit button to the table view’s navigation bar.

__To add an Edit button to the table view__

1. Open `MealTableViewController.swift`.
2. In `MealTableViewController.swift`, find the `viewDidLoad()` method.

   1. `override func viewDidLoad() {`
   2. `super.viewDidLoad()`
   4. `// Load the sample data.`
   5. `loadSampleMeals()`
   6. `}`
3. Below the `super.viewDidLoad()` line, add the following line of code:

   1. `// Use the edit button item provided by the table view controller.`
   2. `navigationItem.leftBarButtonItem = editButtonItem`

   This code creates a special type of bar button item that has editing behavior built into it. It then adds this button to the left side of the navigation bar in the meal list scene.

Your `viewDidLoad()` method should look something like this:

1. `override func viewDidLoad() {`
2. `super.viewDidLoad()`
4. `// Use the edit button item provided by the table view controller.`
5. `navigationItem.leftBarButtonItem = editButtonItem`
7. `// Load the sample data.`
8. `loadSampleMeals()`
9. `}`

_Checkpoint:_ Run your app. Notice there’s an Edit button on the left of the table view’s navigation bar. If you click the Edit button, the table view goes into editing mode—but you won’t be able to delete cells yet, because you haven’t implemented that.

（原归档配图获取待重试：`IEDB_sim_editbutton_2x.png`）

To perform any sort of editing on a table view, you need to implement one of its delegate methods, `tableView(_:commit:forRowAt:)`. This delegate method manages changes to the table rows when it’s in editing mode.

Also, uncomment the implementation of `tableView(_:canEditRowAt:)` to support editing.

__To delete a meal__

1. In `MealTableViewController.swift`, find and uncomment the `tableView(_:commit:forRowAt:)` method. (To uncomment the method, remove the `/*` and `*/` characters surrounding it.)

   After you do that, the template implementation looks like this:

   1. `// Override to support editing the table view.`
   2. `override func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCellEditingStyle, forRowAt indexPath: IndexPath) {`
   3. `if editingStyle == .delete {`
   4. `// Delete the row from the data source`
   5. `tableView.deleteRows(at: [indexPath], with: .fade)`
   6. `} else if editingStyle == .insert {`
   7. `// Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view`
   8. `}`
   9. `}`
2. Below the comment that says `// Delete the row from the data source`, add:

   1. `meals.remove(at: indexPath.row)`

   This code removes the `Meal` object to be deleted from `meals`. The line after it, which is part of the template implementation, deletes the corresponding row from the table view.
3. In `MealTableViewController.swift`, find and uncomment the `tableView(_:canEditRowAt:)` method.

   After you do that, the template implementation looks like this:

   1. `// Override to support conditional editing of the table view.`
   2. `override func tableView(_ tableView: UITableView, canEditRowAt indexPath: IndexPath) -> Bool {`
   3. `// Return false if you do not want the specified item to be editable.`
   4. `return true`
   5. `}`

Your `tableView(_:commitEditingStyle:forRowAtIndexPath:)` method should look like this:

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

_Checkpoint:_ Run your app. If you click the Edit button, the table view goes into editing mode. You can choose a cell to delete by clicking the indicator on the left, and confirm that you want to delete it by pressing the Delete button in that cell. Alternatively, swipe left on a cell to expose the Delete button quickly; this behavior is built into table views. When you click the Delete button for a cell, the cell is removed from the list.

（原归档配图获取待重试：`IEDB_sim_deletebehavior_2x.png`）
> [!NOTE]
>
> When in editing mode, the rating control extends over the delete button. This is because the cell’s layout was not designed using Auto Layout. The controls fit in the normal allotted space, but the control doesn’t adapt when the space is reduced.
>
> To fix this, you need to lay out the cell using nested stack views and Auto Layout constraints; however, that is left as an exercise for the reader.
>
> For more information, see _[Auto Layout Guide](../../../documentation/User%20Experience/Auto%20Layout%20Guide/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjt)_.

### Wrapping Up

In this lesson, you added support to edit and delete meals from the meal list. Because editing a meal and creating a new meal are very similar, the app uses the meal detail scene for both. As a result, you need to distinguish between when you are presenting the view controller modally (adding a meal) and pushing the view controller onto the navigation stack (editing a meal). You modified both the meal detail scene’s appearance and its behaviors based on how it was presented.

You can now add, edit, and delete meals. However, the data is not saved. Every time you launch the app, you start over with the initial sample data. In the next lesson, you’ll add code to save and load the meal list.

> [!NOTE]
>
> To see the completed sample project for this lesson, download the file and view it in Xcode.
>
> （原归档配图未能恢复：`WWDR_download_icon_withPadding_2x.png`）[Download File](https://developer.apple.com/sample-code/swift/downloads/08_ImplementEditAndDeleteBehavior.zip)

[Implement Navigation](ImplementNavigation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjwfvjvomi)

[Persist Data](PersistData.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjufvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-12-08](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqojzfvjvomi)

[Next](PersistData.md)[Previous](ImplementNavigation.md)
