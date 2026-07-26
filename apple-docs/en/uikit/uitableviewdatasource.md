---
title: UITableViewDataSource
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewdatasource
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdatasource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdatasource.json'
content_hash: 'sha256:0b848a414d12d92f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITableViewDataSource

<sub>Protocol</sub>

The methods that an object adopts to manage data and provide cells for a table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UITableViewDataSource : NSObjectProtocol
```

## Overview

Table views manage only the presentation of their data; they don’t manage the data itself. To manage the data, you provide the table with a data source object — an object that implements the [UITableViewDataSource](uitableviewdatasource.md) protocol. A data source object responds to data-related requests from the table. It also manages the table’s data directly, or coordinates with other parts of your app to manage that data. Other responsibilities of the data source object include:

- Reporting the number of sections and rows in the table.
- Providing cells for each row of the table.
- Providing titles for section headers and footers.
- Configuring the table’s index, if any.
- Responding to user- or table-initiated updates that require changes to the underlying data.

Only two methods of this protocol are required, and they’re shown in the following example code.

```swift
// Return the number of rows for the table.     
override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
   return 0
}

// Provide a cell object for each row.
override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
   // Fetch a cell of the appropriate type.
   let cell = tableView.dequeueReusableCell(withIdentifier: "cellTypeIdentifier", for: indexPath)
   
   // Configure the cell’s contents.
   cell.textLabel!.text = "Cell text"
       
   return cell
}
```

Use other methods of this protocol to enable specific features for your table. For example, you must implement the [- tableView:commitEditingStyle:forRowAtIndexPath:](<uitableviewdatasource/tableview(__commit_forrowat_).md>) method to enable the swipe-to-delete feature for rows.

For information about how to create and configure your table’s cells using your data source object, see [Filling a table with data](filling-a-table-with-data.md).

### Specify the location of rows and sections

Table views communicate the location of cells to you using the [row](../foundation/nsindexpath/row.md) and [section](../foundation/nsindexpath/section.md) properties of [NSIndexPath](../foundation/nsindexpath.md) objects. Row and section indexes are zero based, so the first section is at index `0`, the second at index `1`, and so on. Similarly, the first row of each section is at index `0`, which means you need both the [section](../foundation/nsindexpath/section.md) and [row](../foundation/nsindexpath/row.md) values to identify a row uniquely. If your table has no sections, you need only the [row](../foundation/nsindexpath/row.md) value.

![](../../../attachments/9b202d53b6f805deaaabbaed86a978cc/media-3148902@2x.png)

<sub>Illustration that shows a table with multiple sections. The first section has an index of 0 and no row value. The nine rows in the first section have indexes between 0 and 8. The second section has an index of 1 and no row value. Its first row starts at index 0 again.</sub>

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UITableViewController](uitableviewcontroller.md), [UITableViewDiffableDataSource](uitableviewdiffabledatasource-2euir.md), [UITableViewDiffableDataSourceReference](uitableviewdiffabledatasourcereference.md)

## Topics

### Providing the number of rows and sections

- [- tableView:numberOfRowsInSection:](<uitableviewdatasource/tableview(__numberofrowsinsection_).md>) — Tells the data source to return the number of rows in a given section of a table view.
- [- numberOfSectionsInTableView:](<uitableviewdatasource/numberofsections(in_).md>) — Asks the data source to return the number of sections in the table view.

### Providing cells, headers, and footers

- [- tableView:cellForRowAtIndexPath:](<uitableviewdatasource/tableview(__cellforrowat_).md>) — Asks the data source for a cell to insert in a particular location of the table view.
- [- tableView:titleForHeaderInSection:](<uitableviewdatasource/tableview(__titleforheaderinsection_).md>) — Asks the data source for the title of the header of the specified section of the table view.
- [- tableView:titleForFooterInSection:](<uitableviewdatasource/tableview(__titleforfooterinsection_).md>) — Asks the data source for the title of the footer of the specified section of the table view.

### Inserting or deleting table rows

- [- tableView:commitEditingStyle:forRowAtIndexPath:](<uitableviewdatasource/tableview(__commit_forrowat_).md>) — Asks the data source to commit the insertion or deletion of a specified row.
- [- tableView:canEditRowAtIndexPath:](<uitableviewdatasource/tableview(__caneditrowat_).md>) — Asks the data source to verify that the given row is editable.

### Reordering table rows

- [- tableView:canMoveRowAtIndexPath:](<uitableviewdatasource/tableview(__canmoverowat_).md>) — Asks the data source whether a given row can move to another location in the table view.
- [- tableView:moveRowAtIndexPath:toIndexPath:](<uitableviewdatasource/tableview(__moverowat_to_).md>) — Tells the data source to move a row at a specific location in the table view to another location.

### Configuring an index

- [- sectionIndexTitlesForTableView:](<uitableviewdatasource/sectionindextitles(for_).md>) — Asks the data source to return the titles for the sections of a table view.
- [- tableView:sectionForSectionIndexTitle:atIndex:](<uitableviewdatasource/tableview(__sectionforsectionindextitle_at_).md>) — Asks the data source to return the index of the section having the given title and section title index.

## See Also

### Data

- [Filling a table with data](filling-a-table-with-data.md) — Create and configure cells for your table dynamically using a data source object, or provide them statically from your storyboard.
- [Asynchronously loading images into table and collection views](asynchronously-loading-images-into-table-and-collection-views.md) — Store and fetch images asynchronously to make your app more responsive.
- [UITableViewDataSourcePrefetching](uitableviewdatasourceprefetching.md) — A protocol that provides advance warning of the data requirements for a table view, allowing you to start potentially long-running data operations early.
- [UITableViewDiffableDataSource](uitableviewdiffabledatasource-2euir.md) — The object you use to manage data and provide cells for a table view.
- [NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md) — A representation of the state of the data in a view at a specific point in time.
- [UILocalizedIndexedCollation](uilocalizedindexedcollation.md) — An object that organizes, sorts, and localizes the data for a table view that has a section index.
- [UIDataSourceTranslating](uidatasourcetranslating.md) — An advanced interface for managing a data source object.
- [UIRefreshControl](uirefreshcontrol.md) — A standard control that can initiate the refreshing of a scroll view’s contents.
