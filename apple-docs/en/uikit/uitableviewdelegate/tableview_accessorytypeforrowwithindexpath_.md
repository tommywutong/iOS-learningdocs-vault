---
title: 'tableView:accessoryTypeForRowWithIndexPath:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（3.0 起废弃）, iPadOS 2.0+（3.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uitableviewdelegate/tableview:accessorytypeforrowwithindexpath:'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview:accessorytypeforrowwithindexpath:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%3Aaccessorytypeforrowwithindexpath%3A.json'
content_hash: 'sha256:7919575f78dd17aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView:accessoryTypeForRowWithIndexPath:

<sub>Instance Method</sub>

Asks the delegate for the type of standard accessory view to use as a disclosure control for the specified row.

> [!warning] Deprecated
> Use the accessory-view and accessory-type properties (for both normal and editing modes) of the [UITableViewCell](../uitableviewcell.md) class when configuring table-view cells.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (UITableViewCellAccessoryType) tableView:(UITableView *) tableView accessoryTypeForRowWithIndexPath:(NSIndexPath *) indexPath;
```

## Parameters

- `tableView` — The table view requesting the accessory-view type.

- `indexPath` — An index path locating the row in `tableView`.

## Return Value

A constant identifying a type of standard accessory view. For details, see the “Constants” section in [UITableViewCell](../uitableviewcell.md).

## See Also

### Managing accessory views

- [- tableView:accessoryButtonTappedForRowWithIndexPath:](<tableview(__accessorybuttontappedforrowwith_).md>) — Tells the delegate that the user tapped the detail button for the specified row.
