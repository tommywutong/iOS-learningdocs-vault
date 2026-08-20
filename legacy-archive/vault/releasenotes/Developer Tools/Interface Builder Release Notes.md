---
title: Interface Builder Release Notes
apple_id: TP40001016
resource_type: Release Note
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/releasenotes/DeveloperTools/RN-InterfaceBuilder/index.html
archived_at: '2026-07-18T02:50:26.959688Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Interface Builder Release Notes

> [!IMPORTANT]
> 

This document contains the release notes for Interface Builder version 3.

#### Contents:

- [Interface Builder 3.2 Release Notes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjwfvjvomjx)
- [Interface Builder 3.1.1 Release Notes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjwfvjvomzw)
- [Interface Builder 3.1 Release Notes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjwfvjvonbu)
- [Interface Builder 3.0 Release Notes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjwfvjvonjv)

### Interface Builder 3.2 Release Notes

Interface Builder 3.2, included with the Xcode 3.2 toolset, is available only with Snow Leopard and is not supported in previous versions of Mac OS X.

### Summary of Changes in Interface Builder 3.2

### General

- There is a new tab in the Library that allows you to browse all of the classes available to add to your document. You can drag these from the Library to quickly instantiate them; as well as add actions and outlets and get information about classes. For more information, see [The Library's Classes tab](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjwfvjvomi).
- The Interface Builder Cocoa library now includes `NSViewController`, a reusable controller class that manages a view, typically loaded from an Interface Builder document.
- The Library contains a custom cell template to allow you to add your own cell types to a `NSTableColumn`, for example.
- If an Xcode project contains AppleScript files, Interface Builder will parse them and make their outlets and actions available. For more information, see [Integration with the AppleScript to Objective-C Bridge](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjwfvjvomzv).
- Interface Builder and ibtool both run 64-bit natively. If you open a Carbon NIB file, Interface Builder and ibtool will relaunch automatically in 32-bit mode. For more information, see [64-bit Interface Builder](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjwfvjvomzr).
- Development for new AppleScript Studio projects is no longer supported in Interface Builder. NIB files with AppleScript Studio objects will still be editable.
- The document window's browser mode now supports copy, cut, paste, and multiple selection.

### Inspectors

- Hovering over a control for an object's property in an inspector displays a tooltip with the documentation that includes the method name for that property. (Previously, only the documentation was given.)
- The Identity inspector has a table of Used Defined Runtime Attributes, which allow you to add additional key/value pairs to an object. At runtime, `setValue:forKey:` will be called on the object for each key-value pair in the User Defined Runtime Attributes table.
- Double-clicking an object that does not have a visual editor (such as an `NSObject` in the top-level of a document) will open the inspector for that object.
- The Identity inspector now supports assigning custom color labels to objects. Setting a color label for an object will cause its representation to be highlighted with that color in the document window.

### Interface Builder Plug-ins

- Developers can add their own size inspectors with the `ibPopulateSizeInspectorClasses:` method. For more information, see [Adding your own size inspectors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjwfvjvomzs).
- Because instances of NSImage returned by `-[IBDocument documentImageNamed:]` no longer have their `-[NSImage name]` value set, plug-ins that work with images returned by `-[IBDocument documentImageNamed:]` and subsequently read the image's name via `-[NSImage imageName]` must switch to using `-[IBDocument nameForDocumentImage:]`.
- Classes integrated through an Interface Builder plug-in can dicate when their children are removed and how the removal takes place with the new object integration API: `ibCanRemoveChildren:` and `ibRemoveChildren:`. For more information, see [Determining if and how children are removed from classes integrated with Interface Builder plug-ins](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjwfvjvomzt).

### Connections

- Copying an object copies certain actions, outlets, and/or bindings. The default paste maintains the copied connections, but you can use the Paste Without Connections menu item to paste without maintaining connections. For more information, see [Copying and pasting objects with connections](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjwfvjvomzu).
- Type-selection is supported in the connections popups and the connections panel.
- Control dragging a connection between two objects indicates which outlets or actions are already connected. A previous identical connection is indicated with a solid dot (•), while a connection for the same outlet or action, but to a different object is indicated with a dash (-).

### Working with Objects in the Design Canvas

- When resizing views:

  - The view's new size is displayed in a small HUD for easy reference.
  - Holding down the shift key maintains the view's original proportions.
- The system color panel can now be used to directly modify the color of selected controls.
- If the Show Clipping Indicators option is enabled in the Layout menu, controls with truncated text will be clearly marked with a "+" button. Clicking this button resizes the control to fit the truncated text.
- Guides can be disabled using the Snaps to Guides option in the Layout menu. Use this to enable or disable guides when dragging and resizing.

### ibtool and the Interface Builder NIB Post-Processor

- ibtool can export the localizable strings of a document in XLIFF format (using the `--export-xliff` flag) and import an XLIFF document (using the `--import-xliff` flag) to apply its translations to a given Interface Builder document.
- Interface Builder 3.x NIB files contain files used only during development time. When a NIB file is released with a shipping product, the development-time files can be removed to make the NIB file smaller by using the Interface Builder NIB Post-Processor's Strip NIB Files build setting (`IBC_STRIP_NIBS`) in Xcode (`--strip` is the ibtool command line flag equivalent). By default, this is set to the value of the Interface Builder Compiler's Flatten Compiled XIB Files setting.

### Integration with Xcode

- If an Interface Builder document is part of an Xcode project, the document's deployment target will come from the Xcode project's SDK if the document's deployment target is set to "Default" in the Document Info window. You can override the project's deployment target by selecting a different target from the deployment target pop-up.
- If you’re working with multiple versions of Interface Builder, you can set the development target of an Interface Builder document. This should be set to the oldest version of Interface Builder used for development. For example, if you use an Interface Builder document feature that is only compatible on versions of Interface Builder equal to or newer than 3.2 (such as the User Defined Runtime Attributes), setting the development target to Interface Builder 3.0 will result in a document error. Additionally, if the development target is set to 3.2, for example, then the document will not be openable in versions of Interface Builder prior to 3.2.
- Interface Builder parses the header files in frameworks you have linked against in your Xcode project. Outlets and actions from framework classes will appear in an object's connections panel; and the classes found in the framework will be visible in the Classes tab. Interface Builder will also recursively parse the headers of sub-frameworks found in a linked framework.

### File Formats

- The XIB 3.2 file format introduces a more compact and readable structure for arrays, sets, and dictionaries. This will make XIB files more readable when doing SCM diff-ing operations, and in many cases can reduce the size of a XIB file. It is important to remember that XIB files may not be merged or edited by hand. The 3.2 XIB format is used only when the Development Target is set to Interface Builder 3.2 or later.
- Interface Builder documents can no longer be saved in the NIB 2.x file format. NIB 2.x files will automatically be upgraded to NIB 3.x files upon opening.

### Changes to Specific Controls

- You can set the identifier on a `NSToolbar` or an `NSToolbarItem` using its inspector. If no identifier is provided, then one will be automatically generated.
- A custom view's subviews now appear in the correct z-order when opened in Interface Builder 3.2. This order matches what is seen when the NIB file is loaded at runtime.
- OpenGL and layer-backed views now draw during drag and drop.
- Documents with OpenGL views…

  - where the renderer is set to Force Software Renderer will display an inconsistency warning when the document is opened for the first time in IB 3.2. The software renderer saved with older versions of Interface Builder was incorrect, and upon opening, IB 3.2 will automatically switch the software renderer to the correct value. Applications that depend on the exact value of an OpenGL view's renderer should note that Interface Builder saves the renderer ID as `kCGLRendererGenericFloatID` (`0x00020400`), not `kCGLRendererAppleSWID` (`0x00020600`) as versions prior to 3.2.
  - where the number of samples is set will display an inconsistency warning when the document is opened for the first time in IB 3.2. In versions previous to IB 3.2, the number of samples was set without setting the number of sample buffers; resulting in no sampling to occur at runtime. This is automatically fixed in any OpenGL view that is opened with IB 3.2. Make sure that your application still behaves correctly after opening and re-saving your documents with IB 3.2.

### Details About Enhancements in Interface Builder 3.2

### The Library's Classes tab

The Classes tab in Interface Builder's Library contains all of the classes IB has parsed from your Xcode project, linked frameworks, system and user plug-ins, and manually added headers. The Classes tab offers a one-stop location for class management. With it, you can:

- __Instantiate classes.__ Interface Builder matches each class in the Classes tab to the closest corresponding template in the Objects tab of the Library. For example, if you have a custom class in your Xcode project called `MyButton`, dragging it out of the Library would create a `NSButton` instance and set the custom class to `MyButton` automatically. If you have another class called `MyButtonSubclass` which is a subclass of `MyButton`, dragging it from the Library would also have the same effect as dragging a `NSButton` instance from the Objects tab and setting the custom class. However, if you were to create an Interface Builder plug-in containing a `MyButton` template, then dragging out `MyButtonSubclass` would instantiate a `MyButton` instance and set the custom class to `MyButtonSubclass`.
- __View a classes's inheritance.__ To see the inheritance of a class, select it in the Classes tab and select the Lineage detail view at the bottom of the window. If you have selected `NSView`, for example, the inheritance would read `NSView` → `NSResponder` → `NSObject`. The class at the bottom of the list is the root class.
- __See where a class is defined.__ Each class in Interface Builder's classes tab is made up of one or more descriptions. Each description comes from a different source (such as a header file, plug-in, etc). For example, if you add an action to the class `NSApplication` from a file in your Xcode project, then the two sources for the class are the built-in Cocoa plug-in and the header you have defined the action in. You can view the definitions and sources for any class with the Definitions detail view in the Classes tab window.

  > [!NOTE]
  > 

  The possible sources in the Definitions tab are:

  - Plug-ins — user or system plug-ins.
  - Frameworks — frameworks or sub-frameworks linked by your Xcode project.
  - Project — headers in the Xcode project associated with your Interface Builder document.
  - Imported Headers — headers you have manually added to your document (either by dragging in or by using the Read Class Files menu item).
  - Document — changes made in Interface Builder only (such as using the Outlets or Actions detail views to add an outlet or action).
- __Add actions and outlets to a class.__ Adding actions and outlets to a class does not require an instance of that class, and you can simply add outlets and actions to a class from within the Outlets and Actions detail views of the Classes tab.
- __Creating new classes.__ If you need a new subclass of any available class, you can right click that class in the Classes tab or use the action menu and select the Subclass menu item. This will create a new subclass and optionally generate source files for the class to add to your Xcode project. If you needed a subclass of `NSButton`, for example, right click on `NSButton` in the Classes tab, select the Subclass menu item, and then enter the class name. Now you can drag out your new subclass right into your document without needing to switch to Xcode.
- __Write updated class files.__ If you have made changes to a class in Interface Builder (denoted by having a This Document definition in the Definitions detail view), you can write those changes back to disk by right clicking the class in the Classes tab or using the action menu and selecting Write Updated Class Files.

> [!NOTE]
> 

### 64-bit Interface Builder

Interface Builder 3.2 will launch in 64-bit mode on supported hardware. Developer plug-ins should be compiled 64 and 32-bit Universal. If you open a document that contains objects from a 32-bit only plug-in (such as Carbon), then Interface Builder will relaunch automatically in 32-bit mode.

### Adding your own size inspectors

With IB 3.2, you can add custom size inspectors for the classes integrated with your Interface Builder plug-ins. This is done much in the same way as attribute inspectors. In the integration file for your class, implement the `ibPopulateSizeInspectorClasses:` method. In this method, you will add the class for your class's size inspector to the array of existing size inspector classes.

An example implementation of `ibPopulateSizeInspectorClasses:` may look like this:

```objc
#import <InterfaceBuilderKit/InterfaceBuilderKit.h>
#import "MyControlSizeInspector.h"
#import "MyControl.h"

@implementation MyControl (MyControlIntegration)

//...

- (void)ibPopulateSizeInspectorClasses:(NSMutableArray *)classes {
    [super ibPopulateSizeInspectorClasses:classes];
    [classes addObject:[MyControlSizeInspector class]];
}

@end
```


### Determining if and how children are removed from classes integrated with Interface Builder plug-ins

When developing Interface Builder plug-ins, you can use the following methods to determine if and how the children of your custom classes are removed:

- `ibCanRemoveChildren:` — return `NO` if any of the objects in the passed in set cannot be removed; otherwise return the super class's implementation (`[super ibCanRemoveChildren:objects]`).
- `ibRemoveChildren:` — if ibCanRemoveChildren returned `YES`, then this method is called do to the actual child removal.

For example, if you have a control (`MyOneComponentControl`) that you want to always have at least one subcomponent (or child), you would implement `ibCanRemoveChildren` and `ibRemoveChildren` in the following way:

```objc
#import <InterfaceBuilderKit/InterfaceBuilderKit.h>
#import "MyOneSubviewControl.h"

@implementation MyOneComponentControl (MyOneComponentControlIntegration)

- (BOOL)ibCanRemoveChildren:(NSSet *)objects {
    // assure there will always be at least one subview.
    BOOL willHaveAtLeastOneComponent = ([[[NSSet setWithArray:[self components]] setBySubtractingSet:objects] count] >= 1);
    return willHaveAtLeastOneComponent && [super ibCanRemoveChildren:objects];
}

- (void)ibRemoveChildren:(NSSet *)objects {
    [self removeComponents:[[NSSet setWithArray:[self components]] setByIntersectingSet:objects]];
    [super ibRemoveChildren:objects];
}

@end
```


### Copying and pasting objects with connections

When a set of objects is copied to the pasteboard, the connections (outlets, actions, and bindings) between those objects are maintained. In Interface Builder 3.2, the connections to and from those objects to other objects that aren't included in the set being copied and pasted are also maintained in the following cases:

- __Bindings are copied.__ For example, if you copy a check box that has a value binding bound to an array controller, pasting the check box maintains the value binding. However, if you were to copy and paste the array controller, the existing check box's value binding would not be modified.
- __Sent actions are copied.__ For example, if you copy and paste a button that calls `showConfigurationPanel:` on the application delegate, the `showConfigurationPanel:` action will be pasted as well. If you copy and paste the application delegate, the button's action will not be modified.
- __Outlets are copied.__ For example, if you copy a table view that has a data source set, then pasting the table view would maintain the data source outlet. However, if you were to copy and paste the data source object, the existing table view's data source would not be modified.

To paste objects without maintaining any connections, use the "Paste Without Connections" menu item or use the Option-Command-V (⌥⌘V) key equivalent.

### Integration with the AppleScript to Objective-C Bridge

Snow Leopard contains a new AppleScript/Objective-C bridge named AppleScriptObjC, similar to the bridges for Python and Ruby. Interface Builder can read and write AppleScript source files for use with AppleScriptObjC, making connections simpler to use by making the outlets and actions from your AppleScript classes available. In addition, you can generate AppleScript source files from classes you create in Interface Builder (from using the Subclass feature of the Library's Classes tab).

For details on using AppleScriptObjC, see the _[AppleScriptObjC Release Notes](https://developer.apple.com/library/archive/releasenotes/ScriptingAutomation/RN-AppleScriptObjC/index.html#//apple_ref/doc/uid/TP40008853)_.

### Interface Builder 3.1.1 Release Notes

### Enhancements

### UIViewController NIB Name

The UIViewController attributes inspector's NIB Name combo box auto-populates and completes with the names of Interface Builder documents from the project containing the edited document. The design window for a view controller also contains a hyperlink that can be used to quickly navigate to the nib file loaded by a view controller.

### UIScrollView

The Interface Builder library has been updated to contain an instance of UIScrollView for direct use in Interface Builder documents. To use a scroll view in a nib file, simply drag it from the library window, configure it with the inspector, and then optionally add subviews in Interface Builder or provide content at runtime. Remember to set the scroll view's content size at runtime.

### Simulated Metrics Support for Top-Level UIViews

To aid in laying out UIViews that are loaded from UIViewControllers, this release of Interface Builder introduces the concept of simulated metrics for top-level UIViews. The simulated metrics allow you to specify the styles of the various bars that will be present on the window that will house the view that is being designed. For example, while working with a view that is intended to be loaded by a view controller that will be used in a tab bar controller, the simulated bar metrics can specify a simulated status bar and a simulated tab bar. In addition to giving a more accurate visual preview of the final interface, the simulated metrics will also constrain the layout of the view and aid in correct alignment and positioning of the subviews. The simulated metrics have no bearing on the view at runtime, they are simply a visual aid at design time.

### Simulated Rotation Support for Top-Level UIViews

With this release of Interface Builder, UIViews have the same rotation preview control that UIWindows have. A top-level view's title bar presents a rotation button in the upper-right corner. Clicking the rotation button provides a preview of how the rotated view will look at runtime. This feature is intended to be used to validate the auto-resizing settings of the subviews of the top-level view.

### Known Issues

### CompileXIB Fails Because of Missing Plug-ins

If the Xcode CompileXIB build step fails because of a missing plug-in, follow these steps to workaround the issue:

1. Open the xib file that is failing to build. Interface Builder should prompt you to load the missing plug-in.
2. Choose to locate the plug-in and navigate to `/System/Library/Frameworks`.
3. Choose the framework for the missing Interface Builder plug-in. See the table below for a list of plug-ins and their related frameworks.
4. Save the document and quit Interface Builder.
5. Return to Xcode and rebuild.

|
|  |
| AddressBook | com.apple.AddressBook.ibplugin | AddressBook.framework |
| Automator | com.apple.automator.AutomatorPalette | Automator.framework |
| ImageKit | com.apple.imagekit.ibplugin | Quartz.framework |
| QuartzComposer | com.apple.QuartzComposerIBPlugin | Quartz.framework |
| PDFKit | com.apple.pdfkit.ibplugin | Quartz.framework |
| QTKitIB | com.apple.QTKitIBPlugin | QTKit.framework |
| OSAKit | com.apple.OSAKit.IBPlugin | OSAKit.framework |
| DiscRecording | com.apple.InterfaceBuilder.DiscRecordingPlugin.ibplugin | DiscRecordingUI.framework |

### Interface Builder 3.1 Release Notes

### What’s New

### Cocoa Touch Support

- Interface Builder now supports creating interfaces for Cocoa Touch applications.

### General

- Selection menu for selecting any object under the mouse in the design canvas
- Support for (re)focusing the connections window on the endpoint of a particular connection.
- Localizable string management, including find and replace of values across multiple documents
- Support for drag-based reordering in the outline view
- Support for adding, deleting, reordering, and inserting into split views, tab views, and table views
- Auto-selection of matching actions and scroll wheel support in the connection window
- Auto-configuration of views (geometry, control size, and so on) when dragged from the library to the design surface
- Addition of `OTHER_IBTOOL_FLAGS` build setting, for specifying additional build-time arguments in Xcode
- Changes to the layout of the XIB file format to make diffing easier
- Menu for navigating to the Human Interface Guidelines
- First Responder now shows all defined actions.

### Cocoa Touch Support

### FAQ: How does UIViewController’s Autoresizes View To Fill Screen work?

- This property instructs the view controller’s view to grow to fill the screen’s application frame, when the NIB is loaded.

### FAQ: How do I re-order or modify the sub-controllers in a UITabBarController?

- You can re-order or modify the subcontrollers in a UITabBarController by using the UITabBarController’s attributes inspector.

### FAQ: How do I create a ‘Plain’ style UITableView?

- You can change the style of a table view by using the style popup of the UITableView inspector. The item in the popup label ‘indexed’ corresponds to the UITableViewStylePlain style.

### FAQ: How do I use View Controllers?

- Interface Builder now supports designing view controller hierarchies. Tab bar controllers and navigation controllers both support embedding child view controllers. Tab bar controllers support a variable array of of child view controllers, each with their own tab bar item. You can visually edit a view controller, tab bar controller, or navigation controller by double clicking on it from the document window. To add additional view controllers to a tab bar controller, drag a view controller from the library to your tab bar controller's editing window. Navigation controllers support one child view controller, the root item in the navigation hierarchy. Additional view controllers can be pushed to and popped from the navigation controller at runtime.

  Many application will be composed entirely of a hierarchies of view controllers. Interface Builder will allow you to embed many view controllers in one document, however, you need to take care not to build your entire Interface in one document. Doing so would imply loading an application's entire user interface at once. This will result in poor performance and slow launch times. Instead, take advantage of the 'NIB Name' property of `UIViewController`. In the `UIViewController` attribute inspector, there is a 'NIB Name' property. If you set this property, then when the `UIViewController` is instantiated from the edited document at runtime, it won't immediately have a controlled view. Instead it will load the view on demand from the NIB file named in the attribute inspector. To facilitate this on-demand loading, create a second Interface Builder document and mark the `File's Owner` to have the same class as your view controller. Next, create a view in your second document and attach `File's Owner's` 'view' outlet to the view. When your original view controller is loaded at runtime, and it becomes time to fault in that view controller's view, it will load this secondary NIB. Using the 'NIB Name' property of view controllers in Interface Builder is most effective with the child controllers of tab bar controllers.

### FAQ: How do I add an Action to my object?

- Open the object’s Identity inspector, and click the “+” button in the Class Actions section
- Cocoa Touch Class Action inspector now supports two forms of action selectors
- The single argument style: `-(IBAction)someAction:(id)sender`

  To use this style, type the following into the inspector: “`someAction:`” and press return.
- The two argument style: `- (IBAction)someAction:(id)sender withEvent:(UIEvent *)event`

  To use this style, type the following in the inspector: “`someAction:withEvent:`” and press return.
- The Objective-C parser used with Cocoa Touch documents will parse both single and double argument actions.

### FAQ: How do I configure my Cocoa Touch application to load a NIB file automatically?

- Add a new key to your `Info.plist` called `NSMainNibName`.
- The value of this key should be a string containing the name of the NIB file you would like to use -- such as the "MainWindow".
- The naming convention of this NIB is typically along the lines of `YOURAPPNAME_MainWindow.nib`.
- The `.nib` extension is not required in the `Info.plist`.

### FAQ: How do I edit a Cocoa Touch view controller?

- Drag a view controller object from the library into the document window.
- In the document window, double-click the icon for the view controller object to open its editor.
- Drag & and drop views, navigation items, and tab bar items from the Library onto the editor.

### FAQ: How do I rotate a Cocoa Touch window to simulate the user rotating a device?

- Windows have a new button in the upper right corner.
- By default, windows use the portrait aspect ratio. Clicking the corner button rotates the window 90º into landscape mode.
- Clicking the rotate button again reverses the rotation.
- Note that View Controller also support rotation within IB.

### FAQ: What is a Proxy Object, and how do I configure a it?

- Proxy Objects represent objects that exist outside of your NIB file.
- You can make connections to and from Proxy Objects in Interface Builder and have them resolve to objects specified at run-time.
- To use a proxy object, drag a Proxy Object from the Interface Builder Library to your document window.
- Configure the class of the Proxy Object using the Identity Inspector.
- Set the Name property of the Proxy Object. This value should be unique on a per-NIB basis.
- To facilitate the replacement at runtime, do the following in your NIB-loading code:

  1. Create a dictionary add add the actual object to the dictionary, using the value you put in the Name property of the Proxy Object as the key. (If your NIB file includes more than one Proxy Object, include all of the objects and Name keys in the same dictionary.)
  2. Create another dictionary and associate your proxy-object dictionary with the `UINibProxiedObjectsKey` key.
  3. Pass this second dictionary into the _options_ parameter of the `loadNibNamed:owner:options:` method of `NSBundle`.

### FAQ: What is different about NIB loading in a Cocoa Touch application?

- Top level NIB objects are auto-released. (In Mac OS X, top levels objects are retained by default, and hence must be released explicitly on that platform.)
- Outlets are set using the `setValue:forKey:` method. This method retains outlets automatically, so if you use it, you must release those outlets in the object’s `dealloc` method.
- The `awakeFromNib` message is sent to each object that was created as a side effect of loading the nib. This means that on the iOS `File’s Owner` and other `proxy objects` do not receive this message. Please refer to the `CocoaTouch` or `Cocoa` documentation for a complete list of methods available for configuring your UI objects after NIB loading has occurred.

### Known Cocoa Touch Issues

- Not all of the fonts available in Mac OS X are available in iOS.

### General Support

### FAQ: What does refocusing the connections window mean?

- Refocusing the connections window is a speedy way to view what objects the endpoint of a particular connection are connected to. For example, if you are viewing the connections for a menu item, you see that it is connected to the First Responder via an action. Let's say you want to see what other actions are also connected to the First Responder. Simply select (by single-clicking) the First Responder endpoint next to the connection of your menu item's action, and then click the refocus button that appears to the left of the connection button or double click the endpoint's label.
- Having the ability to refocus the connections window eliminates the need to move to the endpoint of an object in the design canvas or document window in order to view what connections exist on that endpoint.
- Refocusing works much in the way a browser behaves when navigating web pages. As you continue to recursively refocus, you can move back and forward through the history of your refocuses using the navigation buttons in the upper left corner of the connections window.

### FAQ: What does selecting a connection's endpoint in the connections window do?

- The connections window now has a concept of selection like other windows in Interface Builder. When you select a connection's endpoint, the lineage of that endpoint (i.e. Window -> Content View -> MyView) is displayed in a path control at the bottom of the window. Secondly, the inspector tracks the selection you just made. This makes it easy to make changes to objects that are visible in the connections window without having to select them in the document window or open them in the design canvas. And finally, selecting a connection's endpoint reveals the refocus button, allowing you to refocus the connections window on that endpoint.

### FAQ: How do I use the selection menu to select objects?

- The selection menu allows you to select any object you see on-screen, regardless of whether or not objects overlap or are hidden.
- To bring up the selection menu, you can either shift right-click (shift-control left-click) over the object(s) you wish to select from.
- Once the selection menu appears, it will contain all of the objects that were under the mouse at the time you brought up the menu.
- Once you find the object you wish to select, click it.

### FAQ: Why did my window disappear when resizing it?

- While the maximum size constraint of windows with a zero max size and the "Has Maximum Size" checkbox enabled was previously ignored, Interface Builder 3.1 now enforces this constraint for any values considered valid by the NSWindow API.

### FAQ: How do I find and replace all instances of a string in my document?

- Bring up the Strings window using the Tools -> Strings menu item (Control-S).
- Select the appropriate document scope using the popup in the upper left (all documents or a selected document).
- Enter a string in the search bar to filter the available strings, if necessary.
- Enter the "Find" mode by selecting the Edit -> Find menu item (Command-F).
- Change the popup from "Find" to "Find and Replace".
- Enter the string to find, and its replacement string, in the available fields.
- Use the arrow keys to locate each match. Use the "Replace" buttons to the right to replace the values.

### FAQ: How do I edit using the strings window?

- The strings in the table can be edited in place simply by double-clicking on the value.
- Double-clicking on items in other columns takes you to the associated object on the design surface.

### FAQ: How do I extract content from the strings window?

- Dragging or copying rows from the table view in the strings window produces text in the form of a strings file entry.

### Known General Issues

- In the connections window, you cannot select connection endpoints that are fixed, such as the menu of an NSPopUpButton or a formatter of an NSTextField or NSTextFieldCell.

### Interface Builder 3.0 Release Notes

### General

- __Supported configurations__

  Interface Builder 3.0 runs on Mac OS X 10.5 (Leopard).
- __IB2 Palettes do not work with IB3__

  Based in part on developer feedback and adoption, Interface Builder 3 provides a new, much simpler and more flexible plug-in model for integrating custom views and controls into the application. Please see the section on Additional Documentation and Help.
- __Loading Plug-ins__

  To load an Interface Builder 3.0 plug-in, click on the Plus button in the Plug-ins section of the preference pane. Plug-ins are now built into their frameworks, so you need to navigate to the framework that contains the plug-in. Alternatively, you can also drag-and-drop a plug-in into the Plug-ins preference pane.
- __xibtool has been replaced with ibtool__

  Please see the ibtool man page for more documentation. The following is information not included in the man page.

  - __ibtool Property Plists__

    There are two new options in ibtool that enable you to export the properties of a nib to a plist, change their values and import the new values back into the plist.

    - __Exporting: --export__

      For each object in the nib, export the properties specified in a specified XML property list to an output property list. The property list should contain a dictionary of class name arrays containing strings of key paths for properties. The output is a dictionary in XML property list format where each key is an object ID, and each value is a dictionary of key paths and their associated value. If a key in the second level dictionary begins with a `.`, it isn't a key path. Currently, the only special key is `.nilKeypaths`. It identifies an array of key paths whose value was `nil`. For example,

```
ibtool --export Simple.plist Simple.nib > output.plist
```

      exports the properties of `Simple.nib` specified by `Simple.plist` into a file named `output.plist`.
    - __Importing: --import__

      For each object in the nib identified by the contents of an imported property list, take the properties specified in the property list and apply them to the object. The imported property list is in the same format as the output of the `--export` command. Be aware that setting a property may have the side effect of not actually changing the property or possibly altering additional properties. Typically this option is combined with `--write`. For example,

```
ibtool --import Simple.plist --write NewSimple.nib Simple.nib
```

      applies the `Simple.plist` changes to the `Simple.nib` file and creates a new nib named `NewSimple.nib`.
  - __Example__

    The following example is run on a nib with an NSButton, NSTextField, and an NSTextView inside of an NSWindow. This example demonstrates how to extract strings as well as geometry from the nib. One thing to note, the `className` property on NSObject is only used here to make reading the resulting plist easier. The `className` property is an example of a property that cannot be changed, so the resulting plist cannot be fed back into ibtool without removing all references to `className` first.

    This example demonstrates how to extract the geometry of the whole frame, the frame origin, the frame width, and the frame height. These could just as easily be replaced or supplemented with other requests such as

```
<string>frame.origin.x</string>
<string>frame.origin.y</string>
<string>frame.size</string>
<string>subviews.frame</string>
<string>subviews.subviews.frame</string>
```

    They could also be moved up the hierarchy to NSView if you need the properties for all subclasses of NSView.

    The following plist is used for extracting information from the nib.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>NSButton</key>
    <array>
        <string>keyEquivalent</string>
        <string>keyEquivalentModifierMask</string>
        <string>title</string>
    </array>p
    <key>NSObject</key>
    <array>
        <string>className</string>
    </array>
    <key>NSTextField</key>
    <array>
        <string>editable</string>
    </array>
    <key>NSTextView</key>
    <array>
        <string>frame</string>
        <string>frame.origin</string>
        <string>frame.size.width</string>
        <string>frame.size.height</string>
    </array>
    <key>NSView</key>
    <array>
        <string>hidden</string>
    </array>
</dict>
</plist>
```

    The following is the resulting plist.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>-1</key>
    <dict>
        <key>className</key>
        <string>FirstResponder</string>
    </dict>
    <key>2</key>
    <dict>
        <key>className</key>
        <string>NSView</string>
        <key>hidden</key>
        <integer>0</integer>
    </dict>
    <key>21</key>
    <dict>
        <key>className</key>
        <string>NSWindow</string>
    </dict>
    <key>249</key>
    <dict>
        <key>className</key>
        <string>NSTextField</string>
        <key>editable</key>
        <integer>1</integer>
        <key>hidden</key>
        <integer>0</integer>
    </dict>
    <key>339</key>
    <dict>
        <key>className</key>
        <string>NSButton</string>
        <key>hidden</key>
        <integer>0</integer>
        <key>keyEquivalent</key>
        <string>m</string>
        <key>keyEquivalentModifierMask</key>
        <integer>1048576</integer>
        <key>title</key>
        <string>Withdraw</string>
    </dict>
    <key>340</key>
    <dict>
        <key>className</key>
        <string>NSScrollView</string>
        <key>hidden</key>
        <integer>0</integer>
    </dict>
    <key>341</key>
    <dict>
        <key>className</key>
        <string>NSTextView</string>
        <key>frame</key>
        <string>{{0, 0}, {149, 56}}</string>
        <key>frame.origin</key>
        <string>{0, 0}</string>
        <key>frame.size.height</key>
        <real>56</real>
        <key>frame.size.width</key>
        <real>149</real>
        <key>hidden</key>
        <integer>0</integer>
    </dict>
</dict>
</plist>
```
  - __Known Issues with plist import and export__

    - The properties of NSWindow are not accessible with the plist export and import at this time.
    - There may be unavoidable side effects of changing property values. Changing one property may also change a related property in that control.
    - Some controls may not allow certain properties to be changed.
    - Importing property values from a plist does not cause the controls to size to fit. For example, changing the title of a button does not change the size of the button to fit the new text.

### File Format and Compatibility

- __XIB files are not human editable__

  XIB files are the result of writing an in-memory object graph to disk, by using a custom serialization protocol. Editing XIB files by hand is not suggested, extremely dangerous, and can lead to corrupted interfaces
- __XIB 3.x and NIB 3.x files are not backward compatible for development__

  There are some features that can only be developed using the XIB 3.x or NIB 3.x formats. Support for these features—such as support for toolbars, and the promotion of cells to first-class citizens—either required underlying changes in AppKit to support, or introduced new content into the document hierarchy that previous versions of Interface Builder cannot handle. Interface Builder 3.0 includes an automatic compatibility check, performed before saving, which will inform you of items which affect the file format compatibility.

### Process

- __Adding a Core Data Entity to IB3__

  To create an interface to your Core Data model, drag the Entity object from the Library to your Document Window. This brings up a wizard that steps you through the configuration process.
- __How to make connections__

  You can still make connections by control-dragging between objects, but we highly recommend you try control-clicking. Control-clicking an object brings up a context-sensitive display allowing you to make action, outlet, or accessibility connections.
- __Layout validation is now automated__

  The Layout Validation menu item has been removed because it happens automatically now. Use the Information Window available from the Document Window to see all warnings and errors for your document. You can change the categorization of warnings, errors, and notes in the preference pane.
- __Moving an object without breaking connections__

  When you copy a group of objects, only connections internal to that group go onto the pasteboard. Because of this, copying and pasting objects typically breaks connections. To move a view, rather than copy and paste it, you need to Pop-and-Drag. Select a group of views, click, and hold without moving the mouse. The views will lift off the window and you can move them. As long as you keep them in the same document, their connections won't break.
- __Grouping__

  The Group menu item has been removed. To group objects together, you can contain them in a custom view. You can also store a custom view as a top-level item in your document window, or you can pop-and-drag it back to the library to store it for reuse.
- __Adding classes, actions, and outlets.__

  The preferred workflow is to create your classes in Xcode. You can then use the Identity Inspector to set the custom class of an object and the header file will be automatically synced when your code changes. However, if you prefer, you can specify a new class in the Identity Inspector and use the Write Class Files... menu in the File menu to generate files for you. In the Identity Inspector, you can add custom actions and outlets then copy/paste, drag and drop, or use the menu to create the definitions in your header file.
- __Image resources cannot be stored in a NIB.__

  The practice of storing image resources such as TIFF files in NIBs has been discouraged for a number of releases. Interface Builder 3 no longer recognizes resources that are stored in a NIB.

### Summary of New Features

- __General__

  - There is a new connection context menu. Control-click to see a list of actions, outlets, and accessibility connections that can be made. Drag from the circle to the item to make the connection to. As you mouse over the interface, only items that can complete a connection are highlighted.
  - Decompose Interface—available in the File menu—breaks your interface into smaller nibs. Smaller nibs ensure faster loading of your application by only loading interface items that are needed.
  - You can use the tab key to access each of the widgets in your view sequentially.
  - There are new menu items for selecting the parent, child, and siblings of the selected control. This aids in accessing those hard to reach controls like Scrollers.
  - Holding the shift key while resizing a view allows you to restrain the resizing to horizontal, vertical, or proportional.
  - The option key can be toggled while resizing to show layout information.
  - Use the Enable Autoresizing menu item in the Layout menu to allow views to resize with their top-level containing view according to their springs and struts. Holding the command key while resizing a top level view inverts the sense of the menu item and can be toggled.
- __File Formats__

  There are three development-time file formats:

  - XIB 3.x file

    A XIB file is a flat version of a nib file, encoded in a human readable XML format. When used with the Xcode v3.x toolchain, they are compiled during the build phase into a flat NIB file—a NIB with just the keyedobjects.nib data. The resulting file is deployable on any recent Mac OS X version, but cannot be opened for development as it is just a deployment file.
  - NIB 3.x wrapper

    These are wrappers ending in .nib that contain two files: designable.nib and keyedobjects.nib. These files can only be opened with Interface Builder 3. However, the keyedobjects.nib file in the wrapper is the same format as the NIB 2.x wrapper, and thus these are deployable on any recent Mac OS X version.
  - NIB 2.x wrapper

    These are wrappers, ending in .nib that contain three files: classes.nib, info.nib, and keyedobjects.nib. These files can be opened for development with any version of Interface Builder. Only the keyedobjects.nib file is required at runtime, and these files are deployable on any recent Mac OS X version.
- __Document Window__

  The document window has been updated with the following items:

  - Command double-clicking on anything in the Document Window jumps to the appropriate header file.
  - A new search field you can use to search for objects by name, id, or type.
  - A browser mode in addition to the existing icon and outline mode.
  - A rearrangeable icon view of top level objects. This allows for grouping of related items.
  - A status bar showing what Xcode project a nib file is related to, whether that project is currently available, and if there are any warnings or errors. Warnings and errors may be viewed by clicking on the information button at the top of the document window.
- __Library__

  The Palettes have been replaced by the concept of a Library to hold all of your controls and media. The Library adds a lot of functionality such as

  - A search field for quickly finding controls.
  - Smart groups to assemble common controls.
  - User-defined groups to organize your favorite controls, controls specific to a project, or your customized controls. Drag any configured control back to the Library to save it in one of your user-defined groups.
  - Icon; Icon and Label; and Icon and Description mode available in the pull-down menu in the lower left corner of the Library. You can choose what level of documentation you would like to see, including a detail view explaining how to use the control you’ve selected. Icon mode saves space. Icon and Label mode shows you the icon and the label to help aid you in searching. Icon and Description mode shows you the icon, label, and a short description explaining how to use the control.
- __Inspectors__

  There are a number of new features available in the Inspector window such as

  - Support for multiple selection. Select any set of controls and you can edit any of their common properties.
  - Documentation tooltips for properties in the Inspector.
  - A realtime animation showing how the selected control will behave based on the springs and struts set in the Size Inspector.
  - Copy/Paste Attributes is available in the Edit menu.
  - Per object notes that allow you to leave detailed information for other developers, or for yourself in the future. These notes show as tooltips when you hover over the control in Interface Builder.
- __Xcode Integration__

  There are a number of new ways that Interface Builder integrates with Xcode when the related Xcode project is open. For example,

  - Automatic synchronization of headers.
  - Loading of resources into the Library Media Browser.
  - Warnings and errors in Xcode when a XIB is built. You can set the priority of notices, warnings and errors in Interface Builder’s preference pane.
  - New templates in Xcode makes it easy to add new XIBs directly to your project.
- __Plug-ins__

  IBPalette has been replaced with a new Interface Builder Plug-in model. See the documentation links in the Additional Documentation and Help section of this document for instructions on creating a new Interface Builder Plug-in.
- __Cocoa Specific__

  Interface Builder 3 adds new support for the following Cocoa controls and functionality:

  - Core Animation
  - Toolbars
  - Tree Controller
  - Dictionary Controller
  - Path Control
  - 10.4+ Formatters
- __Carbon Specific__

  Interface Builder 3 now provides HIView subclassing for all Carbon views.

### Known Issues and Workarounds

- __Undo and Multiple Value Placeholder Binding__

  Undoing edits on the Multiple Value Placeholder value results in an entire binding being removed.
- __Smart Groups of Carbon Elements__

  The smart group rule “Is kind of” doesn’t respond to Carbon class names. Try the Cocoa counterpart if available.
- __Carbon Library__

  The Carbon library is missing a vertical slider element.
- __Carbon Tab Views__

  Carbon tab views appear distorted within Interface Builder.
- __Mini Carbon Controls__

  Mini-sized Carbon controls don’t have the correct height and may not be usable when simulated.
- __Carbon Nibs from Interface Builder 2__

  Various Carbon controls in Nibs created with previous versions of may have incorrect layout rectangles.
- __Carbon Controls with Text__

  Carbon Controls with text don’t have layout baselines for text alignment.
- __Removing Classes from Nibs__

  There is no method for removing a class from a Nib. If the class is removed from the Xcode project, it’s automatically removed from the Nib.
- __Renaming Methods Removes Connections__

  Renaming a method in a header file breaks its connections in Interface Builder. You need to update each connection to point to the new method name.
- __Categories and Classes in a Header File__

  Interface Builder displays only category information when both a class and a category are present in a header file.
- __Hidden Scroll Bars__

  Unhiding hidden scroll bars doesn’t show them.
- __Using ibtool’s --convert Flag__

  Using the `--convert` flag with `ibtool` fails when new class name already exists.
- __Localized Formatters__

  Localized formats may not be used when running in a localized language.
- __Selecting Elements with Core Animation Effects__

  Elements with “Wants Core Animation Layer” active cannot be directly selected.
