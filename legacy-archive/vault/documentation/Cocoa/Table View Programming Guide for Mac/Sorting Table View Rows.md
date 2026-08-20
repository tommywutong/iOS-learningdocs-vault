---
title: Table View Programming Guide for Mac
apple_id: 10000026i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TableView/SortingTableViews/SortingTableViews.html
archived_at: '2026-07-15T07:20:00.060449Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Table View Programming Guide for Mac](About%20Table%20Views%20in%20OS%20X%20Applications.md)


[Next](Working%20with%20NSCell-Based%20Table%20Views.md)[Previous](Enabling%20Row%20Selection%20and%20User%20Actions.md)

# Sorting Table View Rows

Table views can be configured so that users can click on a column’s header to toggle scrolling from none to ascending or descending order. You use sort descriptors to enable this behavior.

Your app can specify a default sort descriptor to use when displaying the table view data. It does this using the `NSTableView`[setSortDescriptors:](https://developer.apple.com/documentation/appkit/nstableview/1534198-sortdescriptors) method. The sort descriptors are an array of `NSSortDescriptors` instances. For example, the following code sorts the content based on the last name and first name:

```
    [theTableView setSortDescriptors:[NSArray arrayWithObjects:
                                      [NSSortDescriptor sortDescriptorWithKey:@"lastName" ascending:YES selector:@selector(compare:)],
                                      [NSSortDescriptor sortDescriptorWithKey:@"firstName" ascending:YES selector:@selector(compare:)],
                                      nil]];
```

This code snippet sorts the content indirectly through the delegate callback (see [Responding to a Sort Request](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazdm2jninedcmbnknlte)) but won’t allow a user to click in a table header to change the sort order for that column. To give users this capability, you need to configure sorting on a per-column basis. In a table configured for per-column sorting, the user’s click on a table header modifies the table view’s sort descriptor to reflect the current sort state of the table view (you can use the [sortDescriptors](https://developer.apple.com/documentation/appkit/nstableview/1534198-sortdescriptors) method to access the sort descriptor).

You can sort individual table columns programmatically by specifying an `NSSortDescriptor` prototype instance for the appropriate `NSTableColumn` instance, or by using Interface Builder.

You can set a sort method for a column programmatically by creating a sort descriptor prototype. You create the prototype by using the method [sortDescriptorWithKey:ascending:selector:](https://developer.apple.com/documentation/foundation/nssortdescriptor/1503730-sortdescriptorwithkey) to create an [NSSortDescriptor](https://developer.apple.com/documentation/foundation/nssortdescriptor) instance. The resulting sort descriptor instance is then set as the table column’s sorting prototype using the method [setSortDescriptorPrototype:](https://developer.apple.com/documentation/appkit/nstablecolumn/1534663-sortdescriptorprototype). When a user clicks the header, the table view’s sort descriptors are modified and the table column header reflects the sort direction.

The following code creates a sort descriptor prototype for a `lastName` column using localized sorting:

```
NSTableColumn *tableColumn = [theTableView tableColumnWithIdentifier:@"lastName"];
NSSortDescriptor *lastNameSortDescriptor = [NSSortDescriptor sortDescriptorWithKey:@"lastName"
                                                                         ascending:YES
                                                                          selector:@selector(compare:)];
[tableColumn setSortDescriptorPrototype:lastNameSortDescriptor];
```


To use Interface Builder to configure per-column sorting, select a table column and open the Table Column Attributes inspector. The inspector contains three controls that help you configure sorting behavior:

- The Sort Key field specifies the key in the table view data model that the column sorts on.
- The Selector field contains the selector that the sort uses. Tabbing to the field causes the field to fill with the [compare:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/compare:) selector.

  This comparison selector expects a single parameter—the value that needs to be sorted—and returns an [NSComparisonResult](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/tdef/NSComparisonResult). You can substitute any method selector that adheres to that pattern, including custom methods of your own.

  The [compare:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/compare:) method works with `NSString`, `NSDate`, and `NSNumber` objects. If your table column contains only strings, you may want to consider using the [caseInsensitiveCompare:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/caseInsensitiveCompare:) method if case sensitivity is unimportant. However, consider replacing these method signatures with the [localizedCompare:](https://developer.apple.com/documentation/foundation/nsstring/1416999-localizedcompare) or [localizedCaseInsensitiveCompare:](https://developer.apple.com/documentation/foundation/nsstring/1417333-localizedcaseinsensitivecompare) methods to take into the account the user’s language requirements.
- The Order pop-up menu allows you to specify the initial order of the sort, as ascending (default) or descending.

Leaving the Sort Key and Selector fields blank disables sorting of the column using the settings within Interface Builder. However, it does not disable sorting of the column using other techniques.

When a table view is sorted through user action or by setting the table view’s sort descriptors, the data source receives a [tableView:sortDescriptorsDidChange:](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1532935-tableview) message. The data source must implement this method to support sorting.

The [tableView:sortDescriptorsDidChange:](https://developer.apple.com/documentation/appkit/nstableviewdatasource/1532935-tableview) method applies the table view’s current sort descriptors to the model collection, and then reloads the table view data. A typical implementation of this delegate method is shown in Listing 7-1.

__Listing 7-1__  Sample implementation of the delegate method `tableView:sortDescriptorsDidChange:`

```objc
- (void)tableView:(NSTableView *)tableView sortDescriptorsDidChange:(NSArray *)oldDescriptors
{
    [peopleArray sortUsingDescriptors: [tableView sortDescriptors]];
    [tableView reloadData];
}
```

The implementation shown in Listing 7-1 sorts the current model content using the table view sort descriptors, but it also loses the initial order of the data. If the initial order is important to your app, you’ll want to take steps to cache the original order so that it can be restored.

[Next](Working%20with%20NSCell-Based%20Table%20Views.md)[Previous](Enabling%20Row%20Selection%20and%20User%20Actions.md)

