---
title: Start Developing iOS Apps (Swift)
apple_id: TP40015214
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2016-12-08'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/DevelopiOSAppsSwift/CreateATableView.html
archived_at: '2026-07-27T06:57:09.939930Z'
---
> 导航：[总目录](../../../README.md) · [referencelibrary](../../../_indexes/referencelibrary.md) · [Start Developing iOS Apps (Swift)](index.md)


[Next](ImplementNavigation.md)[Previous](DefineYourDataModel.md)

## Create a Table View

In this lesson, you create a second, table view-based scene, that lists the user’s meals. This meal list becomes the initial scene for your app. You also design custom table cells to display each meal.

（原归档配图获取待重试：`CTV_sim_tablecellUI_2x.png`）

### Learning Objectives

At the end of the lesson, you’ll be able to:

- Create a second storyboard scene
- Understand the key components of a table view
- Create and design a custom table view cell
- Understand the roles of table view delegates and data sources
- Use an array to store and work with data
- Display dynamic data in a table view

### Create the Meal List

So far, the FoodTracker app has a single [scene](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonrs), that is, a single screen of content. In a storyboard, each scene contains views managed by that a view controller, and any items added to the controller or its views (for example, Auto Layout constraints). A view is a rectangular region that can draw its own content and respond to user events. Views are instances of the `UIView` class or one of its subclasses. In this case, the scene contains the view controller’s content view, and all of the subviews you added in Interface Builder (the stack view, label, text field, image view, and rating control).

Now it’s time to create another scene that shows the entire list of meals. Fortunately, iOS comes with a built-in class, `UITableView`, designed specifically to display a scrolling list of items. A table view is managed by a table view controller (`UITableViewController`). `UITableViewController` is a [subclass](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomju) of `UIViewController`, which is designed to handle table view-related logic. You’ll create the new scene using a table view controller. The controller displays and manages a table view. In fact, the table view is the controller’s content view, and fills the entire space available to the scene.

__To add a scene with a table view to your storyboard__

1. Open your [storyboard](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvooa), `Main.storyboard`.
2. Open the [Object library](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonju) in the utility area. (Alternatively, choose View > Utilities > Show Object Library.)
3. In the Object library, find a Table View Controller object.
4. Drag a Table View Controller object from the list, and drop it on the [canvas](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonq) to the left of the existing scene.

   If you try to drag the table view to the canvas and nothing happens, you’re probably dragging a table view object rather than a table view controller object. The table view object is just a view representing the table itself. Like other view objects, it must be added as a subview to an existing scene. On the other hand, the table view controller is a full scene. It includes both a table view and the controller that manages the table view.

You now have two scenes, one for displaying the meal list and one for displaying the details of a single meal.

（原归档配图获取待重试：`CTV_newtableview_2x.png`）

It makes sense to have the meal list be the first thing users see when they launch your app, so tell Xcode that’s your intent by setting the meal list as the first scene.

__To set the meal list as the initial scene__

1. If you want more space to work, collapse the project navigator and utility area by clicking the Navigator and Utilities buttons in the Xcode toolbar.

   （原归档配图未能恢复：`navigator_utilities_toggle_on_2x.png`）

   You can also collapse the outline view.
2. Drag the [storyboard entry point](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonrw) from the meal detail scene to the meal list scene.

   （原归档配图获取待重试：`CTV_originalinitialscene_2x.png`）

   The table view controller is set as the initial view controller in your storyboard, making the meal list the first scene that loads on app launch.

   （原归档配图未能恢复：`CTV_newinitialscene_2x.png`）

_Checkpoint:_ Run your app. Instead of the meal detail scene with its text field, image view, and rating control, you should now see an empty table view—a screen with a number of horizontal dividers to separate it into rows, but with no content in each row.

（原归档配图获取待重试：`CTV_sim_emptytv_2x.png`）

You need to change a few settings on this table view so you can use it in your app.

__To configure the table view__

1. In your storyboard, open the [outline view](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjw) and expand the [utility area](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonzs).
2. In the outline view, select Table View.

   The table view is nested under Table View Controller Scene > Table View Controller. You may have to click the disclosure triangles next to those objects to see the nested table view.

   （原归档配图获取待重试：`CTV_outlineview_table_2x.png`）
3. With the table view selected, open the Size inspector （原归档配图未能恢复：`inspector_size_2x.png`） in the utility area.
4. In the Size inspector, find the field labeled Row Height and type `90`. Press Return.

You’ll come back to working on the table view itself in a little while, after you design an interface for what the table view displays: its table view cells.

### Design Custom Table Cells

The individual rows in a table view are managed by table view cells (`UITableViewCell`), which are responsible for drawing their contents. Table view cells come with a variety of predefined behavior and default cell styles; however, because you have more content to display in each cell than the default styles allow, you’ll need to define a custom cell style.

__To create a subclass of UITableViewCell__

1. Expand the Navigator area and open the Project navigator.
2. Choose File > New > File (or press Command-N).
3. At the top of the dialog that appears, select iOS.
4. Select Cocoa Touch Class, and click Next.
5. In the Class field, type `Meal`.
6. In the “Subclass of” field, select `UITableViewCell`.

   The class title changes to `MealTableViewCell`. Xcode makes it clear from the naming that you’re creating a custom table view cell, so leave the new name as is.
7. Make sure the Language option is set to Swift.
8. Click Next.

   The save location defaults to your project directory.

   The Group option defaults to your app name, FoodTracker.
9. In the Targets section, make sure your app is selected and the tests for your app are unselected.
10. Click Create.

    Xcode creates a file that defines the `MealTableViewCell` class: `MealTableViewCell.swift`.
11. In the Project navigator, reposition the `MealTableViewCell.swift` file under the other Swift files, if necessary.

Now, open your storyboard again.

If you look at the meal list scene in your storyboard, you’ll notice that it shows a single table view cell.

（原归档配图获取待重试：`CTV_singletvcell_2x.png`）

This cell is a prototype cell for the table. You can define the design and behavior of this cell. The table can then create instances of this cell. But first, you need to connect the table view cell in your scene to the custom cell subclass you just created.

__To configure a custom cell for your table view__

1. In the outline view, select Table View Cell.

   The cell is nested under Table View Controller Scene > Table View Controller > Table View. You may have to disclose those objects to see the table view cell.

   （原归档配图获取待重试：`CTV_outlineview_cell_2x.png`）
2. With the table view cell selected, open the [Attributes inspector](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjz) （原归档配图未能恢复：`inspector_attributes_2x.png`） in the utility area.
3. In the Attributes inspector, find the field labeled Identifier and type `MealTableViewCell`. Press Return.

   You will use this identifier to create instances of this prototype cell.
4. Open the Size inspector （原归档配图未能恢复：`inspector_size_2x.png`）.
5. In the Size inspector, find the field labeled Row Height and type `90`. Make sure the Custom checkbox next to this field is selected.

   （原归档配图获取待重试：`CTV_inspector_size_cell_2x.png`）

   Press Return to display the new cell height in your storyboard.
6. Open the Identity inspector （原归档配图未能恢复：`inspector_identity_2x.png`）.

   Recall that the [Identity inspector](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvoobq) lets you edit properties of an object in your storyboard related to that object’s identity, such as what class the object belongs to.
7. In the Identity inspector, find the Class field and select `MealTableViewCell`.

   （原归档配图未能恢复：`CTV_inspector_identity_cell_2x.png`）

With the cell configured, you can design its custom user interface directly in the storyboard. You’ll need a label, an image view, and a rating control. You can reuse the rating control class that you created in an earlier lesson. Your custom interface will then contain the meal name, photo, and rating.

（原归档配图获取待重试：`CTV_sim_tablecellUI_2x.png`）

__To design the interface of the custom table cell__

1. Use the Object library to find an Image View object and drag it onto the table cell.
2. Drag and resize the image view so that it’s square, flush against the left, top, and bottom of the cell.

   （原归档配图未能恢复：`CTV_imageview_resize_2x.png`）
3. With the image view selected, open the Attributes inspector （原归档配图未能恢复：`inspector_attributes_2x.png`） in the Utility area.
4. In the Attributes inspector, find the Image field and select `defaultPhoto`. If you didn’t add a default photo to your project in a previous lesson, add it now.

   （原归档配图获取待重试：`CTV_imageview_setdefault_2x.png`）
5. Use the Object library to find a Label object and drag it onto the table cell. You will use the label to show the meal’s name.
6. Drag the label so that its lined up with the guidelines to the right side of the image view and to the top margin of the table view cell.

   （原归档配图获取待重试：`CTV_label_drag_2x.png`）
7. Resize the label so that its right edge stretches to the cell’s right margin.

   （原归档配图未能恢复：`CTV_label_resize_2x.png`）
8. Use the Object library to find a Horizontal Stack View object and drag it onto the table cell.
9. With the stack view selected, open the Size inspector （原归档配图未能恢复：`inspector_size_2x.png`） in the utility area.
10. In the Size inspector, type `44` in the Height field and `252` in the Width field. Press Return.
11. Drag the stack view so that it’s below the label and aligned with the label’s left margin.

    （原归档配图获取待重试：`CTV_ratingcontrol_resize_2x.png`）
12. With the view selected, open the Identity inspector （原归档配图未能恢复：`inspector_identity_2x.png`）.
13. In the Identity inspector, find the field labeled Class and select `RatingControl`.

    （原归档配图未能恢复：`CTV_inspector_identity_control_2x.png`）

    If you don’t see `RatingControl` as an option in the pop-up menu, make sure you have the stack view selected on the canvas.
14. With the view selected, open the Attributes inspector （原归档配图未能恢复：`inspector_attributes_2x.png`）.
15. In the Attributes inspector, set the Spacing to 8. Next, find the field labeled Interaction and deselect the User Interaction Enabled checkbox.

    （原归档配图未能恢复：`CTV_tablecellUI_2x.png`）

    You designed your custom rating control class to be interactive, but you don’t want users to be able to change the rating from the cell view. Instead, tapping anywhere in the cell should select the cell. So it’s important to disable that interaction when it’s in this context.

_Checkpoint:_ Run your app. The table view cells now look taller. But even though you added all the necessary user interface elements to your table view cells, they’re showing up empty, just like before. Why’s that?

（原归档配图获取待重试：`CTV_sim_wideemptycells_2x.png`）

In a storyboard, you can configure a table view to display static data (supplied in the storyboard) or dynamic data (programmatically supplied by the table view controller). By default, the table view controller uses dynamic data. This means the interface you created in the storyboard is simply a prototype for your cell. You still need to create instances of this cell in code and fill them with your app’s data.

For now, you can preview your cell using the [assistant editor](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonzw).

__To preview your interface__

1. Click the Assistant button in the Xcode toolbar to open the assistant editor.

   （原归档配图未能恢复：`assistant_editor_toggle_2x.png`）
2. If you want more space to work, collapse the [project navigator](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjx) and [utility area](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonzs) by clicking the Navigator and Utilities buttons in the Xcode toolbar.

   （原归档配图未能恢复：`navigator_utilities_toggle_on_2x.png`）

   You can also collapse the outline view.
3. In the editor selector bar, which appears at the top of the assistant editor, switch the assistant editor from Automatic to Preview > Main.storyboard (Preview).

   （原归档配图未能恢复：`CTV_assistant_switchtopreview_2x.png`）

   The preview shows the image view and the label. The rating control isn’t rendered in the preview, but otherwise the table view cell looks as expected.

   （原归档配图未能恢复：`CTV_assistant_preview_2x.png`）

> [!NOTE]
>
> If you see the wrong scene in the preview, make sure to select the table view scene by clicking its [scene dock](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonrt).

### Add Images to Your Project

Next, you need to add a few sample images to your project. You’ll use these images when you load initial meal data into your app.

You can find sample images within the `Images/` folder of the downloadable file at the end of this lesson, or use your own images. (Just make sure the names of the images you use match the image names in the code later.)

__To add images to your project__

1. If the assistant editor is open, return to the standard editor by clicking the Standard button.

   Open the project navigator and utility area by clicking the Navigator and Utilities buttons in the Xcode toolbar.

   （原归档配图未能恢复：`navigator_utilities_toggle_on_2x.png`）
2. In the project navigator, select `Assets.xcassets` to view the asset catalog.

   Recall that the [asset catalog](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonrz) is a place to store and organize your image assets for an app.
3. In the bottom left corner, click the plus (`+`) button and select New Folder from the pop-up menu.
4. Double-click the folder name and rename it `Sample Images`.
5. With the folder selected, in the bottom left corner, click the plus (`+`) button and choose New Image Set from the pop-up menu.
6. Double-click the image set name and rename it to a name you’ll remember when you’re writing it in code.
7. On your computer, select the image you want to add.
8. Drag and drop the image into the `2x` slot in the image set.

Repeat steps 5–8 for as many images as you like. In this lesson it is assumed that you have three different images named `meal1`, `meal2`, and `meal3`.

（原归档配图获取待重试：`CTV_assetcatalog_2x.png`）

### Connect the Table Cell UI to Code

Before you can display dynamic data in your table view cells, you need to create [outlet](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjv) connections between the prototype in your storyboard and the code that represents the table view cell in `MealTableViewCell.swift`.

__To connect the views to the MealTableViewCell.swift code__

1. In your storyboard, select the label in the table view cell.
2. Click the Assistant button in the Xcode toolbar to open the assistant editor.

   （原归档配图未能恢复：`assistant_editor_toggle_2x.png`）
3. If you want more space to work, collapse the project navigator and utility area by clicking the Navigator and Utilities buttons in the Xcode toolbar.

   （原归档配图未能恢复：`navigator_utilities_toggle_on_2x.png`）
4. In the editor selector bar, which appears at the top of the assistant editor, switch the assistant editor from Preview to Automatic > `MealTableViewCell.swift`.

   （原归档配图未能恢复：`CTV_assistant_switchtocode_2x.png`）

   `MealTableViewCell.swift` is displayed in the editor on the right.
5. In `MealTableViewCell.swift`, find the `class` line, which should look like this:

   1. `class MealTableViewCell: UITableViewCell {`
6. Below the `class` line, add the following:

   1. `//MARK: Properties`
7. Control-drag from the label on your canvas to the code display in the editor on the right, stopping the drag at the line below the comment you just added in `MealTableViewCell.swift`.

   （原归档配图获取待重试：`CTV_label_dragoutlet_2x.png`）
8. In the dialog that appears, for Name, type `nameLabel`. Leave the rest of the options as they are.

   （原归档配图未能恢复：`CTV_label_addoutlet_2x.png`）
9. Click Connect.
10. In your storyboard, select the image view in the table view cell.
11. Control-drag from the image view on your canvas to the code display in the editor on the right, stopping the drag at the line just below the `nameLabel` property in `MealTableViewCell.swift`.

    （原归档配图未能恢复：`CTV_imageview_dragoutlet_2x.png`）
12. In the dialog that appears, for Name, type `photoImageView`.

    Leave the rest of the options as they are, and click Connect.

    （原归档配图获取待重试：`CTV_imageview_addoutlet_2x.png`）
13. In your storyboard, select the rating control in the table view cell.
14. Control-drag from the rating control on your canvas to the code display in the editor on the right, stopping the drag at the line just below the `photoImageView` property in `MealTableViewCell.swift`.

    （原归档配图获取待重试：`CTV_ratingcontrol_dragoutlet_2x.png`）
15. In the dialog that appears, for Name, type `ratingControl`.

    Leave the rest of the options as they are, and click Connect.

    （原归档配图获取待重试：`CTV_ratingcontrol_addoutlet_2x.png`）

Your outlets in `MealTableViewCell.swift` should look like this:

1. `@IBOutlet weak var nameLabel: UILabel!`
2. `@IBOutlet weak var photoImageView: UIImageView!`
3. `@IBOutlet weak var ratingControl: RatingControl!`

### Load Initial Data

To display any real data in your table cells, you need to write code to load that data. At this point, you have a data model for a meal: the `Meal` class. You also need to keep a list of those meals. The natural place to track this is in a custom view controller subclass that’s connected to the meal list scene. This view controller will manage the view that displays the list of meals, and have a reference to the data model behind what’s shown in the user interface.

First, create a custom table view controller subclass to manage the meal list scene.

__To create a subclass of UITableViewController__

1. Choose File > New > File (or press Command-N).
2. At the top of the dialog that appears, select iOS, and then select Cocoa Touch Class.
3. Click Next.
4. In the Class field, type `Meal`.
5. In the “Subclass of” field, select `UITableViewController`.

   The class title changes to `MealTableViewController`. Leave that as is.
6. Make sure the “Also create XIB file” option is unselected.

   XIB files are an older way of designing the views managed by a view controller. They predate storyboards and basically represent a single scene from a storyboard. You won’t need an XIB file for this view controller, because you have already defined its content in the app’s storyboard.
7. Make sure the Language option is set to Swift.
8. Click Next.

   The save location defaults to your project directory.

   The Group option defaults to your app name, FoodTracker.

   In the Targets section, your app is selected and the tests for your app are unselected.
9. Leave these defaults as they are, and click Create.

   Xcode creates `MealTableViewController.swift`, a source code file that defines your custom table view controller subclass.
10. If necessary, in the Project navigator, drag the `MealTableViewController.swift` file so that it’s positioned with the other Swift files.

In this custom subclass, you can now define a [property](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjy) to store a list of `Meal` objects. The [Swift standard library](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjrge) includes a [structure](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjt) called `Array` that works well for tracking lists of items.

__To load the initial data__

1. If the assistant editor is open, return to the standard editor by clicking the Standard button.

   Expand the project navigator and utility area by clicking the Navigator and Utilities buttons in the Xcode toolbar.

   （原归档配图未能恢复：`standard_toggle_2x.png`）
2. Open `MealTableViewController.swift`.
3. Below the `class` line in `MealTableViewController.swift`, add the following code:

   1. `//MARK: Properties`
   3. `var meals = [Meal]()`

   This code declares a property on `MealTableViewController` and initializes it with a default value (an empty [array](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomry) of `Meal` objects). By making `meals` a variable (`var`) instead of a constant, you make the array [mutable](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjr), which means you can add items to it after you initialize it.
4. The table view controller template includes a number of method stubs and commented out methods. These are placeholder implementations that you can uncomment and expand to define the table’s appearance and behavior. You will look at these methods after you have the model data set up. For now, scroll past all the template methods, and add the following code before the final closing brace (`}`):

   1. `//MARK: Private Methods`
   3. `private func loadSampleMeals() {`
   5. `}`

   This is a helper method to load sample data into the app.
5. In the `loadSampleMeals()` method, start by loading the three meal images:

   1. `let photo1 = UIImage(named: "meal1")`
   2. `let photo2 = UIImage(named: "meal2")`
   3. `let photo3 = UIImage(named: "meal3")`

   Make sure the names of the images in your project match the names you write in this code.
6. After loading the images, create three meal objects.

   1. `guard let meal1 = Meal(name: "Caprese Salad", photo: photo1, rating: 4) else {`
   2. `fatalError("Unable to instantiate meal1")`
   3. `}`
   5. `guard let meal2 = Meal(name: "Chicken and Potatoes", photo: photo2, rating: 5) else {`
   6. `fatalError("Unable to instantiate meal2")`
   7. `}`
   9. `guard let meal3 = Meal(name: "Pasta with Meatballs", photo: photo3, rating: 3) else {`
   10. `fatalError("Unable to instantiate meal2")`
   11. `}`

   Because the `Meal` class’s `init!(name:, photo:, rating:)` initializer is failable, you need to check the result returned by the initializer. In this case, you are passing valid parameters, so the initializer should never fail. If the initializer does fail, you have a bug in your code. To help you identify and fix any bugs, if the initializer does fail, the `fatalError()` function prints the error message to the console and the app terminates.
7. After creating the `Meal` objects, add them to the `meals` array using this code:

   1. `meals += [meal1, meal2, meal3]`
8. Find the `viewDidLoad()` method. The template implementation looks like this:

   1. `override func viewDidLoad() {`
   2. `super.viewDidLoad()`
   4. `// Uncomment the following line to preserve selection between presentations`
   5. `// self.clearsSelectionOnViewWillAppear = false`
   7. `// Uncomment the following line to display an Edit button in the navigation bar for this view controller.`
   8. `// self.navigationItem.rightBarButtonItem = self.editButtonItem()`
   9. `}`

   The template implementation of this method includes comments that were inserted by Xcode when it created `MealTableViewController.swift`. Code comments like this provide helpful hints and contextual information in source code files, but you don’t need them for this lesson.
9. In the `viewDidLoad()` method, delete the comments and add this code after the call to `super.viewDidLoad()` to load the sample meal data:

   1. `// Load the sample data.`
   2. `loadSampleMeals()`

   When the view loads, this code calls the helper method you just wrote to load the sample data. You separated this into its own method to make your code more modular and readable.

Your `viewDidLoad()` method should look like this:

1. `override func viewDidLoad() {`
2. `super.viewDidLoad()`
4. `// Load the sample data.`
5. `loadSampleMeals()`
6. `}`

And your `loadSampleMeals()` method should look something like this:

1. `private func loadSampleMeals() {`
3. `let photo1 = UIImage(named: "meal1")`
4. `let photo2 = UIImage(named: "meal2")`
5. `let photo3 = UIImage(named: "meal3")`
7. `guard let meal1 = Meal(name: "Caprese Salad", photo: photo1, rating: 4) else {`
8. `fatalError("Unable to instantiate meal1")`
9. `}`
11. `guard let meal2 = Meal(name: "Chicken and Potatoes", photo: photo2, rating: 5) else {`
12. `fatalError("Unable to instantiate meal2")`
13. `}`
15. `guard let meal3 = Meal(name: "Pasta with Meatballs", photo: photo3, rating: 3) else {`
16. `fatalError("Unable to instantiate meal2")`
17. `}`
19. `meals += [meal1, meal2, meal3]`
20. `}`

_Checkpoint:_ Build your project by choosing Product > Build. It should build without errors. Note: At this point, you may see an Xcode warning related to the fact that there’s no way to reach the View Controller scene in the app. You will fix that in the next lesson. For the rest of this lesson, just ignore it.

> [!IMPORTANT]
>
> If you’re running into build issues, make sure the names of the images in your project exactly match the names you used in the code.

### Display the Data

At this point, your custom table view controller subclass, `MealTableViewController`, has a mutable array that’s prepopulated with some sample meals. Now you need to display this data in the user interface.

To display dynamic data, a table view needs two important helpers: a data source and a delegate. A table view [data source](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjsga), as implied by its name, supplies the table view with the data it needs to display. A table view [delegate](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomzw) helps the table view manage cell selection, row heights, and other aspects related to displaying the data. By default, `UITableViewController` and its subclasses adopt the necessary protocols to make the table view controller both a data source (`UITableViewDataSource` protocol) and a delegate (`UITableViewDelegate` protocol) for its associated table view. Your job is to implement the appropriate protocol methods in your table view controller subclass so that your table view has the correct behavior.

A functioning table view requires three table view data source methods.

1. `func numberOfSections(in tableView: UITableView) -> Int`
2. `func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int`
3. `func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell`

The first of these is `numberOfSections(In:)`, which tells the table view how many sections to display. Sections are visual groupings of cells within table views, which is especially useful in table views with a lot of data. For a simple table view like the one in the FoodTracker app, you just need the table view to display a single section, so the implementation of the `numberOfSections(In:)` data source method is straightforward.

__To display a section in your table view__

1. In `MealTableViewController.swift`, find the `numberOfSections(In:)` data source method. The template implementation looks like this:

   1. `override func numberOfSections(in tableView: UITableView) -> Int {`
   2. `// #warning Incomplete implementation, return the number of sections`
   3. `return 0`
   4. `}`
2. Change the return value from `0` to `1`, and remove the warning comment.

   1. `override func numberOfSections(in tableView: UITableView) -> Int {`
   2. `return 1`
   3. `}`

   This code makes the table view show 1 section instead of 0. You removed the comment that says `#warning Incomplete implementation` because you’ve completed the implementation.

The next data source method, `tableView(_:numberOfRowsInSection:)`, tells the table view how many rows to display in a given section. Your table view has only a single section, and each `Meal` object should have its own row. That means that the number of rows should be the number of `Meal` objects in your `meals` array.

__To return the number of rows in your table view__

1. In `MealTableViewController.swift`, find the `tableView(_:numberOfRowsInSection:)` data source method. The template implementation looks like this:

   1. `override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {`
   2. `// #warning Incomplete implementation, return the number of rows`
   3. `return 0`
   4. `}`

   You want to return the number of meals you have. `Array` has a property called `count` that returns the number of items in the array, so the number of rows is `meals.count`.
2. Change the `tableView(_:numberOfRowsInSection:)` data source method to return the appropriate number of rows, and remove the warning comment.

   1. `override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {`
   2. `return meals.count`
   3. `}`

The last data source method, `tableView(_:cellForRowAt:)`, configures and provides a cell to display for a given row. Each row in a table view has one cell, and that cell determines the content that appears in that row and how that content is laid out.

For table views with a small number of rows, all rows may be onscreen at once, so this method gets called for each row in your table. But table views with a large number of rows display only a small fraction of their total items at a given time. It’s most efficient for table views to ask for only the cells for rows that are being displayed, and that’s what `tableView(_:cellForRowAt:)` allows the table view to do.

For any given row in the table view, you configure the cell by fetching the corresponding `Meal` in the `meals` array, and then setting the cell’s properties to corresponding values from the `Meal` class.

__To configure and display cells in your table view__

1. In `MealTableViewController.swift`, find and uncomment the `tableView(_:cellForRowAt:)` data source method. (To uncomment the method, remove the `/*` and `*/` characters surrounding it.)

   After you do that, the template implementation looks like this:

   1. `override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {`
   2. `let cell = tableView.dequeueReusableCell(withIdentifier: "reuseIdentifier", for: indexPath)`
   4. `// Configure the cell...`
   6. `return cell`
   7. `}`

   The `dequeueReusableCell(withIdentifier:for:)` method requests a cell from the table view. Instead of creating new cells and deleting old cells as the user scrolls, the table tries to reuse the cells when possible. If no cells are available, `dequeueReusableCell(withIdentifier:for:)` instantiates a new one; however, as cells scroll off the scene, they are reused. The identifier tells `dequeueReusableCell(withIdentifier:for:)` which type of cell it should create or reuse.

   To make this code work for your app, you’ll need to change the identifier to the prototype cell identifier you set in the storyboard (`MealTableViewCell`), and then add code to configure the cell.
2. Add code at the beginning of the method, before the rest of the template implementation:

   1. `// Table view cells are reused and should be dequeued using a cell identifier.`
   2. `let cellIdentifier = "MealTableViewCell"`

   This creates a constant with the identifier you set in the storyboard.
3. Update the template’s identifier to the `cellIdentifier` variable. The second line of code in the method should now look like this:

   1. `let cell = tableView.dequeueReusableCell(withIdentifier: cellIdentifier, for: indexPath)`
4. Because you created a custom cell class that you want to use, [downcast](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvoobx) the type of the cell to your custom cell subclass, `MealTableViewCell`.

   1. `guard let cell = tableView.dequeueReusableCell(withIdentifier: cellIdentifier, for: indexPath) as? MealTableViewCell else {`
   2. `fatalError("The dequeued cell is not an instance of MealTableViewCell.")`
   3. `}`

   There’s a lot going on in this code:

   - The `as? MealTableViewCell` expression attempts to downcast the returned object from the `UITableViewCell` class to your `MealTableViewCell` class. This returns an optional.
   - The `guard let` expression safely unwraps the optional.
   - If your storyboard is set up correctly, and the `cellIdentifier` matches the identifier from your storyboard, then the downcast should never fail. If the downcast does fail, the `fatalError()` function prints an error message to the console and terminates the app.
5. After the `guard` statement, add the following code:

   1. `// Fetches the appropriate meal for the data source layout.`
   2. `let meal = meals[indexPath.row]`

   This code fetches the appropriate meal from the `meals` array.
6. Now, use the meal object to configure your cell. Replace the `// Configure the cell` comment with the following code:

   1. `cell.nameLabel.text = meal.name`
   2. `cell.photoImageView.image = meal.photo`
   3. `cell.ratingControl.rating = meal.rating`

   This code sets each of the views in the table view cell to display the corresponding data from `meal` object.

Your `tableView(_:cellForRowAt:)` method should look like this:

1. `override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {`
3. `// Table view cells are reused and should be dequeued using a cell identifier.`
4. `let cellIdentifier = "MealTableViewCell"`
6. `guard let cell = tableView.dequeueReusableCell(withIdentifier: cellIdentifier, for: indexPath) as? MealTableViewCell else {`
7. `fatalError("The dequeued cell is not an instance of MealTableViewCell.")`
8. `}`
10. `// Fetches the appropriate meal for the data source layout.`
11. `let meal = meals[indexPath.row]`
13. `cell.nameLabel.text = meal.name`
14. `cell.photoImageView.image = meal.photo`
15. `cell.ratingControl.rating = meal.rating`
17. `return cell`
18. `}`

The final step to displaying data in the user interface is to connect the code defined in `MealTableViewController.swift` to the meal list scene.

__To point the Table View Controller to MealTableViewController.swift__

1. Open your storyboard.
2. Select the table view controller by clicking on its scene dock until the entire scene has a blue outline around it.

   （原归档配图未能恢复：`CTV_scenedock_table_2x.png`）
3. Open the Identity inspector （原归档配图未能恢复：`inspector_identity_2x.png`）.
4. In the Identity inspector, find the field labeled Class, and select `MealTableViewController`.

   （原归档配图未能恢复：`CTV_inspector_identity_tablevc_2x.png`）

_Checkpoint:_ Run your app. The list of items you added in the `viewDidLoad()` method should show up as cells in your table view. You’ll notice there’s a little bit of overlap between the table view cells and the status bar—you’ll fix that in the next lesson.

（原归档配图获取待重试：`CTV_sim_finalUI_2x.png`）

### Prepare the Meal Detail Scene for Navigation

As you prepare to implement navigation in the FoodTracker app, you need to delete and replace a few pieces of code and parts of the user interface that you won’t need anymore.

__To clean up unused pieces of the project__

1. Open your storyboard and look at the meal detail scene.

   （原归档配图获取待重试：`CTV_mealsceneUI_old_2x.png`）
2. In the meal detail scene, select the `Meal Name` label, and press the Delete key to delete it.

   The rest of the elements in the stack view reposition themselves appropriately.

   （原归档配图获取待重试：`CTV_mealsceneUI_new_2x.png`）
3. Open `ViewController.swift`.
4. In `ViewController.swift`, find the `textFieldDidEndEditing(_:)` method.

   1. `func textFieldDidEndEditing(_ textField: UITextField) {`
   2. `mealNameLabel.text = textField.text`
   3. `}`
5. Delete the line that sets the text property of the label.

   1. `mealNameLabel.text = textField.text`

   You’ll replace this with a new implementation soon.
6. In `ViewController.swift`, find the `mealNameLabel` outlet and delete it.

   1. `@IBOutlet weak var mealNameLabel: UILabel!`

Because you now have two view controllers in your project, it makes sense to give `ViewController.swift` a more meaningful name.

__To rename the ViewController.swift file__

1. In the project navigator, click the `ViewController.swift` file once and press the Return key.

   Xcode lets you type in a new name for the file.
2. Rename the file `MealViewController.swift`. Press Return.
3. In `MealViewController.swift`, find the class declaration line:

   1. `class ViewController: UIViewController, UITextFieldDelegate, UIImagePickerControllerDelegate, UINavigationControllerDelegate {`
4. Change the class name to `MealViewController`.

   1. `class MealViewController: UIViewController, UITextFieldDelegate, UIImagePickerControllerDelegate, UINavigationControllerDelegate {`
5. In the comment at the top of the file, also change the name from `ViewController.swift` to `MealViewController.swift`.
6. Open your storyboard.
7. Select the view controller by clicking on its scene dock.

   （原归档配图获取待重试：`CTV_scenedock_mealscene_2x.png`）
8. With the view controller selected, open the Identity inspector （原归档配图未能恢复：`inspector_identity_2x.png`）.
9. In the Identity inspector, change the Class field from `ViewController` to `MealViewController`.

   （原归档配图获取待重试：`CTV_mealscenefinal_2x.png`）

_Checkpoint_: Build or run your app. Everything should work as before.

### Wrapping Up

In this lesson, you built a custom table view cell. You attached your model object to your table view controller. You added sample data to the model, and you implemented the table view controller code needed to dynamically fill the table with the model data.

Next lesson, you’ll add the ability to navigate between the table and the meal view.

> [!NOTE]
>
> To see the completed sample project for this lesson, download the file and view it in Xcode.
>
> （原归档配图未能恢复：`WWDR_download_icon_withPadding_2x.png`）[Download File](https://developer.apple.com/sample-code/swift/downloads/06_CreateATableView.zip)

[Define Your Data Model](DefineYourDataModel.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmrqfvjvomi)

[Implement Navigation](ImplementNavigation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjwfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-12-08](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqojzfvjvomi)

[Next](ImplementNavigation.md)[Previous](DefineYourDataModel.md)
