---
title: Start Developing iOS Apps (Swift)
apple_id: TP40015214
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2016-12-08'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/DevelopiOSAppsSwift/WorkWithViewControllers.html
archived_at: '2026-07-27T06:57:09.655299Z'
---
> 导航：[总目录](../../../README.md) · [referencelibrary](../../../_indexes/referencelibrary.md) · [Start Developing iOS Apps (Swift)](index.md)


[Next](ImplementingACustomControl.md)[Previous](ConnectTheUIToCode.md)

## Work with View Controllers

In this lesson, you’ll continue to work on the [user interface (UI)](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjy) for the meal scene in the FoodTracker app. You’ll add an image view to the scene, and use an image picker to let the user select an image for the meal.

（原归档配图获取待重试：`WWVC_sim_finalUI_2x.png`）

### Learning Objectives

At the end of the lesson, you’ll be able to:

- Understand the view controller life cycle and its callbacks (for example, `viewDidLoad`, `viewWillAppear` and `viewDidAppear`)
- Pass data between view controllers
- Dismiss a view controller
- Use gesture recognizers to generate events
- Anticipate object behavior based on the `UIView`/`UIControl` class hierarchy
- Use the asset catalog to add image assets to a project

### Understand the View Controller Lifecycle

So far, the FoodTracker app has a single [scene](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonrs), whose user interface is managed by a single [view controller](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvony). As you build more complex apps, you’ll create more scenes, and will need to manage loading and unloading [views](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjw) as they’re moved on and off the screen.

An object of the `UIViewController` class (and its subclasses) comes with a set of methods that manage its view hierarchy. iOS automatically calls these methods at appropriate times when a view controller transitions between states. When you create a view controller [subclass](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomju) (like the `ViewController` class you’ve been working with), it [inherits](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonbv) the methods defined in `UIViewController` and lets you add your own custom behavior for each method. It’s important to understand when the system calls these methods, so you can set up or tear down the views you’re displaying at the appropriate step in the process—something you’ll need to do later in the lessons.

（原归档配图未能恢复：`WWVC_vclife_2x.png`）

iOS calls the `UIViewController` methods as follows:

- `viewDidLoad()`—Called when the view controller’s content view (the top of its view hierarchy) is created and loaded from a storyboard. The view controller’s outlets are guaranteed to have valid values by the time this method is called. Use this method to perform any additional setup required by your view controller.

  Typically, iOS calls `viewDidLoad()` only once, when its content view is first created; however, the content view is not necessarily created when the controller is first instantiated. Instead, it is lazily created the first time the system or any code accesses the controller’s `view` property.
- `viewWillAppear()`—Called just before the view controller’s content view is added to the app’s view hierarchy. Use this method to trigger any operations that need to occur before the content view is presented onscreen. Despite the name, just because the system calls this method, it does not guarantee that the content view will become visible. The view may be obscured by other views or hidden. This method simply indicates that the content view is about to be added to the app’s view hierarchy.
- `viewDidAppear()`—Called just after the view controller’s content view has been added to the app’s view hierarchy. Use this method to trigger any operations that need to occur as soon as the view is presented onscreen, such as fetching data or showing an animation. Despite the name, just because the system calls this method, it does not guarantee that the content view is visible. The view may be obscured by other views or hidden. This method simply indicates that the content view has been added to the app’s view hierarchy.
- `viewWillDisappear()`—Called just before the view controller’s content view is removed from the app’s view hierarchy. Use this method to perform cleanup tasks like committing changes or resigning the first responder status. Despite the name, the system does not call this method just because the content view will be hidden or obscured. This method is only called when the content view is about to be removed from the app’s view hierarchy.
- `viewDidDisappear()`—Called just after the view controller’s content view has been removed from the app’s view hierarchy. Use this method to perform additional teardown activities. Despite the name, the system does not call this method just because the content view has become hidden or obscured. This method is only called when the content view has been removed from the app’s view hierarchy.

You’ll be using some of these methods in the FoodTracker app to load and display your data. In fact, if you recall, you’ve already written some code in the `viewDidLoad()` method of `ViewController`:

1. `override func viewDidLoad() {`
2. `super.viewDidLoad()`
4. `// Handle the text field’s user input through delegate callbacks.`
5. `nameTextField.delegate = self`
6. `}`

This style of app design where view controllers serve as the communication pipeline between your views and your data model is known as [MVC (Model-View-Controller)](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjs). In this pattern, models keep track of your app’s data, views display your user interface and make up the content of an app, and controllers manage your views. By responding to user actions and populating views with content from the [data model](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomzv), controllers serve as a gateway for communication between the model and views. MVC is central to a good design for any iOS app, and so far, the FoodTracker app has been built along MVC principles.

As you keep the MVC pattern in mind for rest of the app’s design, it’s time to take your basic user interface to the next level, and add an image to the meal scene.

### Add a Meal Photo

The next step in finishing the meal scene is adding a way to display a photo of a particular meal. For this, you’ll use an image view (`UIImageView`), a user interface element that displays a picture.

__To add an image view to your scene__

1. Open your [storyboard](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvooa), `Main.storyboard`.
2. Open the [Object library](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonju) in the [utility area](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonzs). (Alternatively, choose View > Utilities > Show Object Library.)

   （原归档配图未能恢复：`object_library_2x.png`）
3. In the Object library, type `image view` in the filter field to find the Image View object quickly.
4. Drag an Image View object from the Object library to your scene so that it’s in the stack view below the button.

   （原归档配图获取待重试：`WWVC_imageview_place_2x.png`）
5. With the image view selected, open the Size inspector （原归档配图未能恢复：`inspector_size_2x.png`） in the utility area.

   Recall that the [Size inspector](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvoobs) appears when you select the fifth button from the left in the inspector selector bar. It lets you edit the size and position of an object in your storyboard.

   （原归档配图获取待重试：`WWVC_inspector_size_2x.png`）
6. In the Intrinsic Size field, select Placeholder. (This field is at the bottom of the Size inspector, so you’ll need to scroll down to it.)
7. Type `320` in both the Width and Height fields. Press Return.

   A view’s [intrinsic content size](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjrga) is the preferred size for the view based on its content. An empty image view doesn’t have an intrinsic content size. As soon as you add an image to a view, its intrinsic content size is set to the image’s size. Providing a placeholder size gives the image a temporary intrinsic content size that you can use while designing your user interface. This value is only used while designing your interface in Interface Builder; at runtime, the layout engine uses the view’s actual intrinsic content size instead.

   （原归档配图未能恢复：`WWVC_placeholdersize_2x.png`）
8. On the bottom right of the canvas, open the Pin menu.

   （原归档配图未能恢复：`AL_pinmenu_2x.png`）
9. Select the checkbox next to Aspect Ratio.

   （原归档配图未能恢复：`WWVC_imageview_aspectratio_2x.png`）
10. In the Pin menu, click the Add 1 Constraints button.

    Your image view now has a 1:1 aspect ratio, so it will always be a square.

    （原归档配图未能恢复：`WWVC_imageview_finalconstraints_2x.png`）
11. With the image view selected, open the Attributes inspector （原归档配图未能恢复：`inspector_attributes_2x.png`）.

    Recall that the [Attributes inspector](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjz) appears when you select the fourth button from the left in the inspector selector bar. It lets you edit the properties of an object in your storyboard.
12. In the Attributes inspector, find the Interaction field and select the User Interaction Enabled checkbox.

    You’ll need this feature later to let users interact with the image view.

### Display a Default Photo

Add a placeholder image to let users know that they can interact with the image view to select a photo. Use this image from the `Images/` folder of the downloadable file at the end of this lesson, or use your own image.

（原归档配图获取待重试：`defaultphoto_2x.png`）

__To add an image to your project__

1. In the [project navigator](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjx), select `Assets.xcassets` to view the asset catalog.

   The [asset catalog](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonrz) is a place to store and organize your image assets for an app.
2. In the bottom left corner, click the plus (`+`) button and select New Image Set from the pop-up menu.

   （原归档配图未能恢复：`WWVC_assetcatalog_2x.png`）
3. Double-click the image set name and rename it to `defaultPhoto`.
4. On your computer, select the image you want to add.
5. Drag and drop the image into the `2x` slot in the image set.

   （原归档配图获取待重试：`WWVC_defaultphoto_drag_2x.png`）

   `2x` is the display resolution for the iPhone 7 [Simulator](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjsha) that you’re using in these lessons, so the image will look best at this resolution.

   > [!NOTE]
   >
   > For more information on image resolutions, see Graphics > Image Size and Resolution in _iOS Human Interface Guidelines_.

With the default placeholder image added to your project, set the image view to display it.

__To display a default image in the image view__

1. Open your storyboard.
2. In your storyboard, select the image view.
3. With the image view selected, open the Attributes inspector （原归档配图未能恢复：`inspector_attributes_2x.png`） in the utility area.
4. In the Attributes inspector, find the field labeled Image and select `defaultPhoto`.

_Checkpoint_: Run your app. The default image displays in the image view.

（原归档配图获取待重试：`WWVC_sim_finalUI_2x.png`）

### Connect the Image View to Code

Now, you need to implement the functionality to change the image in this image view at runtime. First, you need to connect the image view to the code in `ViewController.swift`.

__To connect the image view to the ViewController.swift code__

1. Click the Assistant button in the Xcode toolbar near the top right corner of Xcode to open the assistant editor.

   （原归档配图未能恢复：`assistant_editor_toggle_2x.png`）
2. If you want more space to work, collapse the [project navigator](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjx) and [utility area](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonzs) by clicking the Navigator and Utilities buttons in the Xcode toolbar.

   （原归档配图未能恢复：`navigator_utilities_toggle_on_2x.png`）

   You can also collapse the outline view.
3. In your storyboard, select the image view.
4. Control-drag from the image view on your canvas to the code display in the editor on the right, stopping the drag at the line just below the existing outlets in `ViewController.swift`.

   （原归档配图未能恢复：`WWVC_imageview_dragoutlet_2x.png`）
5. In the dialog that appears, for Name, type `photoImageView`. Leave the rest of the options as they are.

   （原归档配图未能恢复：`WWVC_imageview_addoutlet_2x.png`）
6. Click Connect.

   Xcode adds the necessary code to `ViewController.swift` to store a reference to the image view and configures the storyboard to set up that connection.

   1. `@IBOutlet weak var photoImageView: UIImageView!`

You can now access the image view from code to change its image, but how do you know when to change the image? You need to give users a way to indicate that they want to change the image—for example, by tapping the image view. Then, you’ll define an [action](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomrt) method to change the image when a tap occurs.

There’s a nuanced distinction between [views](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjw) and [controls](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjx), which are specialized versions of views that respond to user actions in a specific way. A view displays content, whereas a control is used to modify the content in some way. A control (`UIControl`) is a subclass of `UIView`. In fact, you’ve already worked with both views (labels, image views) and controls (text fields, buttons) in your interface.

### Create a Gesture Recognizer

An image view isn’t a control, so it’s not designed to respond to input in the same way that button or a slider might. For example, you can’t simply create an action method that’s triggered when a user taps on an image view. (If you try to Control-drag from the image view to your code, you’ll notice that you can’t select Action in the Connection field.)

Fortunately, it’s quite easy to give a view the same capabilities as a control by adding a gesture recognizer to it. [Gesture recognizers](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonbs) are objects that you attach to a view that allow the view to respond to the user the way a control does. Gesture recognizers interpret touches to determine whether they correspond to a specific gesture, such as a swipe, pinch, or rotation. You can write an action method that is called when a gesture recognizer recognizes its assigned gesture, which is exactly what you need to do for the image view.

Attach a tap gesture recognizer (`UITapGestureRecognizer`) to the image view, which will recognize when a user has tapped the image view. You can do this easily in your storyboard.

__To add a tap gesture recognizer to your image view__

1. Open the Object library (Choose View > Utilities > Show Object Library).
2. In the Object library, type `tap gesture` in the filter field to find the Tap Gesture Recognizer object quickly.
3. Drag a Tap Gesture Recognizer object from the Object library to your scene, and place it on top of the image view.

   （原归档配图获取待重试：`WWVC_gesturerecognizer_drag_2x.png`）

   The Tap Gesture Recognizer object appears in the meal [scene dock](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonrt).

   （原归档配图获取待重试：`WWVC_scenedock_2x.png`）

### Connect the Gesture Recognizer to Code

Now, connect that gesture recognizer to an action method in your code.

__To connect the gesture recognizer to the ViewController.swift code__

1. Control-drag from the gesture recognizer in the scene dock to the code display in the editor on the right, stopping the drag at the line below the `//MARK: Actions` [comment](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomzr) in `ViewController.swift`.

   （原归档配图获取待重试：`WWVC_gesturerecognizer_dragaction_2x.png`）
2. In the dialog that appears, for Connection, select Action.
3. For Name, type `selectImageFromPhotoLibrary`.
4. For Type, select `UITapGestureRecognizer`.

   （原归档配图获取待重试：`WWVC_gesturerecognizer_addaction_2x.png`）
5. Click Connect.

   Xcode adds the necessary code to `ViewController.swift` to set up the action.

   1. `@IBAction func selectImageFromPhotoLibrary(_ sender: UITapGestureRecognizer) {`
   2. `}`

### Create an Image Picker to Respond to User Taps

When a user taps the image view, they should be able to choose a photo from a collection of photos, or take one of their own. Fortunately, the `UIImagePickerController` class has this behavior built into it. An image picker controller manages the user interface for taking pictures and for choosing saved images to use in your app. And just as you need a text field [delegate](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomzw) when you work with a text field, you need an image picker controller delegate to work with an image picker controller. The name of that delegate [protocol](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjz) is `UIImagePickerControllerDelegate`, and the object that you’ll define as the image picker controller’s delegate is `ViewController.`

First, `ViewController` needs to adopt the `UIImagePickerControllerDelegate` protocol. Because `ViewController` will be in charge of presenting the image picker controller, it also needs to adopt the `UINavigationControllerDelegate` protocol, which simply lets `ViewController` take on some basic navigation responsibilities.

__To adopt the UIImagePickerControllerDelegate and UINavigationControllerDelegate protocols__

1. Return to the standard editor by clicking the Standard button.

   （原归档配图未能恢复：`standard_toggle_2x.png`）

   Expand the project navigator and utility area by clicking the Navigator and Utilities buttons in the Xcode toolbar.
2. In the project navigator, select `ViewController.swift`.
3. In `ViewController.swift`, find the `class` line, which should look like this:

   1. `class ViewController: UIViewController, UITextFieldDelegate {`
4. After `UITextFieldDelegate`, add a comma (`,`) and `UIImagePickerControllerDelegate` to adopt the protocol.

   1. `class ViewController: UIViewController, UITextFieldDelegate, UIImagePickerControllerDelegate {`
5. After `UIImagePickerControllerDelegate`, add a comma (`,`) and `UINavigationControllerDelegate` to adopt the protocol.

   1. `class ViewController: UIViewController, UITextFieldDelegate, UIImagePickerControllerDelegate, UINavigationControllerDelegate {`

At this point, you can go back to the action method you defined, `selectImageFromPhotoLibrary(_:)`, and finish its implementation.

__To implement the selectImageFromPhotoLibrary(_:) action method__

1. In `ViewController.swift`, find the `selectImageFromPhotoLibrary(_:)` action method you added earlier.

   It should look like this:

   1. `@IBAction func selectImageFromPhotoLibrary(_ sender: UITapGestureRecognizer) {`
   2. `}`
2. In the method implementation, between the curly braces (`{}`), add this code:

   1. `// Hide the keyboard.`
   2. `nameTextField.resignFirstResponder()`

   This code ensures that if the user taps the image view while typing in the text field, the keyboard is dismissed properly.
3. Add this code to create an image picker controller:

   1. `// UIImagePickerController is a view controller that lets a user pick media from their photo library.`
   2. `let imagePickerController = UIImagePickerController()`
4. Add this code:

   1. `// Only allow photos to be picked, not taken.`
   2. `imagePickerController.sourceType = .photoLibrary`

   This line of code sets the image picker controller’s source, or the place where it gets its images. The `.photoLibrary` option uses the simulator’s camera roll.

   The type of `imagePickerController.sourceType` is known to be `UIImagePickerControllerSourceType`, which is an [enumeration](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvooby). This means you can write its value as the abbreviated form `.photoLibrary` instead of `UIImagePickerControllerSourceType.photoLibrary`. Recall that you can use the abbreviated form anytime the enumeration value’s type is already known.
5. Add this code to set the image picker controller’s delegate to `ViewController`:

   1. `// Make sure ViewController is notified when the user picks an image.`
   2. `imagePickerController.delegate = self`
6. Below the previous line, add this line of code:

   1. `present(imagePickerController, animated: true, completion: nil)`

   `present(_:animated:completion:)` is a method being called on `ViewController`. Although it’s not written explicitly, this method is executed on an implicit `self` object. The method asks `ViewController` to present the view controller defined by `imagePickerController`. Passing `true` to the `animated` parameter animates the presentation of the image picker controller. The `completion` parameter refers to a [completion handler](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomzq), a piece of code that executes after this method completes. Because you don’t need to do anything else, you indicate that you don’t need to execute a completion handler by passing in [nil](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvoni).

Your `selectImageFromPhotoLibrary(_:)` action method should look like this:

1. `@IBAction func selectImageFromPhotoLibrary(_ sender: UITapGestureRecognizer) {`
3. `// Hide the keyboard.`
4. `nameTextField.resignFirstResponder()`
6. `// UIImagePickerController is a view controller that lets a user pick media from their photo library.`
7. `let imagePickerController = UIImagePickerController()`
9. `// Only allow photos to be picked, not taken.`
10. `imagePickerController.sourceType = .photoLibrary`
12. `// Make sure ViewController is notified when the user picks an image.`
13. `imagePickerController.delegate = self`
14. `present(imagePickerController, animated: true, completion: nil)`
15. `}`

After an image picker controller is presented, you interact with it through the delegate methods. To give users the ability to select a picture, you’ll need to implement two of the delegate methods defined in `UIImagePickerControllerDelegate`:

1. `func imagePickerControllerDidCancel(_ picker: UIImagePickerController)`
2. `func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : Any])`

The first of these, `imagePickerControllerDidCancel(_:)`, gets called when a user taps the image picker’s Cancel button. This method gives you a chance to dismiss the `UIImagePickerController` (and optionally, do any necessary cleanup).

__To implement the imagePickerControllerDidCancel(_:) method__

1. In `ViewController.swift`, right above the `//MARK: Actions` section, add the following:

   1. `//MARK: UIImagePickerControllerDelegate`

   This is a comment to help you (and anybody else who reads your code) navigate through your code and identify that this section applies to the image picker implementation.
2. Below the comment you just added, add the following method:

   1. `func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {`
   2. `}`
3. In this method, add the following line of code:

   1. `// Dismiss the picker if the user canceled.`
   2. `dismiss(animated: true, completion: nil)`

   This code animates the dismissal of the image picker controller.

Your `imagePickerControllerDidCancel(_:)` method should look like this:

1. `func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {`
2. `// Dismiss the picker if the user canceled.`
3. `dismiss(animated: true, completion: nil)`
4. `}`

The second `UIImagePickerControllerDelegate` method that you need to implement, `imagePickerController(_:didFinishPickingMediaWithInfo:)`, gets called when a user selects a photo. This method gives you a chance to do something with the image or images that a user selected from the picker. In your case, you’ll take the selected image and display it in your image view.

__To implement the imagePickerController(_:didFinishPickingMediaWithInfo:) method__

1. Below the `imagePickerControllerDidCancel(_:)` method, add the following method:

   1. `func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : Any]) {`
   2. `}`
2. In this method, add the following line of code:

   1. `// The info dictionary may contain multiple representations of the image. You want to use the original.`
   2. `guard let selectedImage = info[UIImagePickerControllerOriginalImage] as? UIImage else {`
   3. `fatalError("Expected a dictionary containing an image, but was provided the following: \(info)")`
   4. `}`

   The `info` dictionary always contains the original image that was selected in the picker. It may also contain an edited version of that image, if one exists. To keep things simple, you’ll use the original, unedited image for the meal photo.

   This code accesses the original, unedited image from the `info` dictionary. It safely unwraps the optional returned by the dictionary and casts it as a `UIImage` object. The expectation is that the unwrapping and casting operations will never fail. If they do, it represents either a bug in your app that needs to be fixed at design time. The `fatalError()` method logs an error message to the console, including the contents of the `info` dictionary, and then causes the app to terminate—preventing it from continuing in an invalid state.
3. Add this line of code to set the selected image in the image view outlet that you created earlier:

   1. `// Set photoImageView to display the selected image.`
   2. `photoImageView.image = selectedImage`
4. Add the following line of code to dismiss the image picker:

   1. `// Dismiss the picker.`
   2. `dismiss(animated: true, completion: nil)`

Your `imagePickerController(_:didFinishPickingMediaWithInfo)` method should look like this:

1. `func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : Any]) {`
3. `// The info dictionary may contain multiple representations of the image. You want to use the original.`
4. `guard let selectedImage = info[UIImagePickerControllerOriginalImage] as? UIImage else {`
5. `fatalError("Expected a dictionary containing an image, but was provided the following: \(info)")`
6. `}`
8. `// Set photoImageView to display the selected image.`
9. `photoImageView.image = selectedImage`
11. `// Dismiss the picker.`
12. `dismiss(animated: true, completion: nil)`
13. `}`

_Checkpoint_: Run your app. What happens when you click on the image view?

（原归档配图获取待重试：`WWVC_app_abort_2x.png`）

The app terminates with a `SIGABRT` signal. This means an error occurred that was serious enough to cause the app to abort. In this case, the problem occurs when you attempt to present the image picker. The system must ask the user for permission before accessing their photo library. In iOS 10 and later, you must provide a photo library usage description. This description explains why your app wants to access the photo library.

__To add a photo library usage description__

1. In the project navigator, select `Info.plist`.

   Xcode displays the property list editor in the editor area. A property list is a structured text file that contains essential configuration information about your app. The root of the property list is a dictionary that holds a set of predefined keys and their values.

   （原归档配图获取待重试：`WWVC_Property_List_Editor_2x.png`）
   > [!NOTE]
   >
   > For more information on possible `info.plist` keys, see _[Information Property List Key Reference](../../../documentation/General/Information%20Property%20List%20Key%20Reference/About%20Info.plist%20Keys%20and%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbx)_.
2. If the last item in the property list is an array, make sure the array is collapsed. If you add an item to an expanded array, it adds a child item. If you add an item to a collapsed array, it adds a sibling to the array.
3. To add a new item, hover over the last item in the property list, and click on the add button when it appears (or select Editor > Add Item).

   （原归档配图获取待重试：`WWVC_addInfoPlistItem_2x.png`）
4. In the pop-up menu, scroll down and choose Privacy - Photo Library Usage Description.

   （原归档配图未能恢复：`WWVC_addphotolibrarydescription_2x.png`）
5. In the new row, make sure the Type is set to String. Then, double-click on the Value section and enter `Allows you to add photos to your meals.`

   （原归档配图未能恢复：`WWVC_addingDescriptionString_2x.png`）
6. Press the Return key when you are done editing the description string.

_Checkpoint_: Run your app again. This time you should be able to click the image view to pull up an image picker. You’ll need to click OK on the alert that asks for permission to give the FoodTracker app access to Photos. Then, you can click the Cancel button to dismiss the picker, or open Camera Roll and click an image to select it and set it as the image in the image view.

（原归档配图获取待重试：`WWVC_sim_imagepicker_2x.png`）

If you look through the photos available in the simulator, you’ll notice that it doesn’t include any photos of food. You can add your own images directly into the simulator to test the FoodTracker app with appropriate sample content. You can find a sample image within the `Images/` folder of the downloadable file at the end of this lesson, or use your own image.

__To add images to iOS Simulator__

1. If necessary, run your app in the simulator.
2. On your computer, select the images you want to add.
3. Drag and drop the images into the simulator.

   （原归档配图获取待重试：`WWVC_sim_dragphoto_2x.png`）

   The simulator opens the Photos app and shows the images you added.

   （原归档配图获取待重试：`WWVC_sim_choosephoto_2x.png`）

_Checkpoint_: Run your app. You should be able to tap the image view to pull up an image picker. Open Camera Roll, and click one of the images you added to the simulator to select it and set it as the image in the image view.

（原归档配图获取待重试：`WWVC_sim_selectedphoto_2x.png`）

### Wrapping Up

In this lesson, you’ve learned about the view controller life cycle methods, and used them to configure your view controller’s content. You’ve also learned how to add gesture recognizers to a view, and how to select photos from the photo library. The scene is starting to look like a real app. In the next lesson, you’ll add a custom control to the scene.

> [!NOTE]
>
> To see the completed sample project for this lesson, download the file and view it in Xcode.
>
> （原归档配图未能恢复：`WWDR_download_icon_withPadding_2x.png`）[Download File](https://developer.apple.com/sample-code/swift/downloads/03_WorkWithViewControllers.zip)

[Connect the UI to Code](ConnectTheUIToCode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmrsfvjvomi)

[Implement a Custom Control](ImplementingACustomControl.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjzfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-12-08](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqojzfvjvomi)

[Next](ImplementingACustomControl.md)[Previous](ConnectTheUIToCode.md)
