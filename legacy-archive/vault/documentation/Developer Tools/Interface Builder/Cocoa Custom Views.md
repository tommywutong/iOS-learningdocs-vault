---
title: Interface Builder
apple_id: 10000179i
resource_type: Guide
platform: Xcode Developer Tools|macOS
topic: null
technology: InterfaceBuilderKit
published: '2007-04-05'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/IBTips/Articles/CustomViews.html
archived_at: '2026-07-15T07:24:35.773487Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Interface Builder](Introduction%20to%20Interface%20Builder.md)


[Next](Making%20Connections%20in%20Cocoa%20Applications.md)[Previous](Compatibility%20Checking.md)

# Cocoa Custom Views

One of the widgets provided with the Interface Builder palettes for Cocoa is the CustomView object, which is an instance of NSView. Because NSView is an abstract class, the CustomView object is usually used only as a stand-in for your own custom subclass of NSView,which will be instantiated at runtime.

Before you read this article, you should read “What Happens When a Nib File is Loaded,” which describes what happens to standard objects, custom subclasses of standard objects, and custom objects (subclasses of NSView) when a Cocoa nib file is loaded.

To add a custom subclass of NSView to your interface, open the Classes pane in the Nib file window, click on NSView in the class tree, and select Classes > Subclass NSView. (If you prefer, you can subclass one of the existing subclasses of NSView instead.) Give the subclass a name. Or, if you have an Xcode project linked to your Interface Builder file, you can write a header file for your custom view in Xcode and drag the header file into Interface Builder’s Nib file window.

Once you have defined your custom subclass, drag the CustomView widget from the palette into your design window. With the CustomView object selected, open the Custom Class pane of the Info window and select your subclass.

You can now make connections and set up targets and actions as you wish.

Because the code for your custom subclass is not resident in Interface Builder, you must first implement your custom subclass and build the program before you can test it. To implement your subclass, first be sure your project is open in Xcode. Then, select the subclass in the Classes pane of the Nib file window and select Classes > Create Files For _nameofsubclass_. (You can skip this step if you started by creating the header file in Xcode.) A stub header file and implementation file are added to Xcode, where you can add the methods you need to make the view functional.

Note that Interface Builder will continue to display the generic CustomView object (labeled with the name of your subclass). At runtime, when the custom view is unarchived, an instance of your subclass is created instead.

Because the default implementation of the `drawRect:` method for NSView does nothing, you must override this method if you want your custom view to be visible to the user. You must also override any event methods for events that interest you; the default implementations just pass the event on to the next responder. See the documentation for [NSView](https://developer.apple.com/documentation/appkit/nsview) for details.

To receive keyboard events, your custom view must accept first responder status. If your view needs preparation or cleanup as its responder status changes, or if it only accepts or relinquishes first responder status conditionally, you must implement the appropriate responder methods. See the documentation for [NSResponder](https://developer.apple.com/documentation/appkit/nsresponder) for more information.

As discussed in “What Happens When a Nib File is Loaded,” your custom view object’s `initWithFrame:` method is called when the window is first displayed. Only custom view objects receive this call; `initWithFrame:` is never called for custom subclasses of other objects. If you are not using a custom view object, you must implement a `-(void)awakeFromNib` method to handle any setup at runtime.

For example, suppose you create a subclass of NSOpenGLView and name it MyOpenGLView. You can add this subclass to your nib in either of two ways: you can add a CustomView widget to the design window and set its class to MyOpenGLview; or you can drag an NSOpenGLview widget into the design window and set its custom subclass to MyOpenGLview. Although the two methods seem very similar, the effect is quite different:

- If you use a CustomView object, then `initWithFrame:` is called when the window opens. However, because NSView is an abstract class, Interface Builder does not let you set any attributes in the Info window and you can’t test the object in Interface Builder’s Test Interface mode.
- If MyOpenGLview is set as a custom subclass of an NSOpenGLview object, the `initWithFrame:` method is never called for that object. In this case, on the other hand, Interface Builder’s Info window displays a set of attributes for NSOpenGLview that you can set for your custom subclass of that object.

You can use a custom view object as an accessory view for classes such as NSSavePanel. To do so, drag a CustomView widget from the palette into your Nib file window. It appears as a top level object and a small window opens, labeled “View.” You can add widgets to this window as needed. You must have an outlet in your controller for each object in the accessory view; use the Connections pane of the Info window to connect the outlets. You also have to add actions to objects as needed (buttons, check boxes, and so forth) and connect them to the appropriate controller. Remember to release the custom view when you’re done with it.

A similar use of custom views is as the content view for a drawer. If you want to create a new window with a drawer, you can just drag the composite drawer object (the one that has a window with a drawer sticking off the left side of it) off the window palette onto the desktop. The composite drawer object contains a main window, a content view, and an NSDrawer object that come pre-wired. On the other hand, if you want to add a drawer to an existing window, drag the NSDrawer object (the one that says Drawer) into the Nib file window and a CustomView widget onto the design window. Then connect the NSDrawer object’s `contentView` outlet to the custom view and its `parentWindow` outlet to the existing window. To test the interface, you can add a button to the design window and connect the button to the NSDrawer with the `toggle:` action.

You can also use custom views as simple containers of type NSView. To do so, drag a CustomView widget into your design window. Then, drag other widgets from the palette and drop them on the custom view. Or, you can select the objects that you want to group in the NSView container and select Layout > Make subviews of > Custom View. Using a custom view as a container allows you to manipulate the items in the view as a group. For example, you can make connections to the container and manipulate the items in the view at runtime. Or, you can swap out the contents of the custom view and replace them with the contents of another view.

The file’s owner is responsible for releasing any resources created by the nib. These include any top level objects such as formatters, custom views, extra windows, or extra menus. See “Releasing Nib File Objects” in “What Happens When a Nib File is Loaded.”

[Next](Making%20Connections%20in%20Cocoa%20Applications.md)[Previous](Compatibility%20Checking.md)

