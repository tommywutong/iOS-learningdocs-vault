---
title: Table View Programming Guide for Mac
apple_id: 10000026i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TableView/PopulatingView-TablesProgrammatically/PopulatingView-TablesProgrammatically.html
archived_at: '2026-07-15T07:20:00.026144Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Table View Programming Guide for Mac](About%20Table%20Views%20in%20OS%20X%20Applications.md)


[Next](Populating%20a%20Table%20View%20Using%20Cocoa%20Bindings.md)[Previous](Constructing%20a%20Table%20View%20Using%20Interface%20Builder.md)

# Populating a Table View Programmatically

To populate a table view programmatically, you must implement the `NSTableViewDataSource` and the `NSTableViewDelegate` protocols. Both protocols contain methods that are essential to providing the content and creating the cells for the table view. Specifically, you must implement:

- The [NSTableViewDataSource](https://developer.apple.com/documentation/appkit/nstableviewdatasource) protocol method [numberOfRowsInTableView:](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1524583-numberofrowsintableview), which tells the table how many rows it needs to display.
- The [NSTableViewDelegate Protocol](https://developer.apple.com/documentation/appkit/nstableviewdelegate) method [tableView:viewForTableColumn:row:](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1527449-tableview), which provides the table with the view to display in the cell at a specific column and row. It also populates that cell with the appropriate data.

The data source method is required for the table to work. Fortunately, the method’s implementation is very straightforward.

Listing 3-1 shows a simple implementation of the data source method `numberOfRowsInTableView:`, which simply returns the number of items in the array of name strings.

__Listing 3-1__  A simple implementation of `numberOfRowsInTableView`

```objc
- (NSInteger)numberOfRowsInTableView:(NSTableView *)tableView {
   return nameArray.count;
}
```


The `NSTableViewDelegate` is responsible for providing the cell that’s displayed in the table view, along with implementing any target-action or notification code so that it can interact with the delegate. What follows are two simple implementations of [tableView:viewForTableColumn:row:](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1527449-tableview) that can be used to display the content of the `namesArray` model object. The first implementation uses a text field object for the cell of the table view; the second uses a custom table cell view that’s been defined in Interface Builder.

In both of these simple cases no action is required by the cell. But if the cell view contained buttons, allowed editing, or was required to interact with the delegate, it would have to use target-action or notifications to work. For an example of implementing some of these actions, see the “Complex TableView” example in the _[TableViewPlayground: Using View-Based NSTableView and NSOutlineView](../../../samplecode/TableViewPlayground-%20Using%20View-Based%20NSTableView%20and%20NSOutlineView/TableViewPlayground-%20Using%20View-Based%20NSTableView%20and%20NSOutlineView.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytanzsg4)_ sample project.

The `NSTableViewDelegate` method [tableView:viewForTableColumn:row:](https://developer.apple.com/documentation/appkit/nstableviewdelegate/1527449-tableview) creates and configures the cell that’s displayed in the table view. The pseudocode in Listing 3-2 creates an `NSTextField` object as the cell and populates it with the appropriate name for the row. (In this example, the table has only one column.)

__Listing 3-2__  A simple implementation of `tableView:viewForTableColumn:row:` that returns a text field

```objc
- (NSView *)tableView:(NSTableView *)tableView
   viewForTableColumn:(NSTableColumn *)tableColumn
                  row:(NSInteger)row {

    // Get an existing cell with the MyView identifier if it exists
    NSTextField *result = [tableView makeViewWithIdentifier:@"MyView" owner:self];

    // There is no existing cell to reuse so create a new one
    if (result == nil) {

         // Create the new NSTextField with a frame of the {0,0} with the width of the table.
         // Note that the height of the frame is not really relevant, because the row height will modify the height.
         result = [[NSTextField alloc] initWithFrame:...];

         // The identifier of the NSTextField instance is set to MyView.
         // This allows the cell to be reused.
         result.identifier = @"MyView";
      }

      // result is now guaranteed to be valid, either as a reused cell
      // or as a new cell, so set the stringValue of the cell to the
      // nameArray value at row
      result.stringValue = [self.nameArray objectAtIndex:row];

      // Return the result
      return result;

}
```

The code in Listing 3-2 first calls `makeViewWithIdentifier:owner:`, passing the identifier `@"MyView"` to determine whether there is a cell view available in the pool of resuable cells. If a resuable cell is available, the code assigns the specified row’s `nameArray` value to the text field’s `stringValue` property and returns the result.

If no cell with the identifier `@”MyView”` is available, a new text field is created. The code sets the new text field’s identifier to `@”MyView”` so that it can be reused when the opportunity arises. Finally, as in the first case, the `stringValue` of the text field is set to the correct `nameArray` value and the result is returned.

The most likely situation is that you’ll have designed a cell in Interface Builder and will want to fetch it and then populate the values in that cell. The implementation for this situation is shown in Listing 3-3. This example assumes that there is already a table created in Interface Builder with a column identifier of `@”MyView”` and a cell view that also has the identifier `@”MyView”`.

__Listing 3-3__  A simple implementation of `tableView:viewForTableColumn:row:` that returns a table cell view

```objc
- (NSView *)tableView:(NSTableView *)tableView
   viewForTableColumn:(NSTableColumn *)tableColumn
                  row:(NSInteger)row {

      // Retrieve to get the @"MyView" from the pool or,
      // if no version is available in the pool, load the Interface Builder version
      NSTableCellView *result = [tableView makeViewWithIdentifier:@"MyView" owner:self];

      // Set the stringValue of the cell's text field to the nameArray value at row
      result.textField.stringValue = [self.nameArray objectAtIndex:row];

      // Return the result
      return result;
```

This implementation attempts to retrieve a cell view with the `@”MyView”` identifier from the pool of reusable cells. If there is no reusable view, the code looks in Interface Builder for the table column and cell with the `@”MyView”` identifier. Once found, the `makeViewWithIdentifier:owner:` method returns the cell view and the rest of the code sets the cell’s the string value.

[Next](Populating%20a%20Table%20View%20Using%20Cocoa%20Bindings.md)[Previous](Constructing%20a%20Table%20View%20Using%20Interface%20Builder.md)

