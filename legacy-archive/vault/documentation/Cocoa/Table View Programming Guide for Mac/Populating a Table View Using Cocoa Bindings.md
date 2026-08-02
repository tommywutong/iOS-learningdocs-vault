---
title: Table View Programming Guide for Mac
apple_id: 10000026i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TableView/PopulatingViewTablesWithBindings/PopulatingView-TablesWithBindings.html
archived_at: '2026-07-15T07:20:00.035184Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Table View Programming Guide for Mac](About%20Table%20Views%20in%20OS%20X%20Applications.md)


[Next](Modifying%20a%20Table%E2%80%99s%20Visual%20Attributes.md)[Previous](Populating%20a%20Table%20View%20Programmatically.md)

# Populating a Table View Using Cocoa Bindings

Populating a table view using Cocoa bindings is considered an advanced topic. Although using bindings requires significantly less code—in some cases no code at all—the bindings are hard to see and debug if you aren’t familiar with the interface. It’s strongly suggested that you become comfortable with the techniques for managing table views programmatically before you decide to use Cocoa bindings.

The following example assumes that your app’s delegate has an array property called `peopleArray`, populated with instances of the `Person` class, which serves as the model object. The `Person` class is a subclass of `NSObject` and declares two properties, `name` and `image`. The table view is a single column table that displays an image adjacent to the name.

It’s assumed that the delegate class, and a NIB with a single column table view, have already been created. The identifier for the column is Automatic, which is strongly recommended.

The content binding is all that’s required to relate the controller to the table view. Regardless of how many columns the table has, or how complex the views are, if the model class has the fields to populate it, this binding makes the most important connection to the table view.

To create bindings for the person table view:

1. Select the MainMenu nib file in the File Manager view.

   This displays the Interface Builder editor, which already contains the table view and the `NSTableCellView`.
2. Drag an array controller from the Object library to the Objects dock.
3. Select the array controller in the Objects dock, and bind it to the model object array. This binding sets the `peopleArray` of the app delegate as the content array of the array controller.

| Binding field | Value |
| --- | --- |
| Bind to: | Simple Bindings App Delegate (“Simple Bindings” is the example app name) |
| Model key path | `peopleArray` |
4. Select the table view, and then select the Bindings inspector.
5. Configure the bindings for the table view’s `Content` binding.

| Binding field | Value |
| --- | --- |
| Bind to: | Names Array Controller |
| Controller key | `arrangedObjects` |

When you make the connection to the table view’s `Content` binding, the `objectValue` property of the `NSTableViewCell` used as the cell for the table column is configured such that for each item in the model array, the table updates the `objectValue` property to the current row’s `Person` object.

1. Select the text field in the table column cell and create the binding.

   All bindings of subviews in the cell are made to the `objectValue`.

   Configure the `textField` instance’s `value` binding.

| Binding field | Value |
| --- | --- |
| Bind to: | Table Cell View |
| Model key path | `objectValue.name` |
2. Select the image view in the table column cell, and create the binding to the `Value` binding.

   All bindings of subviews in the cell are made to the `objectValue`.

   Configure the `imageView` instance’s `value` binding.

| Binding field | Value |
| --- | --- |
| Bind to: | Table Cell View |
| Model key path | `objectValue.image` |

[Next](Modifying%20a%20Table%E2%80%99s%20Visual%20Attributes.md)[Previous](Populating%20a%20Table%20View%20Programmatically.md)

