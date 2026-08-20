---
title: Table View Programming Guide for Mac
apple_id: 10000026i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TableView/CreatingViewBasedTablesInIB/CreatingViewBasedTablesInIB.html
archived_at: '2026-07-15T07:19:59.247684Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Table View Programming Guide for Mac](About%20Table%20Views%20in%20OS%20X%20Applications.md)


[Next](Populating%20a%20Table%20View%20Programmatically.md)[Previous](Understanding%20Table%20Views.md)

# Constructing a Table View Using Interface Builder

Table views consist of many different views and objects, and as a result, they are best constructed within Interface Builder. It’s also easier to create individual cells using Interface Builder rather than manually.

The following steps describe how to create a table view in Interface Builder. (Use these steps whether you’re creating an `NSView`-based table or an `NSCell`-based table.)

1. In Xcode, open the nib file to which you want to add the table view.
2. Drag an [NSTableView](https://developer.apple.com/documentation/appkit/nstableview) object from the object library to the appropriate window or view on the canvas.
3. Position and configure the table view as appropriate.
4. In the Size inspector, set the table’s resizing behavior with respect to the window and any other related objects.
5. In the Attributes inspector, add or remove columns.
6. Connect an `IBOutlet` in the appropriate class to the table view to allow for manipulating the table view and its contents.
7. Set the table view’s delegate and data source to the appropriate objects (alternatively, you can use `setDelegate:` and `setDataSource:` to programmatically make these settings).

   If you don’t associate the table view with its delegate, actions sent by objects in the table’s cell views won’t work.

After you add a table view to your window, you need to create cells for it. Although you can create individual table view cells manually, it’s far easier to create them in Interface Builder. The following steps provide the basics for creating cells within a table. (If you need to create cells for an `NSCell`-based table, see [Working with NSCell-Based Table Views](Working%20with%20NSCell-Based%20Table%20Views.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazdm2jninedklktk4yq).)

1. Drag an [NSTableCellView](https://developer.apple.com/documentation/appkit/nstablecellview) object (or a custom view) from the object library to the appropriate column in the table view.

   Interface Builder provides two types of `NSTableCellView`: Image & Text Table Cell View and Text Table Cell View.

   If you choose to use a custom view instead of one of the provided cell views, set its view class in the Attributes inspector. Typically, the view class is a subclass of `NSTableCellView`.
2. Repeat step 1 as many times as necessary to provide cells for every column.
3. (Optional) Set a custom identifier in the Identity area of the Identity inspector for each column.

   If your table is simple and you don’t need to do much column management—or if you’re using bindings—let Interface Builder automatically assign a unique identifier to each column. Using an automatic assignment can be convenient because it ensures that the column’s cells have the same identifier and that these identifiers are in always in sync. For more information, see [Columns and Cells Have Identifiers That Make It Easy to Find Them](Understanding%20Table%20Views.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazdm2jninedelktk42q).

[Next](Populating%20a%20Table%20View%20Programmatically.md)[Previous](Understanding%20Table%20Views.md)

