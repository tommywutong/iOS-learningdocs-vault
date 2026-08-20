---
title: Start Developing iOS Apps (Swift)
apple_id: TP40015214
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2016-12-08'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/DevelopiOSAppsSwift/BuildABasicUI.html
archived_at: '2026-07-27T06:57:09.558032Z'
---
> 导航：[总目录](../../../README.md) · [referencelibrary](../../../_indexes/referencelibrary.md) · [Start Developing iOS Apps (Swift)](index.md)


[Next](ConnectTheUIToCode.md)[Previous](index.md)

## Build a Basic UI

This lesson gets you familiar with Xcode, the tool you use to write apps. You’ll become familiar with the structure of a project in Xcode and learn how to navigate between and use basic project components. In the lesson, you’ll start making a simple [user interface (UI)](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjy) for the FoodTracker app and view it in the simulator. When you’re finished, your app will have a label for the meal’s name, a text field to change the meal’s name, and a button for resetting the name.

（原归档配图未能恢复：`BBUI_sim_finalUI_2x.png`）

### Learning Objectives

At the end of the lesson, you’ll be able to:

- Create a project in Xcode
- Identify the purpose of key files that are created with an Xcode project template
- Open and switch between files in a project
- Run an app in iOS Simulator
- Add, move, and resize UI elements in a storyboard
- Edit the attributes of UI elements in a storyboard using the Attributes inspector
- View and rearrange UI elements using the outline view
- Preview a storyboard UI using the Assistant editor’s Preview mode
- Use Auto Layout to lay out a UI that automatically adapts to the user’s device size

### Create a New Project

Xcode includes several built-in app templates for developing common types of iOS apps, such as games, apps with tab-based navigation, and table view-based apps. Most of these templates have preconfigured interface and source code files. For this lesson, you’ll start with the most basic template: Single View Application.

__To create a new project__

1. Open Xcode from the `/Applications` directory.

   If this is the first time you’ve launched Xcode, it may ask you to agree to the user agreement and to download additional components. Follow the prompts through these screens until Xcode is completely set up and ready to launch.

   As soon as Xcode launches, the welcome window appears.

   （原归档配图获取待重试：`BBUI_welcomewindow_2x.png`）

   If a project window appears instead of the welcome window, don’t worry—you probably created or opened a project in Xcode previously. Just use the menu item in the next step to create the project.
2. In the welcome window, click “Create a new Xcode project” (or choose File > New > Project).

   Xcode opens a new window and displays a dialog in which you choose a template.
3. Select iOS at the top of the dialog.
4. In the Application section, select Single View Application and then click Next.

   （原归档配图未能恢复：`BBUI_singleviewapp_template_2x.png`）
5. In the dialog that appears, use the following values to name your app and choose additional options for your project:

   - Product Name: `FoodTracker`

     Xcode uses the product name you entered to name your project and the app.
   - Team: If this is not automatically filled in, set the team to None.
   - Organization Name: The name of your organization or your own name. You can leave this blank.
   - Organization Identifier: Your organization identifier, if you have one. If you don’t, use `com.example`.
   - Bundle Identifier: This value is automatically generated based on your product name and organization identifier.
   - Language: Swift
   - Devices: Universal

     A Universal app is one that runs on both iPhone and iPad.
   - Use Core Data: Unselected.
   - Include Unit Tests: Selected.
   - Include UI Tests: Unselected.

   （原归档配图获取待重试：`BBUI_newproject_2x.png`）
6. Click Next.
7. In the dialog that appears, select a location to save your project and click Create.

   Xcode opens your new project in the [workspace window](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvooi).

   （原归档配图获取待重试：`BBUI_workspacewindow_2x.png`）

The workspace window may have an error icon with a message that says “Signing for FoodTracker requires a development team.” This warning means you haven’t set up Xcode for iOS development yet, but don’t worry, you can complete these lessons without doing that. You do not need a development team to run the app in the simulator.

> [!NOTE]
>
> Before you can run the app on an iOS device, you need to set a valid team so that the app can be signed. If you are an individual or part of an organization that is a member of the Apple Developer Program, you can select that team here. Otherwise, your Apple ID is assigned to a personal team that you can use to launch apps on devices. However, you will need to join the Apple Developer Program before you can submit your app to the App store.
>
> For more information, select Help > Xcode Help and search for “Signing workflow.”

### Get Familiar with Xcode

Xcode includes everything you need to create an app. It organizes all the files and resources that go into creating an app. It provides editors for both your code and your user interfaces. Also, Xcode lets you build, run, and debug your app—providing simulators for iOS devices and a powerful integrated debugger.

Take a few moments to familiarize yourself with the main sections of the Xcode workspace:

- __Navigator area.__ Provides quick access to the various parts of your project.
- __Editor area.__ Allows you to edit source code, user interfaces, and other resources.
- __Utility area.__ Provides information about selected items and access to ready-made resources. The Utility area is divided into two parts. The top is the [inspector pane](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonbw), where you view and edit information about items selected in the navigator or edit areas. The bottom is the [library pane](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjsgy), where you access user interface elements, code snippets, and other resources.
- __Toolbar.__ Used to build and run your apps, view the progress of running tasks, and configure your work environment.

（原归档配图获取待重试：`BBUI_workspacewindow_callouts_2x.png`）

Don’t be overwhelmed by all of the pieces; each area is described in more detail when you need to use it.

### Run iOS Simulator

Because you based your project on an Xcode template, the basic app environment is automatically set up for you. Even though you haven’t written any code, you can build and run the Single View Application template without any additional configuration.

To build and run your app, use the iOS [Simulator](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonby) app that’s included in Xcode. The simulator gives you an idea of how your app would look and behave if it were running on a device.

The simulator can model a number of different types of hardware—All the screen sizes and resolutions for both iPad and iPhone—so you can simulate your app on every device you’re developing for. In this lesson, use the iPhone 7 option.

__To run your app in the simulator__

1. In the Scheme pop-up menu in the Xcode toolbar, choose iPhone 7.

   The Scheme pop-up menu lets you choose which simulator or device you’d like to run your app on. Make sure you select the iPhone 7 Simulator, not an iOS device.

   （原归档配图获取待重试：`BBUI_schememenu_2x.png`）
2. Click the Run button, located in the top-left corner of the Xcode toolbar.

   （原归档配图获取待重试：`BBUI_toolbar_2x.png`）

   Alternatively, choose Product > Run (or press Command-R).

   If you’re running an app for the first time, Xcode asks whether you’d like to enable developer mode on your Mac. Developer mode allows Xcode access to certain debugging features without requiring you to enter your password each time. Decide whether you’d like to enable developer mode and follow the prompts.

   （原归档配图获取待重试：`BBUI_developermode_2x.png`）

   If you choose not to enable developer mode, you may be asked for your password later on. These lessons assume developer mode is enabled.
3. Watch the Xcode toolbar as the build process completes.

   Xcode displays messages about the build process in the [activity viewer](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomru), which is in the middle of the toolbar.

After Xcode finishes building your project, the simulator starts automatically. It may take a few moments to start up the first time.

The simulator opens in the iPhone mode you specified and then launches your app. Initially, the simulator displays your app’s launch screen, and then it transitions to your app’s main interface. In an unmodified Single View Application template, the launch screen and the main interface are identical.

（原归档配图获取待重试：`BBUI_sim_blank_2x.png`）

Right now, the Single View Application template doesn’t do much—it just displays a white screen. Other templates have more complex behavior. It’s important to understand a template’s uses before you extend it to make your own app. Running your app in the simulator with no modifications is a good way to start developing that understanding.

Quit the simulator by choosing Simulator > Quit Simulator (or pressing Command-Q).

### Review the Source Code

The Single View Application template comes with a few source code files that set up the app environment. First, take a look at the `AppDelegate.swift` file.

__To look at the AppDelegate.swift source file__

1. Make sure the project navigator is open in the navigator area.

   The [project navigator](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjx) displays all the files in your project. If the project navigator isn’t open, click the leftmost button in the navigator selector bar. (Alternatively, choose View > Navigators > Show Project Navigator.)

   （原归档配图获取待重试：`BBUI_projectnavigator_2x.png`）
2. If necessary, open the FoodTracker folder in the project navigator by clicking the disclosure triangle next to it.
3. Select `AppDelegate.swift`.

   Xcode opens the source file in the main editor area of the window.

   （原归档配图获取待重试：`BBUI_appdelegate_file_2x.png`）

   Alternatively, double-click the `AppDelegate.swift` file to open it in a separate window.

### The App Delegate Source File

The `AppDelegate.swift` source file has two primary functions:

- It defines your `AppDelegate` class. The [app delegate](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomrx) creates the window where your app’s content is drawn and provides a place to respond to state transitions within the app.
- It creates the [entry point](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomzx) to your app and a [run loop](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonrr) that delivers input events to your app. This work is done by the `UIApplicationMain` attribute (`@UIApplicationMain`), which appears toward the top of the file.

  Using the `UIApplicationMain` attribute is equivalent to calling the `UIApplicationMain` function and passing your `AppDelegate` class’s name as the name of the delegate class. In response, the system creates an [application object](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonzv). The application object is responsible for managing the life cycle of the app. The system also creates an instance of your `AppDelegate` class, and assigns it to the application object. Finally, the system launches your app.

The `AppDelegate` class is automatically created whenever you create a new project. Unless you are doing something highly unusual, you should use this class provided by Xcode to initialize your app and respond to app-level events. The `AppDelegate` class adopts the `UIApplicationDelegate` protocol. This protocol defines a number of methods you use to set up your app, to respond to the app’s state changes, and to handle other app-level events.

The `AppDelegate` class contains a single property: `window`.

1. `var window: UIWindow?`

This property stores a reference to the app’s window. This window represents the root of your app’s view hierarchy. It is where all of your app content is drawn. Note that the window property is an [optional](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjr), which means it may have no value (be [nil](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvoni)) at some point.

The `AppDelegate` class also contains stub implementations of the following delegate [methods](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjs):

1. `func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool`
2. `func applicationWillResignActive(_ application: UIApplication)`
3. `func applicationDidEnterBackground(_ application: UIApplication)`
4. `func applicationWillEnterForeground(_ application: UIApplication)`
5. `func applicationDidBecomeActive(_ application: UIApplication)`
6. `func applicationWillTerminate(_ application: UIApplication)`

These methods let the application object communicate with the app delegate. During an app state transition—for example, app launch, transitioning to the background, and app termination—the application object calls the corresponding delegate method, giving your app an opportunity to respond. You don’t need to do anything special to make sure these methods get called at the correct time—the application object handles that job for you.

Each of the delegate methods has a default behavior. If you leave the template implementation empty or delete it from your `AppDelegate` class, you get the default behavior whenever that method is called. Alternatively, you can add your own code to the stub methods, defining custom behaviors that are executed when the methods are called.

The template also provides comments for each of the stub methods. These comments describe how these methods can be used by your app. You can use the stub methods and comments as a blueprint for designing many common app-level behaviors.

In this lesson, you won’t be using any custom app delegate code, so you don’t have to make any changes to the `AppDelegate.swift` file.

### The View Controller Source File

The Single View Application template has another source code file: `ViewController.swift`. Select `ViewController.swift` in the project navigator to view it.

（原归档配图获取待重试：`BBUI_viewcontroller_file_2x.png`）

This file defines a custom [subclass](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomju) of `UIViewController` named `ViewController`. Right now, this class simply inherits all the behavior defined by `UIViewController`. To override or extend that behavior, you override the methods defined on `UIViewController`.

As you can see in the `ViewController.swift` file, the template’s implementation overrides both the `viewDidLoad()` and `didReceiveMemoryWarning()` methods; however, the template’s stub implementation doesn’t do anything yet, except call the `UIViewController` version of these methods. You can add your own code to customize the view controller’s response to these events.

Although the template comes with the `didReceiveMemoryWarning()` method, you won’t need to implement it in these lessons, so go ahead and delete it.

At this point, your `ViewController.swift` code should look something like this:

1. `import UIKit`
3. `class ViewController: UIViewController {`
5. `override func viewDidLoad() {`
6. `super.viewDidLoad()`
7. `// Do any additional setup after loading the view, typically from a nib.`
8. `}`
10. `}`

You’ll start writing code in this source code file later in this lesson.

### Open Your Storyboard

You’re ready to start working on a storyboard for your app. A [storyboard](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvooa) is a visual representation of the app’s user interface, showing screens of content and the transitions between them. You use storyboards to lay out the flow—or story—that drives your app. You see exactly what you're building while you’re building it, get immediate feedback about what’s working and what’s not, and make instantly visible changes to your user interface.

__To open your storyboard__

- In the project navigator, select `Main.storyboard`.

  Xcode opens the storyboard in [Interface Builder](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonbx)—its visual interface editor—in the editor area. The background of the storyboard is the [canvas](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonq). You use the canvas to add and arrange user interface elements.

  （原归档配图获取待重试：`BBUI_storyboard_empty_2x.png`）

At this point, the storyboard in your app contains one [scene](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonrs), which represents a screen of content in your app. The arrow that points to the left side of the scene on the canvas is the [storyboard entry point](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonrw), which means that this scene is loaded first when the app starts. This scene contains a single view that’s managed by a view controller. You’ll learn more about the roles of views and view controllers soon.

When you ran your app in the iPhone 7 Simulator app, the view in this scene is what you saw on the device screen. However, the scene on the canvas may not have the same dimensions as the simulator’s screen. You can select the screen size and orientation at the bottom of the canvas. In this case, it’s set to iPhone 7 in a portrait orientation, so the canvas and the simulator are the same.

Even though the canvas shows a specific device and orientation, it is important to create an [adaptive interface](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomrv)—an interface that automatically adjusts so that it looks good on any device and in any orientation. As you develop your interface, you can change the canvas’s view, letting you see how your interface adapts to different size screens.

### Build the Basic UI

It’s time to build a basic interface. You’ll start by working on a user interface for the scene that lets you add a new meal to your meal tracking app, FoodTracker.

Xcode provides a library of objects that you can add to a storyboard file. Some of these are elements that appear in the user interface, such as buttons and text fields. Others, such as view controllers and gesture recognizers, define the behavior of your app but don’t appear onscreen.

The elements that appear in the user interface are known as views. [Views](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjw) display content to the user. They are the building blocks for constructing your user interface and presenting your content in a clear, elegant, and useful way. Views have a variety of useful built-in behaviors, including displaying themselves onscreen and reacting to user input.

All view objects in iOS are of type `UIView` or one of its subclasses. Many `UIView` subclasses are highly specialized in appearance and behavior. Start by adding a text field (`UITextField`), one such subclass of `UIView`, to your scene. A text field lets a user type in a single line of text, which you’ll use as the name of a meal.

__To add a text field to your scene__

1. Choose Editor > Canvas, and make sure Show Bounds Rectangles is selected.

   This setting causes Interface Builder to draw a blue bounding box around all the views in the canvas. Many views and controls have transparent backgrounds, making it difficult to see their actual size. Layout bugs occur when the system resizes a view so that it’s either larger or smaller than you anticipate. Enabling this setting helps you understand exactly what’s going on in your view hierarchy.
2. Open the Object library.

   The [Object library](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonju) appears at the bottom of the [utility area](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonzs) on the right side of Xcode. If you don’t see the Object library, click its button, which is the third button from the left in the library selector bar. (Alternatively, choose View > Utilities > Show Object Library.)

   （原归档配图获取待重试：`object_library_2x.png`）

   A list appears showing each object’s name, description, and visual representation.
3. In the Object library, type `text field` in the filter field to find the Text Field object quickly.
4. Drag a Text Field object from the Object library to your scene.

   （原归档配图未能恢复：`BBUI_textfield_drag_2x.png`）

   If necessary, zoom in by choosing Editor > Canvas > Zoom.
5. Drag the text field so that it’s positioned in the top half of the scene and aligned with the left margin in the scene.

   Stop dragging the text field when it snaps to the left margin.

   （原归档配图获取待重试：`BBUI_textfield_place_2x.png`）

   The blue layout guides help you place the text field. Layout guides are visible only when you drag or resize objects next to them; they disappear when you let go of the text field.
6. If necessary, click the text field to reveal the resize handles.

   You resize a user interface element by dragging its [resize handles](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonrq), which are small white squares that appear on the element’s borders. You reveal an element’s resize handles by selecting it. In this case, the text field should already be selected because you just stopped dragging it. If your text field looks like the one below, you’re ready to resize it; if it doesn’t, select it on the canvas.

   （原归档配图获取待重试：`BBUI_textfield_resizehandles_2x.png`）
7. Resize the left and right edges of the text field until you see three vertical layout guides: the left margin alignment, the horizontal center alignment, and the right margin alignment.

   （原归档配图获取待重试：`BBUI_textfield_finalsize_2x.png`）

Although you have the text field in your scene, there’s no instruction to the user about what to enter in the field. Use the text field’s placeholder text to prompt the user to enter the name of a new meal.

__To configure the text field’s placeholder text__

1. With the text field selected, open the Attributes inspector （原归档配图获取待重试：`inspector_attributes_2x.png`） in the utility area.

   The [Attributes inspector](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjz) appears when you click the fourth button from the left in the inspector selector bar. It lets you edit the properties of an object in your storyboard.

   （原归档配图获取待重试：`BBUI_inspector_attributes_2x.png`）
2. In the Attributes inspector, find the field labeled Placeholder and type `Enter meal name`.

   > [!NOTE]
   >
   > In a production app, any String that can be seen by the user (such as the text field’s placeholder text) should be localized. For more information, see [Build Apps for the World](https://developer.apple.com/internationalization/).
3. Press Return to display the new placeholder text in the text field.

   （原归档配图未能恢复：`BBUI_textfield_withplaceholder_2x.png`）

While you’re editing the text field’s attributes, you can also edit the attributes of the system keyboard that’s displayed when a user selects the text field.

__To configure the text field’s keyboard__

1. Make sure the text field is still selected.
2. In the Attributes inspector, find the field labeled Return Key and select Done (scroll down if necessary).

   This change will make the default Return key on the keyboard more pronounced to the user by changing it into a Done key.
3. In the Attributes inspector, select the Auto-enable Return Key checkbox (again, scroll down if necessary).

   This change makes it impossible for the user to tap the Done key before typing text into the text field, ensuring that users can never enter an empty string as a meal name.

（原归档配图获取待重试：`BBUI_keyboardattributes_2x.png`）

Next, add a label (`UILabel`) at the top of the scene. A label isn’t interactive; it just displays static text in the user interface. To help you understand how to define interaction between elements in the user interface, you’ll configure this label to display the text the user enters into the text field. It’ll be a good way to test that the text field is taking the user input and processing it appropriately.

__To add a label to your scene__

1. In the Object library, type `label` in the filter field to find the Label object quickly.
2. Drag a Label object from the Object library to your scene.
3. Drag the label so that it’s right above the text field and aligned with the left margin in the scene.

   Stop dragging the label when it snaps to the guidelines.

   （原归档配图获取待重试：`BBUI_label_place_2x.png`）
4. Double-click the label and type `Meal Name`.
5. Press Return to display the new text in the label.

   （原归档配图获取待重试：`BBUI_label_rename_2x.png`）

Now, add a button (`UIButton`) to the scene. A button is interactive, so users can tap it to trigger an action that you define. Later, you’ll create an action to reset the label text to a default value.

__To add a button to your scene__

1. In the Object library, type `button` in the filter field to find the Button object quickly.
2. Drag a Button object from the Object library to your scene.
3. Drag the button so that it’s right below the text field and aligned with the left margin in the scene.

   Stop dragging the button when it snaps to the guidelines.

   （原归档配图获取待重试：`BBUI_button_place_2x.png`）
4. Double-click the button and type `Set Default Label Text`.
5. Press Return to display the new text in the button.
6. Reposition the button, if necessary.

   （原归档配图获取待重试：`BBUI_button_rename_2x.png`）

It’s good to understand how the elements you’ve added are actually arranged in the scene. Look at the outline view to see which user interface elements have been added to your scene.

__To view the outline view__

1. In your storyboard, find the outline view toggle.

   （原归档配图获取待重试：`BBUI_outlineview_toggle_2x.png`）
2. If the outline view is collapsed, click the toggle to expand the outline view.

   You can use the outline view toggle to collapse and expand the outline view as needed.

The [outline view](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjw), which appears on the left side of the canvas, provides a hierarchical representation of the objects in your storyboard. You should be able to see the text field, label, and button you just added listed in the hierarchy. But why are the user interface elements you added nested under View?

Views not only display themselves onscreen and react to user input, they can serve as containers for other views. Views are arranged in a hierarchical structure called the view hierarchy. The [view hierarchy](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomrr) defines the layout of views relative to other views. Within that hierarchy, views enclosed within a view are called [subviews](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomrs), and the parent view that encloses a view is called its [superview](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonrx). A view can have multiple subviews and only one superview.

（原归档配图获取待重试：`BBUI_outlineview_2x.png`）

In general, each scene has its own view hierarchy. At the top of each view hierarchy is a [content view](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomzu). In the current scene, the content view is named View, the top level view inside the View Controller. The text field, label, and button are subviews of the content view. All other views that you place in this scene will be subviews of this content view (although they themselves can have nested subviews).

### Preview Your Interface

Preview your app periodically to check that everything is looking the way you expect. You can preview your app interface using the [assistant editor](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonzw), which displays a secondary editor side-by-side with your main one.

__To preview your interface__

1. Click the Assistant button in the Xcode toolbar near the top right corner of Xcode to open the assistant editor.

   （原归档配图获取待重试：`assistant_editor_toggle_2x.png`）
2. If you want more space to work, collapse the project navigator and utility area by clicking the Navigator and Utilities buttons in the Xcode toolbar.

   （原归档配图获取待重试：`navigator_utilities_toggle_on_2x.png`）

   You can also collapse the outline view.
3. In the editor selector bar, which appears at the top of the assistant editor, switch the assistant editor from Automatic to Preview > Main.storyboard (Preview).

   （原归档配图获取待重试：`BBUI_assistant_editorselectorbar_2x.png`）

   （原归档配图获取待重试：`BBUI_assistant_editorselectorbarpreview_2x.png`）

   As you see in the assistant editor, the preview looks almost identical to the canvas. However, this does not really tell you anything new. Both the canvas and the preview are showing the same size screen (iPhone 7) and the same orientation (portrait). If you want to check and see if your interface is adaptive, you need to preview different size screens and different orientations.

   （原归档配图获取待重试：`BBUI_preview_same_2x.png`）
4. To preview the landscape orientation, click the Rotate button at the bottom of the preview.

   （原归档配图获取待重试：`BBUI_preview_rotatebutton_2x.png`）

   Unfortunately, things no longer look quite right. The text field, label, and button keep the same size and position relative to the screen’s upper left corner. This means that the text field no longer fills the screen from margin to margin.

   （原归档配图获取待重试：`BBUI_preview_rotated_2x.png`）
5. To preview a different screen size, click the Add button at the bottom of the assistant editor, and select iPhone SE.

   （原归档配图获取待重试：`BBUI_preview_addSE_2x.png`）

   Again, the text field, label, and button keep the same size and position relative to the screen’s upper left corner. This time, however, the text field extends past the screen’s right edge.

   （原归档配图获取待重试：`BBUI_preview_small_2x.png`）

To create an adaptive interface, you’ll need to specify how the interface should adjust to different screen sizes. For example, when the interface is rotated into a landscape orientation, the text field should grow. When the interface is displayed on an iPhone SE, the text field should shrink. You can specify these kinds of interface rules easily using Auto Layout.

### Adopt Auto Layout

[Auto Layout](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonzx) is a powerful layout engine that helps you design adaptive layouts that dynamically respond to any changes to the scene’s size. You describe your layout using [constraints](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonzy)—rules that explain where one element should be located relative to another, or what size the element should be. Auto Layout dynamically calculates the size and position of each element based on these constraints.

One of the easiest ways to define your layout is using a stack view (`UIStackView`). A stack view provides a streamlined interface for laying out a collection of views in either a column or a row. The stack view uses Auto Layout under the hood to calculate the size and position of all the views that it manages. This lets you easily access the full power of Auto Layout, while greatly reducing the complexity of your layout.

To adopt Auto Layout, wrap your existing interface elements in a stack view, and then add the constraints needed to position the stack view in the scene.

__To add Auto Layout constraints to the meal scene__

1. Return to the standard editor by clicking the Standard button.

   （原归档配图获取待重试：`standard_toggle_2x.png`）

   Expand the project navigator and utility area by clicking the Navigator and Utilities buttons in the Xcode toolbar.
2. While pressing the Shift key on your keyboard, select the text field, label, and button.

   （原归档配图获取待重试：`BBUI_AL_shift_select_2x.png`）
3. On the bottom right of the canvas, click the Embed In Stack button. (Alternatively, choose Editor > Embed In > Stack View.)

   （原归档配图获取待重试：`BBUI_AL_stackmenu_2x.png`）

   Xcode wraps the user interface elements in a stack view, stacking them together. Xcode analyzes your existing layout to figure out that the items should stack vertically, not horizontally.

   （原归档配图获取待重试：`BBUI_AL_stack_2x.png`）
4. If necessary, open the outline view. Select the Stack View object.

   （原归档配图获取待重试：`BBUI_AL_outlineview_2x.png`）
5. In the Attributes inspector, type `8` in the Spacing field. Press Return.

   You’ll notice the user interface elements space out vertically, and the stack view grows with them.

   （原归档配图获取待重试：`BBUI_AL_stackspaced_2x.png`）
6. On the bottom right of the canvas, open the Add New Constraints menu.

   （原归档配图获取待重试：`BBUI_AL_pinmenu_2x.png`）
7. Above “Spacing to nearest neighbor,” click the two horizontal constraints and the top vertical constraint to select them. They become red when they are selected.

   （原归档配图未能恢复：`BBUI_AL_pinconstraints_2x.png`）

   These constraints indicate spacing to the nearest leading, trailing, and top neighbors. In this context, the term nearest neighbor means the boundary of the closest user interface element, which can be the superview, another user interface element, or a margin. Because the “Constrain to margins” checkbox is selected, the stack view in this case will be constrained to the superview’s left and right margins. This provides space between the stack view and the edge of the scene.

   On the other hand, the top of the stack is constrained relative to the scene’s top layout guide. The top layout guide is positioned at the bottom of the status bar, if the status bar is visible. If not, it is positioned at the top of the scene. Therefore, you need to add a little space between the stack view and the layout guide.
8. Type `0` in the left and right boxes, and type `20` spacing in the top box.
9. In the pop-up menu next to Update Frames, choose Items of New Constraints. This causes Interface Builder to automatically update the frames of the affected views when you create the constraints.

   （原归档配图获取待重试：`BBUI_AL_stackconstraints_2x.png`）
10. In the Add New Constraints menu, click the Add 3 Constraints button.

    （原归档配图获取待重试：`BBUI_AL_stackfinal_2x.png`）

The label, text field, and button are now left aligned and laid out with appropriate spacing, but the text field still isn’t stretching to fill the screen’s width. To fix that, you’ll need to add an additional constraint.

__To adjust the text field width within the stack__

1. In your storyboard, select the text field in the meal scene.
2. On the bottom right of the canvas, open the Add New Constraints menu again.

   （原归档配图获取待重试：`AL_pinmenu_2x.png`）
3. Above “Spacing to nearest neighbor,” click the right horizontal constraint to select it. It becomes red when it is selected.
4. Type `0` in the right box.
5. In the pop-up menu next to Update Frames, choose Items of New Constraints.

   （原归档配图获取待重试：`BBUI_AL_textfieldconstraint_2x.png`）
6. In the Add New Constraints menu, click the Add 1 Constraint button.

   （原归档配图未能恢复：`BBUI_AL_textfieldfinal_2x.png`）

_Checkpoint:_ Run your app in iOS Simulator. Rotate the simulator by choosing Hardware > Rotate Left and Hardware > Rotate Right (or Command-Left Arrow and Command-Right Arrow). Notice how the text field grows and shrinks to the appropriate size depending on the device’s orientation and screen size. Also notice that the status bar disappears in landscape orientation.

Click inside the text field and enter text using the onscreen keyboard (if you’d like, you can use your computer’s keyboard by choosing Hardware > Keyboard > Connect Hardware Keyboard).

（原归档配图未能恢复：`BBUI_sim_finalUI_2x.png`）

### Debugging Auto layout

If you don’t get the behavior you expect, use the Auto Layout debugging features to help you. These features can be accessed using the Update Frames button and Resolve Auto Layout Issues menu.

（原归档配图获取待重试：`BBUI_AL_resolvemenu_2x.png`）

If you are getting warnings about misplaced views, use the Update Frames button. This button updates the frames of the selected view and all of its subviews. Select the scene’s view controller to update all the views in the scene. You can also Option-click the Update Frames button to update only the selected view.

If the layout does not behave as you expect, click the Resolve Auto Layout Issues button to bring up a menu of debug commands. All the commands in this menu have two forms. One affects the currently selected view. The other affects all views in the current view controller. If all of the commands are grayed out, select the scene’s view controller or one of the views and open the menu again.

Choose Reset to Suggested Constraints to have Xcode update your interface with a valid set of constraints. Choose Clear Constraints to remove all constraints on the user interface elements, and then try following the previous instructions to set up the constraints again.

（原归档配图获取待重试：`BBUI_AL_resolvemenu_small_2x.png`）

### Wrapping Up

In this lesson, you’ve familiarized yourself with the contents of an Xcode project, and with many of the tools used to design and run an iOS app. You’ve also built a simple user interface.

Although the project’s scene doesn’t do much yet, the basic user interface is there and functional. Making sure your layout is robust and extensible from the start ensures that you have a solid foundation to build upon.

> [!NOTE]
>
> To see the completed sample project for this lesson, download the file and view it in Xcode.
>
> （原归档配图获取待重试：`WWDR_download_icon_withPadding_2x.png`）[Download File](https://developer.apple.com/sample-code/swift/downloads/01_BuildABasicUI.zip)

[Jump Right In](index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmrnknltc)

[Connect the UI to Code](ConnectTheUIToCode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmrsfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-12-08](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqojzfvjvomi)

[Next](ConnectTheUIToCode.md)[Previous](index.md)
