---
title: Start Developing iOS Apps (Swift)
apple_id: TP40015214
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2016-12-08'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/DevelopiOSAppsSwift/ConnectTheUIToCode.html
archived_at: '2026-07-27T06:57:09.598706Z'
---
> 导航：[总目录](../../../README.md) · [referencelibrary](../../../_indexes/referencelibrary.md) · [Start Developing iOS Apps (Swift)](index.md)


[Next](WorkWithViewControllers.md)[Previous](BuildABasicUI.md)

## Connect the UI to Code

In this lesson, you’ll connect the basic [user interface (UI)](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjy) of the FoodTracker app to code and define some actions a user can perform in that UI.

（原归档配图未能恢复：`CUIC_sim_finalUI_2x.png`）

### Learning Objectives

At the end of the lesson, you’ll be able to:

- Explain the relationship between a scene in a storyboard and the underlying view controller
- Create outlet and action connections between UI elements in a storyboard and source code
- Process user input from a text field and display the result in the UI
- Make a class conform to a protocol
- Understand the delegation pattern
- Follow the target-action pattern when designing app architecture

### Connect the UI to Source Code

Elements in a [storyboard](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvooa) are linked to source code. It’s important to understand the relationship that a storyboard has to the code you write.

In a storyboard, a [scene](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonrs) represents one screen of content and typically one view controller. [View controllers](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvony) implement your app’s behavior. A view controller manages a single content view with its hierarchy of subviews. View controllers coordinate the flow of information between the app’s [data model](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomzv), which encapsulates the app’s data, and the views that display that data, manage the life cycle of their content views, handle orientation changes when the device is rotated, define the navigation within your app, and implement the behavior to respond to user input. All view controller objects in iOS are of type `UIViewController` or one of its subclasses.

You define the behavior of your view controllers in code by creating and implementing custom view controller [subclasses](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomju). You can then create a connection between those classes and scenes in your storyboard to get the behavior you defined in code and the user interface you defined in your storyboard.

Xcode already created one such class that you looked at earlier, `ViewController.swift`, and connected it to the scene you’re working on in your storyboard right now. In the future, as you add more scenes, you’ll make this connection yourself in the Identity inspector. The [Identity inspector](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvoobq) lets you edit properties of an object in your storyboard related to that object’s identity, such as what class the object belongs to.

（原归档配图获取待重试：`CUIC_inspector_identity_2x.png`）

At runtime, your storyboard creates an instance of `ViewController`, your custom view controller subclass. The scene from your storyboard appears on the device’s screen, and the user interface’s behavior is defined in `ViewController.swift`.

Although the scene is connected to `ViewController.swift`, that’s not the only connection that needs to be made. To define interaction in your app, your view controller source code needs to be able to communicate with the views in your storyboard. You do this by defining additional connections—called outlets and actions—between the views in the storyboard and the view controller source code files.

### Create Outlets for UI Elements

[Outlets](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjv) provide a way to reference interface objects—the objects you added to your storyboard—from source code files. To create an outlet, Control-drag from a particular object in your storyboard to a view controller file. This operation creates a [property](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjy) for the object in your view controller file, which lets you access and manipulate that object from code at runtime.

You’ll need to create outlets for the text field and label in your user interface to be able to reference them.

__To connect the text field to the ViewController.swift code__

1. Open your storyboard, `Main.storyboard`.
2. Click the Assistant button in the Xcode toolbar near the top right corner of Xcode to open the [assistant editor](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonzw).

   （原归档配图未能恢复：`assistant_editor_toggle_2x.png`）
3. If you want more space to work, collapse the [project navigator](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjx) and [utility area](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonzs) by clicking the Navigator and Utilities buttons in the Xcode toolbar.

   （原归档配图未能恢复：`navigator_utilities_toggle_on_2x.png`）

   You can also collapse the [outline view](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjw).
4. In the editor selector bar, which appears at the top of the assistant editor, change the assistant editor from Preview to Automatic > `ViewController.swift`.

   （原归档配图未能恢复：`CUIC_switchtoviewcontroller_2x.png`）

   `ViewController.swift` displays in the editor on the right.
5. In `ViewController.swift`, find the `class` line, which should look like this:

   1. `class ViewController: UIViewController {`
6. Below the `class` line, add the following:

   1. `//MARK: Properties`

   You just added a comment to your source code. Recall that a [comment](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomzr) is a piece of text in a source code file that doesn’t get compiled as part of the program but provides context or useful information about individual pieces of code.

   A comment that begins with the characters `//MARK:` is a special type of comment that’s used to organize your code and to help you (and anybody else who reads your code) navigate through it. You’ll see this in action later. Specifically, the comment you added indicates that this is the section of your code that lists properties.
7. In your storyboard, select the text field.
8. Control-drag from the text field on your [canvas](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonq) to the code display in the editor on the right, stopping the drag at the line below the comment you just added in `ViewController.swift`.

   （原归档配图未能恢复：`CUIC_textfield_dragoutlet_2x.png`）
9. In the dialog that appears, for Name, type `nameTextField`. Leave the rest of the options as they are.

   （原归档配图获取待重试：`CUIC_textfield_addoutlet_2x.png`）
10. Click Connect.

    Xcode adds the necessary code to `ViewController.swift` to store a reference to the text field and configures the storyboard to set up that connection.

    1. `@IBOutlet weak var nameTextField: UITextField!`

Take a minute to understand what’s happening in this line of code.

The `IBOutlet` attribute tells Xcode that you can connect to the `nameTextField` property from Interface Builder (which is why the attribute has the `IB` prefix). The `weak` keyword indicates that the reference does not prevent the system from deallocating the referenced object. Weak references help prevent reference cycles; however, to keep the object alive and in memory you need to make sure some other part of your app has a strong reference to the object. In this case, it’s the text field’s superview. A superview maintains a strong reference to all of its subviews. As long as the superview remains alive and in memory, all of the subviews remain alive as well. Similarly, the view controller has a strong reference to its content view—keeping the entire view hierarchy alive and in memory.

The rest of the declaration defines an [implicitly unwrapped optional](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjq) variable of type `UITextField` named `nameTextField`. Pay careful attention to the exclamation point at the end of the type declaration. This exclamation point indicates that the type is an implicitly unwrapped optional, which is an [optional](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjr) type that will always have a value after it is first set. When you access an implicitly unwrapped optional, the system assumes it has a valid value and automatically unwraps it for you. Note that this causes the app to terminate if the variable’s value has not yet been set.

When a view controller is loaded from a storyboard, the system instantiates the view hierarchy and assigns the appropriate values to all the view controller’s outlets. By the time the view controller’s `viewDidLoad()` method is called, the system has assigned valid values to all of the controller’s outlets, and you can safely access their contents.

Now, connect the label to your code in the same way you connected the text field.

__To connect the label to the ViewController.swift code__

1. In your storyboard, select the label.
2. Control-drag from the label on your canvas to the code display in the editor on the right, stopping the drag at the line just below your `nameTextField` property in `ViewController.swift`.

   （原归档配图获取待重试：`CUIC_label_dragoutlet_2x.png`）
3. In the dialog that appears, for Name, type `mealNameLabel`. Leave the rest of the options as they are.

   （原归档配图获取待重试：`CUIC_label_addoutlet_2x.png`）
4. Click Connect.

Again, Xcode adds the necessary code to `ViewController.swift` to store a reference to the label and configures the storyboard to set up that connection. This outlet is similar to the text field, except for its name and its type (which is `UILabel`, to match the type of object that’s in the storyboard).

1. `@IBOutlet weak var mealNameLabel: UILabel!`

You only need an outlet to an interface object if you plan to either access a value from the interface object or modify the interface object in your code. In this case, you need to set the text field’s `delegate` property and set the label’s `text` property. You won’t be modifying the button, so there’s no reason to create an outlet for it.

Outlets let you refer to your interface elements in code, but you still need a way to respond whenever the user interacts with the elements. That’s where actions come in.

### Define an Action to Perform

iOS apps are based on [event-driven programming](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomzy). That is, the flow of the app is determined by events: system events and user actions. The user performs actions in the interface that trigger events in the app. These events result in the execution of the app’s logic and manipulation of its data. The app’s response to user action is then reflected back in the user interface. Because the user, rather than the developer, is in control of when certain pieces of the app code get executed, you want to identify exactly which actions a user can perform and what happens in response to those actions.

An [action](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomrt) (or an action method) is a piece of code that’s linked to an event that can occur in your app. When that event takes place, the system execute’s the action’s code. You can define an action method to accomplish anything from manipulating a piece of data to updating the user interface. You use actions to drive the flow of your app in response to user or system events.

You create an action the same way you create an outlet: Control-drag from a particular object in your storyboard to a view controller file. This operation creates a method in your view controller file that gets triggered when a user interacts with the object that the action method is attached to.

Start by creating a simple action that sets the label to `Default Text` whenever the user taps the Set Default Text button. (The code to set the label to the text in the text field is a bit more involved, so you’ll write that in the [Process User Input](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmrsfvjvonq) section.)

__To create a setDefaultLabelText action in the ViewController.swift code__

1. In `ViewController.swift`, just above the last curly brace (`}`), add the following:

   1. `//MARK: Actions`

   This comment indicates that this is the section of your code that lists actions.
2. In your storyboard, select the Set Default Label Text button.
3. Control-drag from the Set Default Label Text button on your canvas to the code display in the editor on the right, stopping the drag at the line below the comment you just added in `ViewController.swift`.

   （原归档配图获取待重试：`CUIC_button_dragaction_2x.png`）
4. In the dialog that appears, for Connection select Action.
5. For Name, type `setDefaultLabelText`.
6. For Type, select `UIButton`.

   You may have noticed that the value of the Type field defaults to `AnyObject`. In Swift, `AnyObject` is a type used to describe an object that can belong to any class. Specifying the type of this action method to be `UIButton` means that only button objects can connect to this action. Although this isn’t significant for the action you’re creating right now, it’s important to remember for later.

   Leave the rest of the options as they are.

   （原归档配图未能恢复：`CUIC_button_addaction_2x.png`）
7. Click Connect.

Xcode adds the necessary code to `ViewController.swift` to set up the action method.

1. `@IBAction func setDefaultLabelText(_ sender: UIButton) {`
2. `}`

The `sender` parameter refers to the object that was responsible for triggering the action—in this case, a button. The `IBAction` attribute indicates that the method is an action that you can connect to from your storyboard in Interface Builder. The rest of the declaration declares a method by the name of `setDefaultLabelText(_:)`.

Right now, the method declaration is empty. The code to reset the value of the label is quite simple.

__To implement the label reset action in the ViewController code__

1. In `ViewController.swift`, find the `setDefaultLabelText` action method you just added.
2. In the method implementation, between the curly braces (`{}`), add this line of code:

   1. `mealNameLabel.text = "Default Text"`

   As you might guess, this code sets the label’s `text` property to Default Text.

   Notice that you didn’t have to specify the type of Default Text, because Swift’s [type inference](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonzq) can see that you’re assigning to something of type `String` and can infer the type correctly.

iOS handles all of the redrawing code for you, so this is actually all the code you need to write for now. Your `setDefaultLabelText(_:)` action method should look like this:

1. `@IBAction func setDefaultLabelText(_ sender: UIButton) {`
2. `mealNameLabel.text = "Default Text"`
3. `}`

_Checkpoint:_ Test your changes by running the simulator. When you click the Set Default Label Text button, your `setDefaultLabelText(_:)` method is called, and the `mealNameLabel` object’s `text` value changes from `Meal Name` (the value set in your storyboard) to `Default Text` (the value set by the action). You should see the change in your user interface.

（原归档配图获取待重试：`CUIC_sim_defaulttext_2x.png`）

While changing the meal’s name to “Default Text” isn’t particularly useful, it does illustrate an important point. The behavior you just implemented is an example of the [target-action](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonry) pattern in iOS app design. Target-action is a design pattern where one object sends a message to another object when a specific event occurs.

In this case:

- The event is the user tapping the Set Default Text button.
- The action is `setDefaultLabelText(_)`.
- The target is `ViewController` (where the action method is defined).
- The sender is the Set Default Label Text button.

The system sends the message by calling the action method on the target and passing in the sender object. The sender is usually a control—such as a button, slider, or switch—that can trigger an event in response to user interaction such as a tap, drag, or value change. This pattern is extremely common in iOS app programming, and you’ll be seeing much more of it throughout the lessons.

### Process User Input

At this point, users can reset the meal name label to a default value, but you really want to let users enter their own meal names using the text field. To keep things simple, you’ll update the `mealNameLabel` object’s `text` value whenever the user enters text into the text field and taps Return.

When you work with accepting user input from a text field, you need some help from a text field delegate. A [delegate](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomzw) is an object that acts on behalf of, or in coordination with, another object. The delegating object—in this case, the text field—keeps a reference to the other object—the delegate—and at the appropriate time, the delegating object sends a message to the delegate. The message tells the delegate about an event that the delegating object is about to handle or has just handled. The delegate may respond by for example, updating the appearance or state of itself or of other objects in the app, or returning a value that affects how an impending event is handled.

A text field’s delegate communicates with the text field while the user is editing the text, and knows when important events occur—such as when a user starts or stops editing text. The delegate can use this information to save or clear data at the right time, dismiss the keyboard, and so on.

Any object can serve as a delegate for another object as long as it [conforms](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomzs) to the appropriate [protocol](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjz). The protocol that defines a text field’s delegate is called `UITextFieldDelegate`. It is very common to make a view controller the delegate for objects that it manages. In this case, you’ll make your `ViewController` instance the text field’s delegate.

First, `ViewController` needs to adopt the `UITextFieldDelegate` protocol. You [adopt](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomrw) a protocol by listing it as part of the class declaration line.

__To adopt the UITextFieldDelegate protocol__

1. If the assistant editor is open, return to the standard editor by clicking the Standard button.

   （原归档配图未能恢复：`standard_toggle_2x.png`）
2. Expand the project navigator and utility area by clicking the Navigator and Utilities buttons in the Xcode toolbar.
3. In the project navigator, select `ViewController.swift`.
4. In `ViewController.swift`, find the `class` line, which should look like this:

   1. `class ViewController: UIViewController {`
5. After `UIViewController`, add a comma (`,`) and `UITextFieldDelegate` to adopt the protocol.

   1. `class ViewController: UIViewController, UITextFieldDelegate {`

By adopting the `UITextFieldDelegate` protocol, you tell the compiler that the `ViewController` class can act as a valid text field delegate. This means you can implement the protocol’s methods to handle text input, and you can assign instances of the `ViewController` class as the delegate of the text field.

__To set the ViewController object as the delegate of its nameTextField property__

1. In `ViewController.swift`, find the `viewDidLoad()` method, which should look like this:

   1. `override func viewDidLoad() {`
   2. `super.viewDidLoad()`
   3. `// Do any additional setup after loading the view, typically from a nib.`
   4. `}`

   The template implementation of this method includes a comment. You don’t need this comment in your method implementation, so go ahead and delete it.
2. Below the `super.viewDidLoad()` line, add a blank line and the following:

   1. `// Handle the text field’s user input through delegate callbacks.`
   2. `nameTextField.delegate = self`

   The `self` refers to the `ViewController` class, because it’s referenced inside the scope of the `ViewController` class definition.

   You can add your own comments to help you understand what’s happening in your code.

Your `viewDidLoad()` method should look like this:

1. `override func viewDidLoad() {`
2. `super.viewDidLoad()`
4. `// Handle the text field’s user input through delegate callbacks.`
5. `nameTextField.delegate = self`
6. `}`

When a `ViewController` instance is loaded, it sets itself as the delegate of its `nameTextField` property.

The `UITextFieldDelegate` protocol defines eight optional methods. Just implement the ones you need to get the behaviors you desire. For now, you’ll need to implement two of these methods:

1. `func textFieldShouldReturn(_ textField: UITextField) -> Bool`
2. `func textFieldDidEndEditing(_ textField: UITextField)`

To understand when these methods get called and what they need to do, it’s important to know how text fields respond to user events. When the user taps a text field, it automatically becomes the first responder. In an app, the [first responder](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonbq) is an object that is first on the line for receiving many kinds of app events, including key events, motion events, and action messages, among others. In other words, many of the events generated by the user are initially routed to the first responder.

As a result of the text field becoming the first responder, iOS displays the keyboard and begins an editing session for that text field. What a user types using that keyboard gets inserted into the text field.

When a user wants to finish editing the text field, the text field needs to resign its first-responder status. Because the text field will no longer be the active object in the app, events need to get routed to a more appropriate object.

This is where your implementation of `UITextFieldDelegate` methods comes in. You need to specify that the text field should resign its first-responder status when the user taps a button to end editing in the text field. You do this in the `textFieldShouldReturn(_:)` method, which gets called when the user taps Return (or in this case, Done) on the keyboard.

__To implement the UITextFieldDelegate protocol method textFieldShouldReturn(_:)__

1. In `ViewController.swift`, right above the `//MARK: Actions` section, add the following:

   1. `//MARK: UITextFieldDelegate`

   This comment is used to organize your code and to help you (and anybody else who reads your code) navigate through it.

   You’ve added several of these comments so far. Xcode lists each of these comments as a section title in the source code file’s [Functions menu](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonbr), which appears if you click the name of the file at the top of the editor area. The Functions menu lets you jump to a section in your code quickly. You’ll notice the sections you denoted by `//MARK:` listed here. You can click on one of the section titles to jump to that section in the file.

   （原归档配图未能恢复：`CUIC_functionsmenu_2x.png`）
2. Below the comment, add the following method:

   1. `func textFieldShouldReturn(_ textField: UITextField) -> Bool {`
   2. `}`
3. In this method, add the following code to resign the text field’s first-responder status, and a comment to describe what the code does:

   1. `// Hide the keyboard.`
   2. `textField.resignFirstResponder()`

   Try typing the second line instead of just copying and pasting. You’ll find that [code completion](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomrz) is one of the great time-saving features of Xcode. When Xcode brings up the list of potential completions, scroll through the list until you find the one you want and then press Return. Xcode inserts the whole line for you.

   （原归档配图获取待重试：`CUIC_code_completion_2x.png`）
4. In this method, add the following line of code:

   1. `return true`

   This method returns a Boolean value that indicates whether the system should process the press of the Return key. In this case, you always want to respond to the user pressing the Return key, so just return `true`.

Your `textFieldShouldReturn(_:)` method should look like this:

1. `func textFieldShouldReturn(_ textField: UITextField) -> Bool {`
2. `// Hide the keyboard.`
3. `textField.resignFirstResponder()`
4. `return true`
5. `}`

The second method that you need to implement, `textFieldDidEndEditing(_:)`, is called after the text field resigns its first-responder status. Because you resign first responder status in `textFieldShouldReturn`, the system calls this method just after calling `textFieldShouldReturn`.

The `textFieldDidEndEditing(_:)` method gives you a chance to read the information entered into the text field and do something with it. In your case, you’ll take the text that’s in the text field and use it to change the value of your label.

__To implement the UITextFieldDelegate protocol method textFieldDidEndEditing(_:)__

1. In `ViewController.swift`, after the `textFieldShouldReturn(_:)` method, add the following method:

   1. `func textFieldDidEndEditing(_ textField: UITextField) {`
   2. `}`
2. In this method, add the following line of code:

   1. `mealNameLabel.text = textField.text`

That’s all you need to do to see the result. Your `textFieldDidEndEditing(_:)` method should look like this:

1. `func textFieldDidEndEditing(_ textField: UITextField) {`
2. `mealNameLabel.text = textField.text`
3. `}`

_Checkpoint:_ Test your changes by running the simulator. You can select the text field and type text into it. When you click the Done button on the keyboard, the keyboard is dismissed and the label text changes to display the text in the text field. When you click the Set Default Label Text button, the label changes from what’s currently displayed in the label to `Default Text` (the value set by the action you defined earlier).

（原归档配图未能恢复：`CUIC_sim_finalUI_2x.png`）

### Wrapping Up

In this lesson, you’ve used the assistant editor to add outlets and actions to your source code. You’ve also added code to update the user interface as the user interacts with the controls. The project is still just a relatively simple, single scene, but you will continue to add features and increase its complexity over the remaining lessons.

> [!NOTE]
>
> To see the completed sample project for this lesson, download the file and view it in Xcode.
>
> （原归档配图未能恢复：`WWDR_download_icon_withPadding_2x.png`）[Download File](https://developer.apple.com/sample-code/swift/downloads/02_ConnectTheUIToTheCode.zip)

[Build a Basic UI](BuildABasicUI.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqnjnknltc)

[Work with View Controllers](WorkWithViewControllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqnrnknltc)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-12-08](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqojzfvjvomi)

[Next](WorkWithViewControllers.md)[Previous](BuildABasicUI.md)
