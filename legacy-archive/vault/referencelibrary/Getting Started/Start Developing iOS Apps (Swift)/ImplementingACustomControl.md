---
title: Start Developing iOS Apps (Swift)
apple_id: TP40015214
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2016-12-08'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/DevelopiOSAppsSwift/ImplementingACustomControl.html
archived_at: '2026-07-27T06:57:09.812636Z'
---
> 导航：[总目录](../../../README.md) · [referencelibrary](../../../_indexes/referencelibrary.md) · [Start Developing iOS Apps (Swift)](index.md)


[Next](DefineYourDataModel.md)[Previous](WorkWithViewControllers.md)

## Implement a Custom Control

In this lesson, you’ll implement a custom rating control for the FoodTracker app, and add it to the scene.

（原归档配图获取待重试：`ICC_sim_finalUI_2x.png`）

### Learning Objectives

At the end of the lesson, you’ll be able to:

- Create and associate custom source code files with elements in a storyboard
- Define a custom class
- Implement an initializer on a custom class
- Use `UIStackView` as a container
- Understand how to create views programmatically
- Add accessibility information to a custom control
- Work with `@IBInspectable` and `@IBDesignable` to display and control a custom view in Interface Builder

### Create a Custom View

To be able to rate a meal, users need a [control](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjx) that lets them select the number of stars they want to assign to the meal. There are many ways to implement this, but this lesson focuses on a straightforward approach, building a custom control by combining existing views and controls. You’ll create a stack view subclass that manages a row of buttons representing the stars. You’ll define your custom control entirely in code, and then add it to your [storyboard](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvooa).

The rating control appears as a row of stars.

（原归档配图获取待重试：`ICC_ratingcontrol_2x.png`）

Users can choose a rating for a meal. When a user taps a star, that star and the stars preceding it are filled in. If the user taps the rightmost filled in star (the star associated with the current rating), the rating is cleared and all stars are displayed as empty.

To begin designing the [user interface (UI)](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjy), interaction, and behavior of this control, start by creating a custom stack view (`UIStackView`) [subclass](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomju).

__To create a subclass of UIStackView__

1. Choose File > New > File (or press Command-N).
2. At the top of the dialog that appears, select iOS.
3. Select Cocoa Touch Class, and click Next.
4. In the Class field, type `RatingControl`.
5. In the “Subclass of” field, select `UIStackView`.
6. Make sure the Language option is set to Swift.

   （原归档配图获取待重试：`ICC_newviewclass_2x.png`）
7. Click Next.

   The save location defaults to your project directory.

   The Group option defaults to your app name, FoodTracker.

   In the Targets section, your app is selected and the tests for your app are unselected.
8. Leave these defaults as they are, and click Create.

   Xcode creates a file that defines the `RatingControl` class: `RatingControl.swift`. `RatingControl` is a custom view subclass of `UIView`.
9. If necessary, in the Project navigator, drag the `RatingControl.swift` file so that it’s positioned under the other Swift files.

   （原归档配图获取待重试：`ICC_dragfile_2x.png`）
10. In `RatingControl.swift`, delete the comments that come with the template [implementation](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonbu) so you can start working with a blank slate.

    The implementation should look like this:

    1. `import UIKit`
    3. `class RatingControl: UIStackView {`
    5. `}`

You typically create a view in one of two ways: by programatically [initializing](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomq) the view, or by allowing the view to be loaded by the storyboard. There’s a corresponding initializer for each approach: `init(frame:)` for programatically initializing the view and `init?(coder:)` for loading the view from the storyboard. Recall that an [initializer](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomq) is a method that prepares an instance of a class for use, which involves setting an initial value for each property and performing any other setup.

You will need to implement both of these methods in your custom control. While designing the app, Interface Builder programatically instantiates the view when you add it to the canvas. At runtime, your app loads the view from the storyboard.

__To override the initializers__

1. In `RatingControl.swift`, under the `class` line, add this comment.

   1. `//MARK: Initialization`
2. Below the comment, start typing `init`. Stop typing when the code completion overlay shows up.

   （原归档配图获取待重试：`ICC_init_codecompletion_2x.png`）
3. Select `init(frame: CGRect)` from the listed options, and press Return.

   Xcode inserts the initializer skeleton for you.

   1. `init(frame: CGRect) {`
   3. `}`
4. Errors and warnings appear as yellow triangle icons (warnings) and red circles (errors) next to the code. Currently, the `init(frame:)` method has an error. Click on the error icon to bring up more information about the error.

   （原归档配图获取待重试：`ICC_init_fixit_2x.png`）
5. Double-click the Fix-it to insert the `override` keyword.

   1. `override init(frame: CGRect) {`
   3. `}`

   The Swift compiler knows that `init(frame:)` must be marked as required, and offers a fix-it to make this change in your code. [Fix-its](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvoojq) are provided by the compiler as potential solutions to errors in your code.
6. Add this line to call the superclass’s initializer:

   1. `super.init(frame: frame)`
7. Below the `init(frame:)` method, start typing `init` again, and select init(coder: NSCoder) from the code completion options. Press Return.

   Xcode inserts the initializer skeleton for you.

   1. `init(coder: NSCoder) {`
   3. `}`
8. Use the Fix-it to insert the `required` keyword.

   > [!NOTE]
   >
   > Swift handles initializers differently than other methods. If you don’t provide any initializers, Swift classes automatically inherit all of their super class’s designated initializers. If you implement any initializers, you not longer inherit any of the superclasses initializers; however, the superclass can mark one or more of its initializers as `required`. The subclass must implement (or automatically inherit) all of the required initializers. Furthermore, the subclass must mark their initializers as `required`, indicating that their subclasses must also implement the initializers.
9. Add this line to call the superclass’s initializer.

   1. `super.init(coder: coder)`

The initializers should look like this:

1. `override init(frame: CGRect) {`
2. `super.init(frame: frame)`
3. `}`
5. `required init(coder: NSCoder) {`
6. `super.init(coder: coder)`
7. `}`

Right now, your initializers are placeholders that simply call the superclass’s implementation. You will add additional configuration steps later in this lesson.

### Display the Custom View

To display your custom control, you need to add a stack view to your storyboard and establish a connection between the stack view and the code you just wrote.

__To display the view__

1. Open your storyboard.
2. In your storyboard, use the [Object library](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonju) to find a Horizontal Stack View object, and drag one into your storyboard scene so that it’s in the stack view below the image view.

   （原归档配图未能恢复：`ICC_addhorizontalstack_2x.png`）
3. With the horizontal stack view selected, open the Identity inspector （原归档配图未能恢复：`inspector_identity_2x.png`）.

   Recall that the [Identity inspector](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvoobq) lets you edit properties of an object in your storyboard related to that object’s identity, such as what class the object belongs to.

   （原归档配图获取待重试：`ICC_inspector_identity_2x.png`）
4. In the Identity inspector, find the field labeled Class and select `RatingControl`.

   （原归档配图获取待重试：`ICC_identity_ratingcontrol_2x.png`）

### Add Buttons to the View

At this point, you’ve got the basics of a custom `UIStackView` subclass, called `RatingControl`. Next, you need to add buttons to your view to allow the user to select a rating. Start with something simple, like getting a single red button to show up in your view.

__To create a button in your view__

Make sure the button is added, regardless of which initializer is called. To do this, add a private method, `setupButtons()`, and call that method from both initializers.

1. In `RatingControl.swift`, under the initializer methods, add this comment.

   1. `//MARK: Private Methods`

   Use the space below this comment to create private methods—methods with the `private` modifier before the `func` introducer. Private methods can only be called by code within the declaring class. This lets you encapsulate and protect methods, ensuring that they are not unexpectedly or accidentally called from the outside.
2. Under the comment, add the following method:

   1. `private func setupButtons() {`
   3. `}`
3. In the `setupButtons()` method, add the following lines of code to create a red button:

   1. `// Create the button`
   2. `let button = UIButton()`
   3. `button.backgroundColor = UIColor.red`

   Here, you are using one of the `UIButton` class’s convenience initializers. This initializer calls `init(frame:)` and passes in a zero-sized rectangle. Starting with a zero-sized button is fine, because you’re using Auto Layout. The stack view will automatically define the button’s position, and you will add constraints to define the button’s size.

   You are using `red` so it’s easy to see where the view is. If you’d like, use one of the other predefined `UIColor` values instead, like `blue` or `green`.
4. Below the last line, add the button’s constraints:

   1. `// Add constraints`
   2. `button.translatesAutoresizingMaskIntoConstraints = false`
   3. `button.heightAnchor.constraint(equalToConstant: 44.0).isActive = true`
   4. `button.widthAnchor.constraint(equalToConstant: 44.0).isActive = true`

   The first line of code disables the button’s automatically generated constraints. When you programmatically instantiate a view, its `translatesAutoresizingMaskIntoConstraints` property defaults to `true`. This tells the layout engine to create constraints that define the view’s size and position based on the view’s `frame` and `autoresizingmask` properties. Typically, when you are using Auto Layout, you want to replace these autogenerated constraints with your own. To remove the autogenerated constraints, set the `translatesAutoresizingMaskIntoConstraints` property to `false`.

   > [!NOTE]
   >
   > This line is not strictly necessary. When you add a view to a stack view, the stack view automatically sets the view’s `translatesAutoresizingMaskIntoConstraints` property to `false`. However, when using Auto Layout, it’s a good habit to explicitly disable the autogenerated constraints whenever you programmatically create a view. That way you won’t accidentally forget to disable them when it actually matters.

   The lines starting with `button.heightAnchor` and `button.widthAnchor` create the constraints that define the button’s height and width. Each line performs the following steps:

   1. The button’s `heightAnchor` and `widthAnchor` properties give access to layout anchors. You use layout anchors to create constraints—in this case, constraints that define the view’s height and width, respectively.
   2. The anchor’s `constraint(equalToConstant:)` method returns a constraint that defines a constant height or width for the view.
   3. The constraint’s `isActive` property activates or deactivates the constraint. When you set this property to `true`, the system adds the constraint to the correct view, and activates it.

   Together, these lines define the button as a fixed-size object in your layout (44 point x 44 point).
5. Finally, add the button to the stack:

   1. `// Add the button to the stack`
   2. `addArrangedSubview(button)`

   The `addArrangedSubview()` method adds the button you created to the list of views managed by the `RatingControl` stack view. This action adds the view as a subview of the `RatingControl`, and also instructs the `RatingControl` to create the constraints needed to manage the button’s position within the control.

Your `setupButtons()` method should look like this:

1. `private func setupButtons() {`
3. `// Create the button`
4. `let button = UIButton()`
5. `button.backgroundColor = UIColor.red`
7. `// Add constraints`
8. `button.translatesAutoresizingMaskIntoConstraints = false`
9. `button.heightAnchor.constraint(equalToConstant: 44.0).isActive = true`
10. `button.widthAnchor.constraint(equalToConstant: 44.0).isActive = true`
12. `// Add the button to the stack`
13. `addArrangedSubview(button)`
14. `}`

Now call this method from both initialization methods, as shown below:

1. `override init(frame: CGRect) {`
2. `super.init(frame: frame)`
3. `setupButtons()`
4. `}`
6. `required init(coder: NSCoder) {`
7. `super.init(coder: coder)`
8. `setupButtons()`
9. `}`

_Checkpoint_: Run your app. You should be able to see a view with a small red square inside of it. The red square is the button you added in the initializer.

（原归档配图获取待重试：`ICC_sim_1redbutton_2x.png`）

You need to add an action for this button (and for the other buttons you’ll be adding later). Eventually, you will use this button to change the meal’s rating; however, for now you’ll just check that the action is working.

__To add an action to the button__

1. In `RatingControl.swift`, after the `//MARK Initialization` section, add the following:

   1. `//MARK: Button Action`
2. Under the comment, add the following:

   1. `func ratingButtonTapped(button: UIButton) {`
   2. `print("Button pressed 👍")`
   3. `}`

   Use the `print()` function to check that the `ratingButtonTapped(_:)` action is linked to the button as expected. This function prints a message to the standard output, which in this case is the Xcode debug [console](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvoobw). The console is a useful debugging mechanism that appears at the bottom of the editor area.

   You’ll replace this debugging implementation with a real implementation in a little while.
3. Find the `setupButtons()` method:

   1. `private func setupButtons() {`
   3. `// Create the button`
   4. `let button = UIButton()`
   5. `button.backgroundColor = UIColor.red`
   7. `// Add constraints`
   8. `button.translatesAutoresizingMaskIntoConstraints = false`
   9. `button.heightAnchor.constraint(equalToConstant: 44.0).isActive = true`
   10. `button.widthAnchor.constraint(equalToConstant: 44.0).isActive = true`
   12. `// Add the button to the stack`
   13. `addArrangedSubview(button)`
   14. `}`
4. Just above the `// Add the button to the stack` comment, add the following code:

   1. `// Setup the button action`
   2. `button.addTarget(self, action: #selector(RatingControl.ratingButtonTapped(button:)), for: .touchUpInside)`

   In the previous lesson, you used the target-action pattern to link elements in your storyboard to action methods in your code. The `addTarget(_, action:, for:)` method does the same thing in code. You’re attaching the `ratingButtonTapped(_:)` action method to the `button` object, which will be triggered whenever the `.TouchDown` event occurs.

   There’s a lot going on in this code. Here’s a breakdown:

   - The target is `self`, which refers to the current instance of the enclosing class. In this case, it refers to the `RatingControl` object that is setting up the buttons.
   - The `#selector` expression returns the `Selector` value for the provided method. A selector is an opaque value that identifies the method. Older APIs used selectors to dynamically invoke methods at runtime. While newer APIs have largely replaced selectors with blocks, many methods—like `performSelector(_:)` and `addTarget(_:action:forControlEvents:)`—still take selectors as arguments. In this example, the `#selector(RatingControl.ratingButtonTapped(_:))` expression returns the selector for your `ratingButtonTapped(_:)` action method. This lets the system call your action method when the button is tapped.
   - The `UIControlEvents` option set defines a number of events that controls can respond to. Typically buttons respond to the `.touchUpInside` event. This occurs when the user touches the button, and then lifts their finger while the finger is still within the button’s bounds. This event has an advantage over `.touchDown`, because the user can cancel the event by dragging their finger outside the button before lifting it.
   - Note that because you’re not using Interface Builder, you don’t need to define your action method with the `IBAction` attribute; you just define the action like any other method. You can use a method that takes no arguments, that takes a single sender argument, or that takes both a sender and an event argument.

     1. `func doSomething()`
     2. `func doSomething(sender: UIButton)`
     3. `func doSomething(sender: UIButton, forEvent event: UIEvent)`

Your `setupButtons()` method should now look like this:

1. `private func setupButtons() {`
3. `// Create the button`
4. `let button = UIButton()`
5. `button.backgroundColor = UIColor.red`
7. `// Add constraints`
8. `button.translatesAutoresizingMaskIntoConstraints = false`
9. `button.heightAnchor.constraint(equalToConstant: 44.0).isActive = true`
10. `button.widthAnchor.constraint(equalToConstant: 44.0).isActive = true`
12. `// Setup the button action`
13. `button.addTarget(self, action: #selector(RatingControl.ratingButtonTapped(button:)), for: .touchUpInside)`
15. `// Add the button to the stack`
16. `addArrangedSubview(button)`
17. `}`

_Checkpoint_: Run your app. When you click the red square, you should see the “Button pressed” message in the console.

（原归档配图获取待重试：`ICC_console_buttonpressed_2x.png`）

Now it’s time to think about what pieces of information the `RatingControl` class needs to have in order to represent a rating. You’ll need to keep track of a rating value, as well as the buttons that a user taps to set that rating. You can represent the rating value with an `Int`, and the buttons as an array of `UIButton` objects.

__To add rating properties__

1. In `RatingControl.swift`, find the class declaration line:

   1. `class RatingControl: UIView {`
2. Below this line, add the following code:

   1. `//MARK: Properties`
   2. `private var ratingButtons = [UIButton]()`
   4. `var rating = 0`

   This creates two properties. The first is a property that contains the list of buttons. You don’t want to let anything outside the `RatingControl` class access these buttons; therefore, you declare them as private.

   The Second property contains the control’s rating. You need to be able to both read and write this value from outside this class. By leaving it as internal access (the default), you can access it from any other class inside the app.

Right now, you have one button in the view, but you need five total. To create a total of five buttons, use a `for`-`in` loop. A `for`-`in` loop iterates over a sequence, such as ranges of numbers, to execute a set of code multiple times. Instead of creating one button, the loop will create five.

__To create a total of five buttons__

1. In `RatingControl.swift`, find the `setupButtons()` method, and add a `for`-`in` loop around the method’s contents, like this:

   1. `for _ in 0..<5 {`
   2. `// Create the button`
   3. `let button = UIButton()`
   4. `button.backgroundColor = UIColor.red`
   6. `// Add constraints`
   7. `button.translatesAutoresizingMaskIntoConstraints = false`
   8. `button.heightAnchor.constraint(equalToConstant: 44.0).isActive = true`
   9. `button.widthAnchor.constraint(equalToConstant: 44.0).isActive = true`
   11. `// Setup the button action`
   12. `button.addTarget(self, action: #selector(RatingControl.ratingButtonTapped(button:)), for: .touchUpInside)`
   14. `// Add the button to the stack`
   15. `addArrangedSubview(button)`
   16. `}`

   Make sure the lines in the `for`-`in` loop are indented properly by selecting all of them and pressing Control-I.

   The [half-open range operator](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvooju) (`..<`) doesn’t include the upper number, so this range goes from `0` to `4` for a total of five loop iterations, drawing five buttons instead of just one. The underscore (`_`) represents a wildcard, which you can use when you don’t need to know which iteration of the loop is currently executing.
2. Add the following just above the for-in loop’s closing curly brace (}).

   1. `// Add the new button to the rating button array`
   2. `ratingButtons.append(button)`

   As you create each button, you add it to the `ratingButtons` array to keep track of it.

Your `setupButtons()` method should now look like this:

1. `private func setupButtons() {`
3. `for _ in 0..<5 {`
4. `// Create the button`
5. `let button = UIButton()`
6. `button.backgroundColor = UIColor.red`
8. `// Add constraints`
9. `button.translatesAutoresizingMaskIntoConstraints = false`
10. `button.heightAnchor.constraint(equalToConstant: 44.0).isActive = true`
11. `button.widthAnchor.constraint(equalToConstant: 44.0).isActive = true`
13. `// Setup the button action`
14. `button.addTarget(self, action: #selector(RatingControl.ratingButtonTapped(button:)), for: .touchUpInside)`
16. `// Add the button to the stack`
17. `addArrangedSubview(button)`
19. `// Add the new button to the rating button array`
20. `ratingButtons.append(button)`
21. `}`
22. `}`

_Checkpoint_: Run your app. Notice how the stack view lays out the buttons. They are arranged horizontally, but there’s no space between them—making them look like a single, red block.

（原归档配图获取待重试：`ICC_buttonswithoutspace_2x.png`）

To fix this, open `Main.storyboard` and select the `RatingControl` stack view. Open the [Attributes inspector](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjz) （原归档配图未能恢复：`inspector_attributes_2x.png`）, and set the Spacing attribute to `8`.

（原归档配图获取待重试：`ICC_setstackspacing_2x.png`）

_Checkpoint_: Run your app again. Now, the buttons should be laid out as expected. Note, clicking any of the buttons at this point should still call the `ratingButtonTapped(button:)` method and log the message to the console.

（原归档配图获取待重试：`ICC_sim_5redbuttons_2x.png`）

To collapse the console, use the Debug area toggle.

（原归档配图获取待重试：`debug_toggle_2x.png`）

### Add Support for Interface Builder

If you look at the rating control in Interface Builder, you’ll notice that it’s displayed as a large, empty rectangle. Worse yet, if you select the rating control, its bounding box turns red, indicating that there’s a problem with the control’s layout. In fact, there are two other indications that something might be wrong. There’s a yellow warning triangle in the right side of the Activity viewer. There’s also a red error icon beside the View Controller Scene in the Outline view.

（原归档配图获取待重试：`ICC_errorsandwarnings_2x.png`）

If you click these icons, Xcode shows additional information about the errors and warnings.

（原归档配图获取待重试：`ICC_ambiguouslayoutwarning_2x.png`）

（原归档配图获取待重试：`ICC_missingconstrainterror_2x.png`）

In both cases, the root cause is the same. Interface Builder does not know anything about the contents of your rating control. To fix this, you define the control as `@IBDesignable`. This lets Interface Builder instantiate and draw a copy of your control directly in the canvas. Additionally, now that Interface Builder has a live copy of your control, its layout engine can properly position and size the control.

__To declare the control as @IBDesignable__

1. In `RatingControl.swift`, find the class declaration:

   1. `class RatingControl: UIStackView {`
2. Add `@IBDesignable` to the beginning of the line as shown:

   1. `@IBDesignable class RatingControl: UIStackView {`
3. Rebuild the project by typing Command-B (or choosing Product > Build).
4. Open `Main.storyboard`. Once the build completes, the storyboard shows a live view of your rating control.

   （原归档配图获取待重试：`ICC_designableliveview_2x.png`）

   Notice that the canvas now correctly sizes and places your `RatingControl` view. As a result, the warnings and errors are now gone.

Interface Builder can do more than just display your custom view. You can also specify properties that can then be set in the Attributes inspector. Add the `@IBInspectable` attribute to the desired properties. Interface Builder supports the inspection of basic types (and their corresponding optionals), including: Booleans, numbers, strings, as well as `CGRect`, `CGSize`, `CGPoint`, and `UIColor`.

__To add inspectable properties__

1. In `RatingControl.swift`, add the following properties to the bottom of the `//MARK: Properties` section:

   1. `@IBInspectable var starSize: CGSize = CGSize(width: 44.0, height: 44.0)`
   2. `@IBInspectable var starCount: Int = 5`

   These lines define the size of your buttons and the number of buttons in your control.
2. Now you need to use these values. Locate the `setupButtons()` method, and make the following changes:

   1. In the `for`-`in` declaration, change `5` to `starCount`.
   2. In the `button.heightAnchor.constraint()` method call, change `44.0` to `starSize.height`.
   3. In the `button.widthAnchor.constraint()` method call, change `44.0` to `starSize.width`.

   The method should appear as shown below:

   1. `private func setupButtons() {`
   3. `for _ in 0..<starCount {`
   4. `// Create the button`
   5. `let button = UIButton()`
   6. `button.backgroundColor = UIColor.red`
   8. `// Add constraints`
   9. `button.translatesAutoresizingMaskIntoConstraints = false`
   10. `button.heightAnchor.constraint(equalToConstant: starSize.height).isActive = true`
   11. `button.widthAnchor.constraint(equalToConstant: starSize.width).isActive = true`
   13. `// Setup the button action`
   14. `button.addTarget(self, action: #selector(RatingControl.ratingButtonTapped(button:)), for: .touchUpInside)`
   16. `// Add the button to the stack`
   17. `addArrangedSubview(button)`
   19. `// Add the new button to the rating button array`
   20. `ratingButtons.append(button)`
   21. `}`
   22. `}`

   If you switch to the `Main.storyboard` and select the `RatingControl`, you’ll see the Star Size and Star Count settings in the Attributes inspector. The dashes indicate that the control is currently using the default values (in this case 44.0 points and 5 stars). However, changing these values does not yet change the control.

   （原归档配图获取待重试：`ICC_inspectableattributes_2x.png`）
3. To update the control, you need to reset the control’s buttons every time these attributes change. To do that, add a property observer to each property. A [property observer](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjsgm) observes and responds to changes in a property’s value. Property observers are called every time a property’s value is set, and can be used to perform work immediately before or after the value changes.

   In `RatingControl.swift`, modify the inspectable properties as shown below:

   1. `@IBInspectable var starSize: CGSize = CGSize(width: 44.0, height: 44.0) {`
   2. `didSet {`
   3. `setupButtons()`
   4. `}`
   5. `}`
   7. `@IBInspectable var starCount: Int = 5 {`
   8. `didSet {`
   9. `setupButtons()`
   10. `}`
   11. `}`

   Here, you define property observers for the `starSize` and `starCount` properties. Specifically, the `didSet` property observer is called immediately after the property’s value is set. Your implementation then calls the `setupButtons()` method. This method adds new buttons using the updated size and count; however, the current implementation doesn’t get rid of the old buttons.
4. To clear out the old buttons, add the following code to the beginning of the `setupButtons()` method.

   1. `// clear any existing buttons`
   2. `for button in ratingButtons {`
   3. `removeArrangedSubview(button)`
   4. `button.removeFromSuperview()`
   5. `}`
   6. `ratingButtons.removeAll()`

   This code iterates over all of the rating control’s buttons. First, it removes the button from the list of views managed by the stack view. This tells the stack view that it should no longer calculate the button’s size and position—but the button is still a subview of the stack view. Next, the code removes the button from the stack view entirely. Finally, once all the buttons have been removed, it clears the `ratingButtons` array.

   The `setupButtons()` method should now appear as shown below:

   1. `private func setupButtons() {`
   3. `// clear any existing buttons`
   4. `for button in ratingButtons {`
   5. `removeArrangedSubview(button)`
   6. `button.removeFromSuperview()`
   7. `}`
   8. `ratingButtons.removeAll()`
   10. `for _ in 0..<starCount {`
   11. `// Create the button`
   12. `let button = UIButton()`
   13. `button.backgroundColor = UIColor.red`
   15. `// Add constraints`
   16. `button.translatesAutoresizingMaskIntoConstraints = false`
   17. `button.heightAnchor.constraint(equalToConstant: starSize.height).isActive = true`
   18. `button.widthAnchor.constraint(equalToConstant: starSize.width).isActive = true`
   20. `// Setup the button action`
   21. `button.addTarget(self, action: #selector(RatingControl.ratingButtonTapped(button:)), for: .touchUpInside)`
   23. `// Add the button to the stack`
   24. `addArrangedSubview(button)`
   26. `// Add the new button to the rating button array`
   27. `ratingButtons.append(button)`
   28. `}`
   29. `}`
   > [!NOTE]
   >
   > Ripping out and replacing all of the buttons is not necessarily the best idea from a performance standpoint. However, the `didSet` observers should only be called by Interface Builder at design time. When the app is running, the `setupButtons()` method is only called once, when the control is first loaded from the storyboard. Therefore, there’s no need to create a more-complex solution to update the existing buttons in place.

_Checkpoint_: Open `Main.storyboard` and select the `RatingControl` object. Try changing the Star Size and Star Count attributes. The control in the canvas should change to match the new settings. Run the app, and you should see the changes in the simulator.

（原归档配图获取待重试：`ICC_modifyinginspectableproperties_2x.png`）

Be sure to reset these settings to their default values when you are done testing them.

> [!NOTE]
>
> For more information on working with custom views, see Lay out user interfaces > Add objects and media > Render custom views in Xcode help.

### Add Star Images to the Buttons

Next, you’ll add images of an empty, filled, and highlighted star to the buttons.

（原归档配图获取待重试：`ICC_emptyStar_2x.png`）

（原归档配图获取待重试：`ICC_filledStar_2x.png`）

（原归档配图获取待重试：`ICC_highlightedStar_2x.png`）

You can find the star images used in this lesson in the `Images/` folder of the complete project file at the end of this lesson, or use your own images. (Make sure the names of the images you use match the image names in the code later.)

__To add images to your project__

1. In the [project navigator](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjx), select `Assets.xcassets` to view the asset catalog.

   Recall that the [asset catalog](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonrz) is a place to store and organize your image assets for an app.
2. In the bottom left corner, click the plus (`+`) button and choose New Folder from the pop-up menu.

   （原归档配图获取待重试：`ICC_assetcatalog_addfolder_2x.png`）
3. Double-click the folder name and rename it `Rating Images`.
4. With the folder selected, in the bottom left corner, click the plus (`+`) button and choose New Image Set from the pop-up menu.

   An image set represents a single image asset, but can contain different versions of the image to display at different screen resolutions.
5. Double-click the image set name and rename it `emptyStar`.
6. On your computer, select the empty star image you want to add.
7. Drag and drop the image into the `2x` slot in the image set.

   （原归档配图获取待重试：`ICC_emptystar_drag_2x.png`）

   `2x` is the display resolution for iPhone 7 Simulator that you’re using in these lessons, so the image will look best at this resolution.
8. In the bottom left corner, click the plus (`+`) button and choose New Image Set from the pop-up menu.
9. Double-click the image set name and rename it `filledStar`.
10. On your computer, select the filled-in star image you want to add.
11. Drag and drop the image into the `2x` slot in the image set.

    （原归档配图获取待重试：`ICC_filledstar_drag_2x.png`）
12. In the bottom left corner, click the plus (`+`) button and choose New Image Set from the pop-up menu.
13. Double-click the image set name and rename it `highlightedStar`.
14. On your computer, select the filled-in star image you want to add.
15. Drag and drop the image into the `2x` slot in the image set.

    （原归档配图获取待重试：`ICC_highlightedstar_drag_2x.png`）

Your Rating images folder should now contain all three star images.

（原归档配图获取待重试：`ICC_assetcatalog_final_2x.png`）

Next, write the code to set the appropriate image for a button at the right time.

__To set star images for the buttons__

1. In `RatingControl.swift`, navigate to the `setupButtons()` method, and add this code just above the `for`-`in` loop that creates the buttons:

   1. `// Load Button Images`
   2. `let bundle = Bundle(for: type(of: self))`
   3. `let filledStar = UIImage(named: "filledStar", in: bundle, compatibleWith: self.traitCollection)`
   4. `let emptyStar = UIImage(named:"emptyStar", in: bundle, compatibleWith: self.traitCollection)`
   5. `let highlightedStar = UIImage(named:"highlightedStar", in: bundle, compatibleWith: self.traitCollection)`

   These lines load the star images from the assets catalog. Note that the assets catalog is located in the app’s main bundle. This means that the app can load the images using the shorter `UIImage(named:)` method. However, because the control is `@IBDesignable`, the setup code also needs to run in Interface Builder. For the images to load properly in Interface Builder, you must explicitly specify the catalog’s bundle. This ensures that the system can find and load the image.
2. Find the line that sets the background color (`button.backgroundColor = UIColor.redColor()`) and replace it with the following:

   1. `// Set the button images`
   2. `button.setImage(emptyStar, for: .normal)`
   3. `button.setImage(filledStar, for: .selected)`
   4. `button.setImage(highlightedStar, for: .highlighted)`
   5. `button.setImage(highlightedStar, for: [.highlighted, .selected])`

   Buttons have five different states: normal, highlighted, focused, selected, and disabled. By default, the button modifies its appearance based on its state, for example a disabled button appears grayed out. A button can be in more than one state at the same time, such as when a button is both disabled and highlighted.

   Buttons always start in the normal state (not highlighted, selected, focused, or disabled). A button is highlighted whenever the user touches it. You can also programmatically set a button to be selected or disabled. The focused state is used by focus-based interfaces, like Apple TV.

   In the code above, you are telling the button to use the empty star image for the normal state. This is the button’s default image. The system uses this image (possibly with an added effect) whenever a state or combination of states doesn’t have an image of their own.

   Next, the code above sets the filled image for the selected state. If you programmatically set the button as selected, it will change from the empty star to the filled star.

   Finally, you set the highlighted image for both the highlighted and the selected and highlighted states. When the user touches the button, whether or not it is selected, the system will show the highlighted button image.

Your `setupButtons()` method should look like this:

1. `private func setupButtons() {`
3. `// Clear any existing buttons`
4. `for button in ratingButtons {`
5. `removeArrangedSubview(button)`
6. `button.removeFromSuperview()`
7. `}`
8. `ratingButtons.removeAll()`
10. `// Load Button Images`
11. `let bundle = Bundle(for: type(of: self))`
12. `let filledStar = UIImage(named: "filledStar", in: bundle, compatibleWith: self.traitCollection)`
13. `let emptyStar = UIImage(named:"emptyStar", in: bundle, compatibleWith: self.traitCollection)`
14. `let highlightedStar = UIImage(named:"highlightedStar", in: bundle, compatibleWith: self.traitCollection)`
16. `for _ in 0..<starCount {`
17. `// Create the button`
18. `let button = UIButton()`
20. `// Set the button images`
21. `button.setImage(emptyStar, for: .normal)`
22. `button.setImage(filledStar, for: .selected)`
23. `button.setImage(highlightedStar, for: .highlighted)`
24. `button.setImage(highlightedStar, for: [.highlighted, .selected])`
26. `// Add constraints`
27. `button.translatesAutoresizingMaskIntoConstraints = false`
28. `button.heightAnchor.constraint(equalToConstant: starSize.height).isActive = true`
29. `button.widthAnchor.constraint(equalToConstant: starSize.width).isActive = true`
31. `// Setup the button action`
32. `button.addTarget(self, action: #selector(RatingControl.ratingButtonTapped(button:)), for: .touchUpInside)`
34. `// Add the button to the stack`
35. `addArrangedSubview(button)`
37. `// Add the new button to the rating button array`
38. `ratingButtons.append(button)`
39. `}`
40. `}`

_Checkpoint_: Run your app. You should see stars instead of red buttons. Tapping any of the buttons at this point should still call `ratingButtonTapped(_:)` and log the message to the console. You’ll even see the blue highlighted star while you are touching the button, but your buttons don’t change to the filled images yet. You’ll fix that next.

（原归档配图获取待重试：`ICC_sim_emptystars_2x.png`）

### Implement the Button Action

The user needs to be able to select a rating by tapping a star, so you’ll replace the debugging implementation with a real implementation of the `ratingButtonTapped(_:)` method.

__To implement the rating action__

1. In `RatingControl.swift`, find the `ratingButtonTapped(button:)` method:

   1. `func ratingButtonTapped(button: UIButton) {`
   2. `print("Button pressed 👍")`
   3. `}`
2. Replace the `print` statement with this code:

   1. `func ratingButtonTapped(button: UIButton) {`
   2. `guard let index = ratingButtons.index(of: button) else {`
   3. `fatalError("The button, \(button), is not in the ratingButtons array: \(ratingButtons)")`
   4. `}`
   6. `// Calculate the rating of the selected button`
   7. `let selectedRating = index + 1`
   9. `if selectedRating == rating {`
   10. `// If the selected star represents the current rating, reset the rating to 0.`
   11. `rating = 0`
   12. `} else {`
   13. `// Otherwise set the rating to the selected star`
   14. `rating = selectedRating`
   15. `}`
   16. `}`

   In the code above, the `indexOf(_:)` method attempts to find the selected button in the array of buttons and to return the index at which it was found. This method returns an optional `Int` because the instance you’re searching for might not exist in the collection you’re searching. However, because the only buttons that trigger this action are the ones you created and added to the array, if the `indexOf(_:)` method cannot find a matching button, you have a serious bug in your code. Throwing a fatal error here terminates the app and prints a useful error message to the console, helping you find and fix any problems while you design and test your app.

   Once you have the button’s index (in this case a value from 0 to 4), you add 1 to the index to calculate the selected rating (giving you a value from 1 to 5). If the user tapped the star that corresponds with the current rating, you reset the control’s `rating` property to 0. Otherwise, you set the `rating` to the selected rating.
3. Once the rating is set, you need some way to update the button’s appearance. In `RatingControl.swift`, before the last curly brace (`}`), add the following method:

   1. `private func updateButtonSelectionStates() {`
   2. `}`

   This is a helper method that you’ll use to update the selection state of the buttons.
4. In the `updateButtonSelectionStates()` method, add the following `for`-`in` loop:

   1. `private func updateButtonSelectionStates() {`
   2. `for (index, button) in ratingButtons.enumerated() {`
   3. `// If the index of a button is less than the rating, that button should be selected.`
   4. `button.isSelected = index < rating`
   5. `}`
   6. `}`

   This code iterates through the buttons and sets each one’s selected state based on its position and the rating. As you saw earlier, the selected state affects the button’s appearance. If the button’s index is less than the rating, the `isSelected` property is set to `true`, and the button displays the filled-in star image. Otherwise, the `isSelected` property is set to `false`, and the button shows the empty star image.
5. Add a property observer to the `rating` property, and have it call the `updateButtonSelectionStates()` method whenever the rating changes.

   1. `var rating = 0 {`
   2. `didSet {`
   3. `updateButtonSelectionStates()`
   4. `}`
   5. `}`
6. You also need to update the button’s selection state whenever buttons are added to the control. In the `setupButtons()` method, add a call to the `updateButtonSelectionStates()` method just above the method’s closing curly brace (`}`). The `setupButtons()` method should now look as shown below:

   1. `private func setupButtons() {`
   3. `// Clear any existing buttons`
   4. `for button in ratingButtons {`
   5. `removeArrangedSubview(button)`
   6. `button.removeFromSuperview()`
   7. `}`
   8. `ratingButtons.removeAll()`
   10. `// Load Button Images`
   11. `let bundle = Bundle(for: type(of: self))`
   12. `let filledStar = UIImage(named: "filledStar", in: bundle, compatibleWith: self.traitCollection)`
   13. `let emptyStar = UIImage(named:"emptyStar", in: bundle, compatibleWith: self.traitCollection)`
   14. `let highlightedStar = UIImage(named:"highlightedStar", in: bundle, compatibleWith: self.traitCollection)`
   16. `for index in 0..<starCount {`
   17. `// Create the button`
   18. `let button = UIButton()`
   20. `// Set the button images`
   21. `button.setImage(emptyStar, for: .normal)`
   22. `button.setImage(filledStar, for: .selected)`
   23. `button.setImage(highlightedStar, for: .highlighted)`
   24. `button.setImage(highlightedStar, for: [.highlighted, .selected])`
   26. `// Add constraints`
   27. `button.translatesAutoresizingMaskIntoConstraints = false`
   28. `button.heightAnchor.constraint(equalToConstant: starSize.height).isActive = true`
   29. `button.widthAnchor.constraint(equalToConstant: starSize.width).isActive = true`
   31. `// Setup the button action`
   32. `button.addTarget(self, action: #selector(RatingControl.ratingButtonTapped(button:)), for: .touchUpInside)`
   34. `// Add the button to the stack`
   35. `addArrangedSubview(button)`
   37. `// Add the new button to the rating button array`
   38. `ratingButtons.append(button)`
   39. `}`
   41. `updateButtonSelectionStates()`
   42. `}`

_Checkpoint_: Run your app. You should see five stars and be able to click one to change the rating. Click the third star to change the rating to 3, for example. Click the same star a second time. The control should reset to a zero-star rating.

（原归档配图未能恢复：`ICC_sim_filledstars_2x.png`）

### Add Accessibility Information

With iOS built-in accessibility features, you can deliver an outstanding mobile experience to every customer, including those with special needs. These features include VoiceOver, Switch Control, playback of closed captioned or audio described video, Guided Access, Text to Speech, and more.

In most cases, users benefit from these features without any additional work on your part. VoiceOver, however, often requires a little attention. VoiceOver is a revolutionary screen reader for blind and low vision users. VoiceOver reads your user interface to the user. Although the default description of built-in controls provides a good starting point, you may need to optimize the presentation of your user interface, especially for custom views and controls.

For the rating control, you need to provide three additional pieces of information for each button,

- __Accessibility label.__ A short, localized word or phrase that succinctly describes the control or view, but does not identify the element’s type. Examples are “Add” or “Play.”
- __Accessibility value.__ The current value of an element, when the value is not represented by the label. For example, the label for a slider might be “Speed,” but its current value might be “50%.”
- __Accessibility hint.__ A brief, localized phrase that describes the results of an action on an element. Examples are “Adds a title” or “Opens the shopping list.”

In the rating control, each button’s accessibility label describes the value that the button sets. For example, the first button’s label says “Set 1 star rating.” The accessibility value contains the control’s current rating. For example, if you have a 4-star rating, the value says “4 stars set.” Finally, you assign a hint to the currently selected star that says, “Tap to reset the rating to zero.” All the other stars have a `nil`-valued hint, because their effects are already adequately described by their labels.

__To add accessibility labels, values, and hints__

1. In `RatingControl.swift`, navigate to the `setupButtons()` method. find the `for`-`in` declaration. Replace the placeholder loop variable (`_`) with `index` as shown:

   1. `for index in 0..<starCount {`
2. Inside the `for`-`in` loop, just after the constraints, add the following code:

   1. `// Set the accessibility label`
   2. `button.accessibilityLabel = "Set \(index + 1) star rating"`

   This code calculates a label string using the button’s index, then assigns it to the button’s `accessibilityLabel` property.

   The `setupButtons()` method should now look like this:

   1. `private func setupButtons() {`
   3. `// Clear any existing buttons`
   4. `for button in ratingButtons {`
   5. `removeArrangedSubview(button)`
   6. `button.removeFromSuperview()`
   7. `}`
   8. `ratingButtons.removeAll()`
   10. `// Load Button Images`
   11. `let bundle = Bundle(for: type(of: self))`
   12. `let filledStar = UIImage(named: "filledStar", in: bundle, compatibleWith: self.traitCollection)`
   13. `let emptyStar = UIImage(named:"emptyStar", in: bundle, compatibleWith: self.traitCollection)`
   14. `let highlightedStar = UIImage(named:"highlightedStar", in: bundle, compatibleWith: self.traitCollection)`
   16. `for index in 0..<starCount {`
   17. `// Create the button`
   18. `let button = UIButton()`
   20. `// Set the button images`
   21. `button.setImage(emptyStar, for: .normal)`
   22. `button.setImage(filledStar, for: .selected)`
   23. `button.setImage(highlightedStar, for: .highlighted)`
   24. `button.setImage(highlightedStar, for: [.highlighted, .selected])`
   26. `// Add constraints`
   27. `button.translatesAutoresizingMaskIntoConstraints = false`
   28. `button.heightAnchor.constraint(equalToConstant: starSize.height).isActive = true`
   29. `button.widthAnchor.constraint(equalToConstant: starSize.width).isActive = true`
   31. `// Set the accessibility label`
   32. `button.accessibilityLabel = "Set \(index + 1) star rating"`
   34. `// Setup the button action`
   35. `button.addTarget(self, action: #selector(RatingControl.ratingButtonTapped(button:)), for: .touchUpInside)`
   37. `// Add the button to the stack`
   38. `addArrangedSubview(button)`
   40. `// Add the new button to the rating button array`
   41. `ratingButtons.append(button)`
   42. `}`
   44. `updateButtonSelectionStates()`
   45. `}`
3. Navigate to the updateButtonSelectionStates() method. Inside the `for`-`in` loop, add the following code just after the line that sets the button’s `isSelected` property.

   1. `// Set the hint string for the currently selected star`
   2. `let hintString: String?`
   3. `if rating == index + 1 {`
   4. `hintString = "Tap to reset the rating to zero."`
   5. `} else {`
   6. `hintString = nil`
   7. `}`
   9. `// Calculate the value string`
   10. `let valueString: String`
   11. `switch (rating) {`
   12. `case 0:`
   13. `valueString = "No rating set."`
   14. `case 1:`
   15. `valueString = "1 star set."`
   16. `default:`
   17. `valueString = "\(rating) stars set."`
   18. `}`
   20. `// Assign the hint string and value string`
   21. `button.accessibilityHint = hintString`
   22. `button.accessibilityValue = valueString`

   Here, you start by checking whether the button is the currently selected button. If it is, you assign a hint. If not, you set the button’s `hintString` property to `nil`.

   Next, you calculate the value based on the control’s rating. Use a `switch` statement to assign custom strings if the `rating` is `0` or `1`. If the rating is greater than `1`, you calculate the hint using string interpolation.

   Finally, assign these values to the `accessibilityHint` and `accessibilityValue` properties.

When the user runs your app with VoiceOver enabled, when they touch one of the buttons, VoiceOver reads the button’s label, followed by the word _button_. Then it reads the accessibility value. Finally, it reads the accessibility hint (if any). This lets the user know both the control’s current value and the result of tapping the currently selected button.

> [!NOTE]
>
> For more information on accessibility, see [Accessibility on iOS](https://developer.apple.com/accessibility/ios/).
>
> Also, for the purpose of this lesson, you assigned simple strings to the accessibility properties; however, a production app should use localized strings. For more information on internationalization and localization, see [Build Apps for the World](https://developer.apple.com/internationalization/).

### Connect the Rating Control to the View Controller

The last thing you need to do to set up the rating control is to give the `ViewController` class a reference to it.

__To connect a rating control outlet to ViewController.swift__

1. Open your storyboard.
2. Click the Assistant button in the Xcode toolbar to open the [assistant editor](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonzw).

   （原归档配图未能恢复：`assistant_editor_toggle_2x.png`）
3. If you want more space to work, collapse the [project navigator](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjx) and [utility area](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonzs) by clicking the Navigator and Utilities buttons in the Xcode toolbar.

   （原归档配图未能恢复：`navigator_utilities_toggle_on_2x.png`）

   You can also collapse the outline view.
4. Select the rating control.

   `ViewController.swift` displays in the editor on the right. (If it doesn’t, choose Automatic > ViewController.swift in the editor selector bar.)
5. Control-drag from the rating control on your canvas to the code display in the editor on the right, stopping the drag at the line below the `photoImageView` property in `ViewController.swift`.

   （原归档配图获取待重试：`ICC_ratingcontrol_dragoutlet_2x.png`）
6. In the dialog that appears, for Name, type `ratingControl`. Leave the rest of the options as they are.

   （原归档配图获取待重试：`ICC_ratingcontrol_addoutlet_2x.png`）
7. Click Connect.

The `ViewController` class now has a reference to the rating control in the storyboard.

### Clean Up the Project

You’re close to finalizing the meal scene’s user interface, but first you need to do some cleanup. Now that the FoodTracker app is implementing more advanced behavior and a different user interface than in the previous lessons, you’ll want to remove the pieces you don’t need. You’ll also center the elements in your stack view to balance the user interface.

__To clean up the UI__

1. Return to the standard editor by clicking the Standard button.

   （原归档配图未能恢复：`standard_toggle_2x.png`）

   Expand the project navigator and utility area by clicking the Navigator and Utilities buttons in the Xcode toolbar.
2. Open your storyboard.
3. Select the Set Default Label Text button, and press the Delete key to delete it.

   The stack view rearranges your user interface elements to fill the gap that the button left.

   （原归档配图获取待重试：`ICC_deletebutton_2x.png`）
4. If necessary, open the outline view. Select the Stack View object.

   （原归档配图未能恢复：`ICC_outlineview_2x.png`）
5. Open the [Attributes inspector](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjz) （原归档配图未能恢复：`inspector_attributes_2x.png`）.
6. In the Attributes inspector, find the Alignment field and select Center.

   （原归档配图获取待重试：`ICC_centerstack_2x.png`）

Now, remove the action method that corresponds with the button you deleted.

__To clean up the code__

1. Open `ViewController.swift`.
2. In `ViewController.swift`, delete the `setDefaultLabelText(_:)` action method.

   1. `@IBAction func setDefaultLabelText(sender: UIButton) {`
   2. `mealNameLabel.text = "Default Text"`
   3. `}`

   That’s all you need to delete for now. You’ll make a change to the label outlet (`mealNameLabel`) in a later lesson.

_Checkpoint_: Run your app. Everything should work exactly as before, but the Set Default Label Text button is gone, and the elements are centered horizontally. The buttons should be side-by-side. Clicking any of the buttons at this point should still call `ratingButtonTapped(_:)` and change the button images appropriately.

> [!IMPORTANT]
>
> If you’re running into build issues, try pressing Command-Shift-K to [clean](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjqg4) your project.

（原归档配图获取待重试：`ICC_sim_finalUI_2x.png`）

### Wrapping Up

In this lesson, you learned how to build a custom control that can be displayed in Interface Builder. The control also exposes properties that can be modified in the Attributes inspector. Finally, you added accessibility information, ensuring that the control works well with Voice Over.

Next, you will design and connect the app’s data model.

> [!NOTE]
>
> To see the completed sample project for this lesson, download the file and view it in Xcode.
>
> （原归档配图未能恢复：`WWDR_download_icon_withPadding_2x.png`）[Download File](https://developer.apple.com/sample-code/swift/downloads/04_ImplementACustomControl.zip)

[Work with View Controllers](WorkWithViewControllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqnrnknltc)

[Define Your Data Model](DefineYourDataModel.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmrqfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-12-08](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqojzfvjvomi)

[Next](DefineYourDataModel.md)[Previous](WorkWithViewControllers.md)
