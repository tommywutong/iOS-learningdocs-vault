---
title: Start Developing iOS Apps (Swift)
apple_id: TP40015214
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2016-12-08'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/DevelopiOSAppsSwift/ImplementNavigation.html
archived_at: '2026-07-27T06:57:10.006158Z'
---
> 导航：[总目录](../../../README.md) · [referencelibrary](../../../_indexes/referencelibrary.md) · [Start Developing iOS Apps (Swift)](index.md)


[Next](ImplementEditAndDeleteBehavior.md)[Previous](CreateATableView.md)

## Implement Navigation

In this lesson, you use navigation controllers and segues to create the navigation flow of the FoodTracker app. At the end of the lesson, you’ll have a complete navigation scheme and interaction flow for the app.

（原归档配图未能恢复：`IN_sim_navbar_2x.png`）

### Learning Objectives

At the end of the lesson, you’ll be able to:

- Embed an existing view controller within a navigation controller in a storyboard
- Create segues between view controllers
- Edit the attributes of a segue in a storyboard using the Attributes inspector
- Pass data between view controllers using the `prepare(for:sender:)` method
- Perform an unwind segue
- Use stack views to create robust, flexible layouts

### Add a Segue to Navigate Forward

With data displaying as expected, it’s time to provide a way to navigate from the initial meal list [scene](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonrs) to the meal detail scene. Transitions between scenes are called [segues](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonrv).

Before creating a segue, you need to configure your scenes. First, you’ll put your table view controller inside of a navigation controller. A [navigation controller](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvoojx) manages transitions backward and forward through a series of [view controllers](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvony). The set of view controllers managed by a particular navigation controller is called its [navigation stack](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjt). The first item added to the stack becomes the [root view controller](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjrgi) and is never popped off (removed from) the navigation stack.

__To add a navigation controller to your meal list scene__

1. Open your [storyboard](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvooa), `Main.storyboard`.
2. Select the meal list scene by clicking on its [scene dock](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonrt).

   （原归档配图未能恢复：`CTV_scenedock_table_2x.png`）
3. Choose Editor > Embed In > Navigation Controller.

   Xcode adds a new navigation controller to your storyboard, sets the storyboard entry point to it, and assigns the meal list scene as its root view controller.

（原归档配图获取待重试：`IN_navcontrolleradded_2x.png`）

On the [canvas](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonq), the icon connecting the controllers is the root view controller relationship. The table view controller is the navigation controller’s root view controller. The [storyboard entry point](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonrw) is set to the navigation controller because the navigation controller is now a container for the table view controller.

You might notice that your table view has a bar on top of it now. This is a navigation bar. Every controller on the navigation stack gets a navigation bar, which can contain controls for backward and forward navigation. Next, you’ll add a button to this navigation bar to transition to the meal detail scene.

_Checkpoint:_ Run your app. Above your table view you should now see extra space. This is the navigation bar provided by the navigation controller. The navigation bar extends its background to the top of the status bar, so the status bar doesn’t overlap with your content anymore.

（原归档配图未能恢复：`IN_sim_emptynavbar_2x.png`）

### Configure the Navigation Bar for the Scenes

Now, you’ll add the meal list title and a button (to add additional meals) to the navigation bar. Navigation bars get their title from the view controller at the top of the navigation stack—they don’t have a title themselves. Each view controller has a `navigationItem` property. This property defines the navigation bar’s appearance for that view controller.

In Interface Builder, you can configure a view controller’s navigation item by editing the navigation bar in the view controller’s scene.

__To configure the navigation bar in the meal list__

1. Double-click the navigation bar in the meal list scene.

   （原归档配图获取待重试：`IN_rename_meallist_2x.png`）

   A cursor appears in a text field, letting you enter text.
2. Type `Your Meals` and press Return. This sets the title for the table view controller’s navigation item.

   （原归档配图获取待重试：`IN_meallist_newname_2x.png`）
3. Open the [Object library](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonju). (Choose View > Utilities > Show Object Library.)
4. In the Object library, find a Bar Button Item object.
5. Drag a Bar Button Item object from the list to the far right of the navigation bar in the meal list scene.

   A button called Item appears where you dragged the bar button item.

   （原归档配图获取待重试：`IN_meallist_barbutton_2x.png`）
6. Select the bar button item and open the [Attributes inspector](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjz) （原归档配图未能恢复：`inspector_attributes_2x.png`）.
7. In the Attributes inspector, choose Add from the pop-up menu next to the System Item option.

   The button changes to an Add button (`+`).

   （原归档配图未能恢复：`IN_meallist_addbutton_2x.png`）

_Checkpoint:_ Run your app. The navigation bar should now have a title and display an Add button (`+`). The button doesn’t do anything yet. You’ll fix that next.

（原归档配图未能恢复：`IN_sim_navbar_2x.png`）

You want the Add button (`+`) to bring up the meal detail scene, so you’ll do this by having the button trigger a segue (or transition) to that scene.

__To configure the Add button in the meal detail scene__

1. On the canvas, select the Add button (`+`).
2. Control-drag from the button to the meal detail scene.

   （原归档配图获取待重试：`IN_addbutton_drag_2x.png`）

   A shortcut menu titled Action Segue appears in the location where the drag ended.

   （原归档配图获取待重试：`IN_addbutton_segue_2x.png`）

   The Action Segue menu allows you to choose the type of segue used to transition from the meal list scene to the meal detail scene when the user taps the Add button.
3. Choose Show from the Action Segue menu.

A [show segue](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjrgm) pushes the selected scene onto the top of the navigation stack, and the navigation controller presents that scene. When you select the show segue, Interface Builder sets up the show segue and alters the meal detail scene’s appearance in the canvas—it is presented with a navigation bar in Interface Builder.

（原归档配图获取待重试：`IN_showsegue_2x.png`）

_Checkpoint:_ Run your app. You can click the Add button and navigate to the meal detail scene from the meal list scene. Because you’re using a navigation controller with a show segue, the backward navigation is handled for you, and a back button automatically appears in the meal detail scene. This means you can click the back button in the meal detail scene to get back to the meal list.

（原归档配图获取待重试：`IN_sim_showsegue_2x.png`）

The push-style navigation you get by using the show segue is working just as it’s supposed to—but it’s not quite what you want when adding items. Push navigation is designed for a drill-down interface, where you’re providing more information about whatever the user selected. Adding an item, on the other hand, is a modal operation—the user performs an action that’s complete and self-contained, and then returns from that scene to the main navigation. The appropriate method of presentation for this type of scene is a [modal segue](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjrgq).

Instead of deleting the existing segue and creating a new one, simply change the segue’s style in the Attributes inspector. As is the case with most selectable elements in a storyboard, you can use the Attributes inspector to edit a segue’s attributes.

__To change the segue style__

1. Select the segue from the meal list scene to the meal detail scene.

   （原归档配图获取待重试：`IN_selectsegue_2x.png`）
2. In the Attributes inspector, choose Present Modally from the Kind field’s pop-up menu.
3. In the Attributes inspector, type `AddItem` in the Identifier field. Press Return.

   Later, you’ll use this identifier to identify the segue.

A modal view controller doesn’t get added to the navigation stack, so it doesn’t get a navigation bar in Interface Builder. However, you want to keep the navigation bar to provide the user with visual continuity. To give the meal detail scene a navigation bar when presented modally, embed it in its own navigation controller.

__To add a navigation controller to the meal detail scene__

1. Select the meal detail scene by clicking on its scene dock.

   （原归档配图未能恢复：`CTV_scenedock_mealscene_2x.png`）
2. With the view controller selected, choose Editor > Embed In > Navigation Controller.

As before, Xcode adds a navigation controller and shows the navigation bar at the top of the meal detail scene.

You may need to update the frames in the meal detail scene, if they don’t update automatically. If you are getting warnings about misplaced views, select the view controller and press the Update Frames button in the bottom right corner of the canvas. This will correct the position of every view in the scene, based on their current constraints.

（原归档配图获取待重试：`IN_navcontroller_mealscene_2x.png`）

Next, configure the navigation bar to add a title to this scene as well as two buttons, Cancel and Save. Later, you’ll link these buttons to [actions](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomrt).

__To configure the navigation bar in the meal detail scene__

1. Double-click the navigation bar in the meal detail scene.

   （原归档配图未能恢复：`IN_rename_mealscene_2x.png`）

   A cursor appears, letting you enter text.
2. Type `New Meal` and press Return to save.
3. Drag a Bar Button Item object from the [Object library](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonju) to the far left of the navigation bar in the meal detail scene.
4. In the Attributes inspector, for System Item, select Cancel.

   The button text changes to Cancel.

   （原归档配图获取待重试：`IN_mealscene_cancelbutton_2x.png`）
5. Drag another Bar Button Item object from the Object library to the far right of the navigation bar in the meal detail scene.
6. In the Attributes inspector, for System Item, select Save.

   The button text changes to Save.

   （原归档配图获取待重试：`IN_mealscene_savebutton_2x.png`）

_Checkpoint:_ Run your app. Click the Add button. You still see the meal detail scene, but there’s no longer a button to navigate back to the meal list—instead, you see the two buttons you added, Cancel and Save. Those buttons aren’t linked to any actions yet, so you can click them, but they don’t do anything. You’ll configure the buttons to save or cancel adding a new meal and to bring the user back to the meal list soon.

（原归档配图获取待重试：`IN_sim_saveandcancel_2x.png`）

### Store New Meals in the Meal List

The next step in creating the FoodTracker app’s functionality is implementing the ability for a user to add a new meal. Specifically, when a user enters a meal name, rating, and photo in the meal detail scene and taps the Save button, you want `MealViewController` to configure a `Meal` object with the appropriate information and pass it back to `MealTableViewController` to display in the meal list.

Start by adding a `Meal` property to `MealViewController`.

__To add a Meal property to MealViewController__

1. Open `MealViewController.swift`.
2. Below the `ratingControl` [outlet](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjv) in `MealViewController.swift`, add the following property:

   1. `/*`
   2. `This value is either passed by `MealTableViewController` in `prepare(for:sender:)``
   3. `or constructed as part of adding a new meal.`
   4. `*/`
   5. `var meal: Meal?`

   This declares a property on `MealViewController` that is an [optional](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjr) `Meal`, which means that at any point, it may be `nil`.

You care about configuring and passing the `Meal` only if the Save button was tapped. To be able to determine when this happens, add the Save button as an outlet in `MealViewController.swift`.

__To connect the Save button to the MealViewController code__

1. Open your storyboard.
2. Click the Assistant button in the Xcode toolbar to open the assistant editor.

   （原归档配图未能恢复：`assistant_editor_toggle_2x.png`）
3. If you want more space to work, collapse the project navigator and utility area by clicking the Navigator and Utilities buttons in the Xcode toolbar.

   （原归档配图未能恢复：`navigator_utilities_toggle_on_2x.png`）
4. In your storyboard, select the Save button.
5. Control-drag from the Save button on your canvas to the code display in the editor on the right, stopping the drag at the line just below your `ratingControl` property in `MealViewController.swift`.

   （原归档配图获取待重试：`IN_savebutton_dragoutlet_2x.png`）
6. In the dialog that appears, for Name, type `saveButton`. Leave the rest of the options as they are.

   （原归档配图获取待重试：`IN_savebutton_addoutlet_2x.png`）
7. Click Connect.

You now have a way to identify the Save button.

### Create an Unwind Segue

The task now is to pass the `Meal` object to `MealTableViewController` when a user taps the Save button and discard it when a user taps the Cancel button, switching from displaying the meal detail scene to displaying the meal list in either case.

To accomplish this, you’ll use an unwind segue. An [unwind segue](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonzt) moves backward through one or more segues to return the user to a scene managed by an existing view controller. While regular segues create a new instance of the destination view controller, unwind segues let you return to view controllers that already exist. Use unwind segues to implement navigation back to an existing view controller.

Whenever a segue gets triggered, it provides a place for you to add your own code that gets executed. This method is called `prepare(for:sender:)`, and it gives you a chance to store data and do any necessary cleanup on the [source view controller](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjsge) (the view controller that the segue is coming from). You’ll implement this method in `MealViewController` to do exactly that.

__To implement the prepare(for:sender:) method on MealViewController__

1. Return to the standard editor by clicking the Standard button.

   （原归档配图未能恢复：`standard_toggle_2x.png`）
2. Open `MealViewController.swift`.
3. At the top of the file, under `import UIKit`, add the following:

   1. `import os.log`

   This imports the unified logging system. Like the `print()` function, the unified logging system lets you send messages to the console. However, the unified logging system gives you more control over when messages appear and how they are saved.

   > [!NOTE]
   >
   > For more information on the unified logging system, see _Logging Reference_.
4. In `MealViewController.swift`, above the `//MARK: Actions` section, add the following:

   1. `//MARK: Navigation`

   This is a comment to help you (and anybody else who reads your code) know that this method is related to the navigation flow of your app.
5. Below the comment, add this method skeleton:

   1. `// This method lets you configure a view controller before it's presented.`
   2. `override func prepare(for segue: UIStoryboardSegue, sender: Any?) {`
   3. `}`
6. In the `prepare(for:sender:)` method, add a call to the superclass’s implementation:

   1. `super.prepare(for: segue, sender: sender)`

   The `UIViewController` class’s implementation doesn’t do anything, but it’s a good habit to always call `super.prepare(for:sender:)` whenever you override `prepare(for:sender:)`. That way you won’t forget it when you subclass a different class.
7. Below the call to `super.prepare(for:sender:)`, add the following `guard` statement:

   1. `// Configure the destination view controller only when the save button is pressed.`
   2. `guard let button = sender as? UIBarButtonItem, button === saveButton else {`
   3. `os_log("The save button was not pressed, cancelling", log: OSLog.default, type: .debug)`
   4. `return`
   5. `}`

   This code verifies that the sender is a button, and then uses the [identity operator](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonby) (`===`) to check that the objects referenced by the `sender` and the `saveButton` outlet are the same.

   If they are not, the `else` statement is executed. The app logs a debug message using the system’s standard logging mechanisms. Debug messages contain information that may be useful during debugging or when troubleshooting specific problems. They are intended for debugging environments, and do not appear in a shipping app.

   After logging the debug message, the method returns.
8. Below the `else` statement, add the following code:

   1. `let name = nameTextField.text ?? ""`
   2. `let photo = photoImageView.image`
   3. `let rating = ratingControl.rating`

   This code creates constants from the current text field text, selected image, and rating in the scene.

   Notice the nil coalescing operator (`??`) in the `name` line. The [nil coalescing operator](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjsgi) is used to return the value of an optional if the optional has a value, or return a default value otherwise. Here, the operator unwraps the optional `String` returned by `nameTextField.text` (which is optional because there may or may not be text in the text field), and returns that value if it’s a valid string. But if it’s `nil`, the operator the returns the empty string (`""`) instead.
9. Add the following code:

   1. `// Set the meal to be passed to MealTableViewController after the unwind segue.`
   2. `meal = Meal(name: name, photo: photo, rating: rating)`

   This code configures the `meal` property with the appropriate values before segue executes.

   > [!NOTE]
   >
   > The `Meal` class’s `init?(name:, photo:, rating:)` initializer is a failable initializer. If the `name` parameter is an empty string, or if the `rating` parameter is less than `0` or greater than `5,` this code assigns `nil` to the `meal` variable. Otherwise, it assigns a new `Meal` object to the the `meal` variable.

Your `prepare(for:sender:)` method should look like this:

1. `// This method lets you configure a view controller before it's presented.`
3. `override func prepare(for segue: UIStoryboardSegue, sender: Any?) {`
5. `super.prepare(for: segue, sender: sender)`
7. `// Configure the destination view controller only when the save button is pressed.`
8. `guard let button = sender as? UIBarButtonItem, button === saveButton else {`
9. `os_log("The save button was not pressed, cancelling", log: OSLog.default, type: .debug)`
10. `return`
11. `}`
13. `let name = nameTextField.text ?? ""`
14. `let photo = photoImageView.image`
15. `let rating = ratingControl.rating`
17. `// Set the meal to be passed to MealTableViewController after the unwind segue.`
18. `meal = Meal(name: name, photo: photo, rating: rating)`
19. `}`

The next step in creating the unwind segue is to add an action method to the [destination view controller](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjrgu) (the view controller that the segue is going to). This method must be marked with the `IBAction` attribute and take a segue (`UIStoryboardSegue`) as a parameter. Because you want to unwind back to the meal list scene, you need to add an action method with this format to `MealTableViewController.swift`.

In this method, you’ll write the logic to add the new meal (that’s passed from `MealViewController`, the source view controller) to the meal list data and add a new row to the table view in the meal list scene.

__To add an action method to MealTableViewController__

1. Open `MealTableViewController.swift`.
2. Before the `//MARK: Private Methods` section, add the following line:

   1. `//MARK: Actions`
3. Below the `//MARK: Actions` comment, add the following:

   1. `@IBAction func unwindToMealList(sender: UIStoryboardSegue) {`
   3. `}`
4. In the `unwindToMealList(_:)` action method, add the following `if` statement:

   1. `if let sourceViewController = sender.sourceViewController as? MealViewController, meal = sourceViewController.meal {`
   2. `}`

   There’s a lot happening in the condition for this `if` statement.

   This code uses the [optional type cast operator](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvoojz) (`as?`) to try to [downcast](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvoobx) the segue’s source view controller to a `MealViewController` instance. You need to downcast because `sender.sourceViewController` is of type `UIViewController`, but you need to work with a `MealViewController`.

   The operator returns an optional value, which will be `nil` if the downcast wasn’t possible. If the downcast succeeds, the code assigns the `MealViewController` instance to the [local](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjrgy) constant `sourceViewController`, and checks to see if the meal property on `sourceViewController` is `nil`. If the `meal` property is non-`nil`, the code assigns the value of that property to the local constant `meal` and executes the `if` statement.

   If either the downcast fails or the `meal` property on `sourceViewController` is `nil`, the condition evaluates to `false` and the `if` statement doesn’t get executed.
5. In the `if` statement, add the following code:

   1. `// Add a new meal.`
   2. `let newIndexPath = IndexPath(row: meals.count, section: 0)`

   This code computes the location in the table view where the new table view cell representing the new meal will be inserted, and stores it in a local constant called `newIndexPath`.
6. In the `if` statement, below the previous line of code, add the following code:

   1. `meals.append(meal)`

   This adds the new meal to the existing list of meals in the data model.
7. In the `if` statement, below the previous line of code, add the following code:

   1. `tableView.insertRows(at: [newIndexPath], with: .automatic)`

   This animates the addition of a new row to the table view for the cell that contains information about the new meal. The `.automatic` animation option uses the best animation based on the table’s current state, and the insertion point’s location.

You’ll finish a more advanced implementation of this method in a little while, but for now, the `unwindToMealList(_:)` action method should look like this:

1. `@IBAction func unwindToMealList(sender: UIStoryboardSegue) {`
2. `if let sourceViewController = sender.source as? MealViewController, let meal = sourceViewController.meal {`
4. `// Add a new meal.`
5. `let newIndexPath = IndexPath(row: meals.count, section: 0)`
7. `meals.append(meal)`
8. `tableView.insertRows(at: [newIndexPath], with: .automatic)`
9. `}`
10. `}`

Now you need to create the actual unwind segue to trigger this action method.

__To link the Save button to the unwindToMealList action method__

1. Open your storyboard.
2. On the canvas, Control-drag from the Save button to the Exit item at the top of the meal detail scene.

   （原归档配图获取待重试：`IN_savebutton_dragunwind_2x.png`）

   A menu appears in the location where the drag ended. It shows all the available unwind action methods.

   （原归档配图获取待重试：`IN_savebutton_unwindsegue_2x.png`）
3. Choose `unwindToMealListWithSender:` from the shortcut menu.

   Now, when users tap the Save button, they navigate back to the meal list scene, during which process the `unwindToMealList(sender:)` action method is called.

> [!NOTE]
>
> Unwind segues provide a simple method for passing information back to an earlier view controller. Sometimes, however, you need more complex communication between your view controllers. In those cases, consider using the [delegate](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomzw) pattern.
>
> For more information, see Delegation in _The Swift Programming Language (Swift 3.0.1)_.

_Checkpoint:_ Run your app. Now when you click the Add button (`+`), create a new meal, and click Save, you should see the new meal in your meal list.

> [!IMPORTANT]
>
> If you don’t see the `unwindToMealListWithSender:` method in the shortcut menu, make sure that the method has the right signature.
>
> `@IBAction func unwindToMealList(sender: UIStoryboardSegue)`

### Disable Saving When the User Doesn't Enter an Item Name

What happens if a user tries to save a meal with no name? Because the `meal` property on `MealViewController` is an optional and you set your initializer up to fail if there’s no name, the `Meal` object doesn’t get created and added to the meal list—which is what you expect to happen. But you can take this a step further and keep users from accidentally trying to add meals without a name by disabling the Save button while they’re typing a meal name, and checking that they’ve specified a valid name before letting them dismiss the keyboard.

__To disable the Save button when there’s no item name__

1. In `MealViewController.swift`, find the `//MARK: UITextFieldDelegate` section.

   You can jump to it quickly using the [functions menu](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonbr), which appears if you click the name of the file at the top of the editor area.
2. In this section, add another `UITextFieldDelegate` method:

   1. `func textFieldDidBeginEditing(_ textField: UITextField) {`
   2. `// Disable the Save button while editing.`
   3. `saveButton.isEnabled = false`
   4. `}`

   The `textFieldDidBeginEditing` method gets called when an editing session begins, or when the keyboard gets displayed. This code disables the Save button while the user is editing the text field.
3. Scroll to the bottom of the class. Before the last closing curly brace (`}`), add the following line:

   1. `//MARK: Private Methods`
4. Below the `//MARK: Private Methods` comment, add the following method:

   1. `private func updateSaveButtonState() {`
   2. `// Disable the Save button if the text field is empty.`
   3. `let text = nameTextField.text ?? ""`
   4. `saveButton.isEnabled = !text.isEmpty`
   5. `}`

   This is a helper method to disable the Save button if the text field is empty.
5. Go back to the the `//MARK: UITextFieldDelegate` section and find the `textFieldDidEndEditing(_:)` method:

   1. `func textFieldDidEndEditing(_ textField: UITextField) {`
   2. `}`

   The implementation should be empty at this point.
6. Add these lines of code:

   1. `updateSaveButtonState()`
   2. `navigationItem.title = textField.text`

   The first line calls `updateSaveButtonState()` to check if the text field has text in it, which enables the Save button if it does. The second line sets the title of the scene to that text.
7. Find the `viewDidLoad()` method.

   1. `override func viewDidLoad() {`
   2. `super.viewDidLoad()`
   4. `// Handle the text field’s user input through delegate callbacks.`
   5. `nameTextField.delegate = self`
   6. `}`
8. Add a call to `updateSaveButtonState()` in the implementation to make sure the Save button is disabled until a user enters a valid name:

   1. `// Enable the Save button only if the text field has a valid Meal name.`
   2. `updateSaveButtonState()`

Your `viewDidLoad()` method should look like this:

1. `override func viewDidLoad() {`
2. `super.viewDidLoad()`
4. `// Handle the text field’s user input through delegate callbacks.`
5. `nameTextField.delegate = self`
7. `// Enable the Save button only if the text field has a valid Meal name.`
8. `updateSaveButtonState()`
9. `}`

And your `textFieldDidEndEditing(_:)` method should look like this:

1. `func textFieldDidEndEditing(_ textField: UITextField) {`
2. `updateSaveButtonState()`
3. `navigationItem.title = textField.text`
4. `}`

_Checkpoint:_ Run your app. Now when you click the Add button (`+`), the Save button is disabled until you enter a valid (nonempty) meal name and dismiss the keyboard.

（原归档配图获取待重试：`IN_sim_savebuttondisabled_2x.png`）

### Cancel a New Meal Addition

A user might decide to cancel the addition of a new meal, and return to the meal list without saving anything. For this, you’ll implement the behavior of the Cancel button.

__To create and implement a cancel action method__

1. Open your storyboard.
2. Click the Assistant button in the Xcode toolbar to open the assistant editor.

   （原归档配图未能恢复：`assistant_editor_toggle_2x.png`）
3. In your storyboard, select the Cancel button.
4. Control-drag from the Cancel button on your canvas to the code display in the editor on the right, stopping the drag at the line just below the `//MARK: Navigation` comment in `MealViewController.swift`.

   （原归档配图获取待重试：`IN_cancelbutton_dragaction_2x.png`）
5. In the dialog that appears, for Connection, select Action.
6. For Name, type `cancel`.
7. For Type, select `UIBarButtonItem`. Leave the rest of the options as they are.

   （原归档配图获取待重试：`IN_cancelbutton_addaction_2x.png`）
8. Click Connect.

   Xcode adds the necessary code to `MealViewController.swift` to set up the action.

   1. `@IBAction func cancel(_ sender: UIBarButtonItem) {`
   2. `}`
9. In the `cancel(_:)` action method, add the following line of code:

   1. `dismiss(animated: true, completion: nil)`

   The `dismiss(animated:completion:)` method dismisses the modal scene and animates the transition back to the previous scene (in this case, the meal list). The app does not store any data when the meal detail scene is dismissed, and neither the `prepare(for:sender:)` method nor the unwind action method are called.

Your `cancel(_:)` action method should look like this:

1. `@IBAction func cancel(_ sender: UIBarButtonItem) {`
2. `dismiss(animated: true, completion: nil)`
3. `}`

_Checkpoint:_ Run your app. Now when you click the Add button (`+`) and click Cancel instead of Save, you should navigate back to the meal list without adding a new meal.

### Wrapping Up

In this lesson, you learned how to push scenes onto the navigation stack, and how to present views modally. You learned how to navigate back to a previous scene using segue unwinding, how to pass data across segues, and how to dismiss modal views.

At this point, the app displays an initial list of sample meals, and lets you add new meals to the list. In the next lesson, you’ll add the ability to edit and delete meals.

> [!NOTE]
>
> To see the completed sample project for this lesson, download the file and view it in Xcode.
>
> （原归档配图未能恢复：`WWDR_download_icon_withPadding_2x.png`）[Download File](https://developer.apple.com/sample-code/swift/downloads/07_ImplementNavigation.zip)

[Create a Table View](CreateATableView.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqobnknltc)

[Implement Edit and Delete Behavior](ImplementEditAndDeleteBehavior.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqojnknltc)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-12-08](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqojzfvjvomi)

[Next](ImplementEditAndDeleteBehavior.md)[Previous](CreateATableView.md)
