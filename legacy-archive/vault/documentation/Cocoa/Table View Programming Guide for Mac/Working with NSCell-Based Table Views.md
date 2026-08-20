---
title: Table View Programming Guide for Mac
apple_id: 10000026i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TableView/PopulatingCellTables/PopulatingCellTables.html
archived_at: '2026-07-15T07:20:00.014196Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Table View Programming Guide for Mac](About%20Table%20Views%20in%20OS%20X%20Applications.md)


[Next](Document%20Revision%20History.md)[Previous](Sorting%20Table%20View%20Rows.md)

# Working with NSCell-Based Table Views

Although most tables use `NSView` subclasses for cells, you might need to work with a table that instead uses `NSCell` subclasses. Working with an `NSCell`-based table is similar to working with an `NSView`-based table, but there are differences in how you add cells to the table and how you use Cocoa bindings.

The steps you take to create an `NSCell`-based table in Interface Builder are identical to the steps you take to create an `NSView`-based table. For specifics, see [Constructing a Table View Using Interface Builder](Constructing%20a%20Table%20View%20Using%20Interface%20Builder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazdm2jninedilktk4yq).

After you add an `NSCell`-based table to your user interface, you can add individual cells either manually or using Interface Builder. To use Interface Builder to add cells:

1. Drag the correct cell type from the object library to the appropriate column within the table view.

   Only subclasses of [NSCell](https://developer.apple.com/documentation/appkit/nscell) can be inserted into `NSCell`-based table views.
2. Repeat step 1 as often as necessary to provide cells for every column.
3. Consider setting an identifier for each column. Set the identifier in the Identity area of the Identity inspector.

   Setting a column identifier makes populating and retrieving columns substantially easier.

`NSCell`-based table views are similar to `NSView`-based table views: They have a data source that adopts the [NSTableViewDataSource](https://developer.apple.com/documentation/appkit/nstableviewdatasource) protocol, and an optional delegate that adopts the [NSTableViewDelegate Protocol](https://developer.apple.com/documentation/appkit/nstableviewdelegate) to allow custome table view behavior.

To tell the table view how many rows it has to display, `NSCell`-based table views must implement the [numberOfRowsInTableView:](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1524583-numberofrowsintableview)[NSTableViewDataSource](https://developer.apple.com/documentation/appkit/nstableviewdatasource) method. It must also implement the [tableView:objectValueForTableColumn:row:](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1533674-tableview) method that returns the data displayed in each column cell. If the table view data is editable, then a method to allow the updating the model values can be implemented. Note that when using Cocoa bindings for populating an `NSCell`-based table view, the data source methods required for programmatic populating are unnecessary.

A table view class that conforms to the data source protocol is responsible for:

- Providing the number of rows in the table view
- Providing the content for each item within the table view
- Responding to edit requests if the table view supports editing
- Receiving notifications that the information used when sorting the table view has changed
- Providing pasteboard data for supporting drag and drop within your own app as well as within other apps

Although the [NSTableViewDelegate Protocol](https://developer.apple.com/documentation/appkit/nstableviewdelegate) declares all the data-providing methods to be optional, all data sources that programmatically populate `NSCell`-based table views must implement those methods. The methods that provide the number of rows and the content for each item within the table are optional when using Cocoa bindings.

If your app uses a data source, the data source class must adopt the [NSTableViewDataSource](https://developer.apple.com/documentation/appkit/nstableviewdatasource) protocol and implement some or all of the methods defined by the protocol. Even though all the methods in the data source are optional, the [numberOfRowsInTableView:](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1524583-numberofrowsintableview) method is not optional if you are not using Cocoa bindings.

To populate a table view programmatically, use this process:

- Create a data source class that adopts the [NSTableViewDataSource](https://developer.apple.com/documentation/appkit/nstableviewdatasource) protocol. Note that you don’t have to create a separate data source class; instead, you can integrate this functionality into a another class, such as the class that also implements the delegate methods.
- Implement the [numberOfRowsInTableView:](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1524583-numberofrowsintableview) and [tableView:objectValueForTableColumn:row:](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1533674-tableview) methods that provide the data.
- If the table view allows the user to edit the data, implement the [tableView:setObjectValue:forTableColumn:row:](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1526317-tableview) method.
- Your app must also set the object as the data source of the table view. (Do this in Interface Builder or in code, using the `NSTableView` instance method `setDataSource:`.)

The following example populates a simple table view and enables editing. The table consists of a single column called “Names”.

The table column has had its column identifier set to `name`. This can be done in Interface Builder by selecting the table column, opening the Table Column Attributes inspector, and setting the identifier string. It can also be done programmatically by invoking [setIdentifier:](https://developer.apple.com/documentation/appkit/nstablecolumn/1531113-identifier) on a table column, passing the column name. The table column identifier is a great convenience when using `NSCell`-based table views with multiple columns (and it’s an absolute necessity when using `NSView`-based table views). To access a table column instance, simply ask the table view for the column by using the identifier string. In this way you eliminate the need to cache the table columns for comparison. Setting the column identifier is a simple practice that you should always perform.

The code fragment in Listing 8-1 shows the implementation of the [numberOfRowsInTableView:](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1524583-numberofrowsintableview) data source method. For this simple code snippet, it’s assumed that the app’s delegate is acting as the data source object of the table view and that the sample data is a simple array of strings stored in a property declared as `namesArray`.

__Listing 8-1__  Example `numberOfRowsInTableView:` implementation

```objc
- (NSInteger)numberOfRowsInTableView:(NSTableView *)tableView
{
    // This is a defensive move
    // There are cases where the nib containing the NSTableView can be loaded before the data is populated
    // by ensuring the count value is 0 and checking to see if the namesArray is not nil, the app
    // is protecting itself agains that situation
    NSInteger count=0;
    if (self.namesArray)
        count=[self.namesArray count];
    return count;
}
```

The `numberOfRowsInTableView:` implementation returns the number of objects in `namesArray`. First it does some defensive programming. It declares a `count` variable and sets it to `0` and then ensures that `self.namesArray` is not `nil`. This is a good practice because sometimes a NIB containing a table view may be loaded and sent a `reload` message before the data itself has been initialized. Because this method returns a scalar, an exception may occur. By performing this simple test, your app can ensure that the data has been loaded and is available before any attempt is made to display the content.

Having implemented the method that returns the number of items in the table view, you must now implement the method that populates those rows. The [tableView:objectValueForTableColumn:row:](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1533674-tableview) method returns the appropriate value to display for the requested row and column of the specified `NSTableView`. You can see in Listing 8-2 an example of why the table column identifier is so useful: The identity of the column that requires population is sent the [identifier](https://developer.apple.com/documentation/appkit/nstablecolumn/1531113-identifier) message and the name returned is compared to determine the data to provide.

__Listing 8-2__  Example `tableView:objectValueForTableColumn:row:` sample implementation

```objc
- (id)tableView:(NSTableView *)aTableView objectValueForTableColumn:(NSTableColumn *)aTableColumn row:(NSInteger)rowIndex
{
    // The return value is typed as (id) because it will return a string in most cases.
    id returnValue=nil;

    // The column identifier string is the easiest way to identify a table column.
    NSString *columnIdentifer = [aTableColumn identifier];

    // Get the name at the specified row in namesArray
    NSString *theName = [namesArray objectAtIndex:rowIndex];


    // Compare each column identifier and set the return value to
    // the Person field value appropriate for the column.
    if ([columnIdentifer isEqualToString:@"name"]) {
        returnValue = theName;
    }


    return returnValue;
}
```

In Listing 8-2, `returnValue` is a local variable for storing the value returned by the method. The return value is of type [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString) because all the column contents are strings. If the table had a combination of `NSTextFieldCell`, `NSImageCell`, and so on, the `returnValue` would typically be typed more generically, as `id`.

Next, the object assigns `anObject` to the object at the `rowIndex` offset in the `namesArray` property. Because there is a one-to-one correlation between a row and the array index for the corresponding value, accessing the object for a row is straightforward.

Finally, the `returnValue` variable is set to the value that’s displayed in the column. To eliminate code and simplify returning the data, it takes advantage of key-value coding.

For your app to edit the content of an `NSCell`-based table view, you implement the [tableView:setObjectValue:forTableColumn:row:](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1526317-tableview) data source protocol method. This method is similar to [tableView:objectValueForTableColumn:row:](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1533674-tableview), which provides the data for the table view, but instead of requesting that you return a value for the specified row and column, it provides the new value for that row and cell.

Listing 8-3 shows an implementation of the [tableView:setObjectValue:forTableColumn:row:](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1526317-tableview) method.

__Listing 8-3__  Example `tableView:setObjectValue:forTableColumn:row:` implementation

```objc
- (void)tableView:(NSTableView *)aTableView setObjectValue:(id)anObject forTableColumn:(NSTableColumn *)aTableColumn row:(NSInteger)rowIndex
{

    // The column identifier string is the easiest way to identify a table column.
    NSString *columnIdentifer = [aTableColumn identifier];

    if ([columnIdentifer isEqualToString:@"name"]) {
        [namesArray replaceObjectAtIndex:rowIndex withObject:anObject];
    }

}
```

The example implementation in Listing 8-3 examines the column `identifier` method result to ensure that it’s the “Names” table column that’s being edited. This is a good practice regardless of the number of columns in a table. After verifying the column’s identity, the code replaces the object in the `namesArray` with the new value.

The Cocoa bindings technique used in `NSView`-based tables differs significantly from that used in `NSCell`-based tables. In an `NSCell`-based table you bind the table column’s content binding to the array controller’s `arrangedObjects`, and then configure the column’s cell’s bindings. You never bind directly to the table view’s content binding.

[Next](Document%20Revision%20History.md)[Previous](Sorting%20Table%20View%20Rows.md)

