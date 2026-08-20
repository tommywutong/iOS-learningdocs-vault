---
title: Cocoa Bindings Programming Topics
apple_id: 10000167i
resource_type: Guide
platform: macOS
topic: General
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/Tasks/onerelation.html
archived_at: '2026-07-15T07:12:21.886247Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Bindings Programming Topics](Introduction%20to%20Cocoa%20Bindings%20Programming%20Topics.md)


[Next](Filtering%20Using%20a%20Custom%20Array%20Controller.md)[Previous](Displaying%20Images%20Using%20Bindings.md)

# Implementing To-One Relationships Using Pop-Up Menus

You can implement an editable to-one relationship using an NSPopUpButtonCell or NSPopUpButton. That is, allow the user to select a menu item from a pop-up menu in order to change the destination object of a to-one relationship in your model.

This article extends the example presented in [Creating a Master-Detail Interface](Creating%20a%20Master-Detail%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsga4talkcineugqkejbbq) by adding a pop-up menu to the table view in the master interface. Instead of displaying the author’s last name in the Author column, you might allow users to select an author from a pop-up menu, as shown in Figure 1. Note that if you display just the last name, you have essentially flattened the to-one relationship. Consequently, if the user enters text in an editable Author column text cell, the user changes the value of the last name property belonging to the Person object, not the destination of the to-one relationship belonging to the Media object. Using pop-up menus is one way to implement an editable to-one relationship.

See [Creating a Master-Detail Interface](Creating%20a%20Master-Detail%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsga4talkcineugqkejbbq) for the steps to create a master-detail interface.

__Figure 1__  Using pop-up menus to represent to-one relationships

!!

To do this, you first need the supporting model and controller objects. Assuming you already have a master interface, you create an array of models that will be displayed in the pop-up menu, and you create an array controller to manage it.

How you initialize the collection of objects to display in the pop-up depends on your application. This example assumes that a collection already exists and is a property of the File’s Owner (for example, a property called `authors` containing Person objects).

Create an NSArrayController by dragging it from the Cocoa-Controllers palette to your nib file, and rename it appropriately (for example, `AuthorsController`). It’s common to have multiple controller objects per nib file so renaming them helps to identify them. Now, bind the model to the controller as follows. Select the array controller, display the Bindings pane in the Info window, reveal the `contentArray` binding, and configure it as follows:

1. Set the `Bind to` aspect to the object that maintains the collection of model objects (for example, the File’s Owner).
2. Leave the `Controller Key` blank.
3. Set the `Model Key Path` to the name of the array (for example, `authors`).

Also enter the appropriate class name in the Object Class Name field on the Attributes pane (for example, enter the Person class name).

Next, you create the pop-up views by dragging an NSPopUpButton to a window or an NSPopUpButtonCell to the column that will display the to-one relationship.

The primary bindings of an NSPopUpMenu and NSTableColumn (containing an NSPopUpButtonCell) that you will use to set up an editable to-one relationship are:

- `content`—the collection of objects to display in the pop-up menu.
- `contentValues`—the property of the objects in `content` that you want to display in the pop-up menu.
- `selectedObject`—the to-one relationship that users change when selecting an item from the pop-up menu.

For example, if you want to display a pop-up menu in a column, configure the `content` binding to specify the content of the pop-up menu as follows:

1. Set the `Bind to` aspect to `AuthorsController`.
2. Set the `Controller Key` aspect to `arrangedObjects` .
3. Leave the `Model Key Path` aspect blank.

Then configure the `contentValues` binding to specify what should be displayed in the menu items as follows:

1. Set the `Bind to` aspect to `AuthorsController`.
2. Set the `Controller Key` aspect to `arrangedObjects`.
3. Set the `Model Key Path` aspect to `lastName`.

Finally, configure the `selectedObject` binding to specify the actual to-one relationship this pop-up menu changes as follows:

1. Set the `Bind to` aspect to `MediaAssetsController`.
2. Set the `Controller Key` aspect to `arrangedObjects`.
3. Set the `Model Key Path` aspect to `author` (a to-one relationship).

Now, when you run your application, a pop-up menu appears in each of the table column cells, displaying the current value of the to-one relationship. When the user selects another item from the menu, the controller changes the destination object of that to-one relationship.

Follow the same steps above to configure an NSPopUpButton as an editable to-one relationship. If you are implementing a master-detail interface and this pop-up button appears in the detail interface, then set the `Controller Key` for the `selectedObject` binding to `selection`, that is, to the currently selected object.

[Next](Filtering%20Using%20a%20Custom%20Array%20Controller.md)[Previous](Displaying%20Images%20Using%20Bindings.md)

