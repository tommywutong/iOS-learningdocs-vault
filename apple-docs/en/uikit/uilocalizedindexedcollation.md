---
title: UILocalizedIndexedCollation
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilocalizedindexedcollation
source_url: 'https://developer.apple.com/documentation/uikit/uilocalizedindexedcollation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilocalizedindexedcollation.json'
content_hash: 'sha256:3c8fc5de4d3ad279'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UILocalizedIndexedCollation

<sub>Class</sub>

An object that organizes, sorts, and localizes the data for a table view that has a section index.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UILocalizedIndexedCollation
```

## Overview

Use a [UILocalizedIndexedCollation](uilocalizedindexedcollation.md) object in conjunction with your table’s data source object to sort and manage the data in an indexed table view. An index is an ideal way for users to navigate a table view containing sequential content. For example, the Contacts app sorts contacts alphabetically and displays an index for navigating those contacts quickly. You use the collation object as the source of the table’s section titles and index titles in your table view. You also use it to sort items in each section of your table.

To prepare the data for a section index, create an indexed-collation object and call [- sectionForObject:collationStringSelector:](<uilocalizedindexedcollation/section(for_collationstringselector_).md>) for each model object to be indexed. That method determines the section in which each of these objects should appear and returns an integer that identifies the section. The table-view controller then puts each object in a local array for its section. For each section array, the controller calls the [- sortedArrayFromArray:collationStringSelector:](<uilocalizedindexedcollation/sortedarray(from_collationstringselector_).md>) method to sort all of the objects in the section. The indexed-collation object is now the data store that the table-view controller uses to provide section-index data to the table view, as shown in the following example code.

**Swift**

```swift
func tableView(tableView: UITableView!, titleForHeaderInSection section: Int) -> String! {
    let currentCollation = UILocalizedIndexedCollation.currentCollation() as UILocalizedIndexedCollation
    let sectionTitles = currentCollation.sectionTitles as NSArray
    return sectionTitles.objectAtIndex(section) as String
}
 
func sectionIndexTitlesForTableView(tableView: UITableView!) -> NSArray! {
    let currentCollation = UILocalizedIndexedCollation.currentCollation() as UILocalizedIndexedCollation
    return currentCollation.sectionIndexTitles as NSArray
}
 
func tableView(tableView: UITableView!, sectionForSectionIndexTitle title: String!, atIndex index: Int) -> Int {
    let currentCollation = UILocalizedIndexedCollation.currentCollation() as UILocalizedIndexedCollation
    return currentCollation.sectionForSectionIndexTitleAtIndex(index)
}
```

**Objective-C**

```objc
- (NSString *)tableView:(UITableView *)tableView titleForHeaderInSection:(NSInteger)section
{
    return [[[UILocalizedIndexedCollation currentCollation] sectionTitles] objectAtIndex:section];
}
 
- (NSArray *)sectionIndexTitlesForTableView:(UITableView *)tableView
{
    return [[UILocalizedIndexedCollation currentCollation] sectionIndexTitles];
}
 
- (NSInteger)tableView:(UITableView *)tableView sectionForSectionIndexTitle:(NSString *)title atIndex:(NSInteger)index
{
    return [[UILocalizedIndexedCollation currentCollation] sectionForSectionIndexTitleAtIndex:index];
}
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Getting the shared instance

- [+ currentCollation](<uilocalizedindexedcollation/current().md>) — Returns an indexed-collation instance for the current table view.

### Preparing the sections and section indexes

- [- sectionForObject:collationStringSelector:](<uilocalizedindexedcollation/section(for_collationstringselector_).md>) — Returns an integer identifying the section in which a model object belongs.
- [- sortedArrayFromArray:collationStringSelector:](<uilocalizedindexedcollation/sortedarray(from_collationstringselector_).md>) — Sorts the objects within a section by their localized titles.

### Providing section index data to the table view

- [sectionTitles](uilocalizedindexedcollation/sectiontitles.md) — Returns the list of section titles for the table view.
- [sectionIndexTitles](uilocalizedindexedcollation/sectionindextitles.md) — Returns the list of section-index titles for the table view.
- [- sectionForSectionIndexTitleAtIndex:](<uilocalizedindexedcollation/section(forsectionindextitle_).md>) — Returns the section that the table view should scroll to for the given index title.

## See Also

### Data

- [Filling a table with data](filling-a-table-with-data.md) — Create and configure cells for your table dynamically using a data source object, or provide them statically from your storyboard.
- [Asynchronously loading images into table and collection views](asynchronously-loading-images-into-table-and-collection-views.md) — Store and fetch images asynchronously to make your app more responsive.
- [UITableViewDataSource](uitableviewdatasource.md) — The methods that an object adopts to manage data and provide cells for a table view.
- [UITableViewDataSourcePrefetching](uitableviewdatasourceprefetching.md) — A protocol that provides advance warning of the data requirements for a table view, allowing you to start potentially long-running data operations early.
- [UITableViewDiffableDataSource](uitableviewdiffabledatasource-2euir.md) — The object you use to manage data and provide cells for a table view.
- [NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md) — A representation of the state of the data in a view at a specific point in time.
- [UIDataSourceTranslating](uidatasourcetranslating.md) — An advanced interface for managing a data source object.
- [UIRefreshControl](uirefreshcontrol.md) — A standard control that can initiate the refreshing of a scroll view’s contents.
