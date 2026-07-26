---
title: hasUncommittedUpdates
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/hasuncommittedupdates
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/hasuncommittedupdates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/hasuncommittedupdates.json'
content_hash: 'sha256:a8c62ebea780a1c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# hasUncommittedUpdates

<sub>Instance Property</sub>

A Boolean value that indicates whether the table view’s appearance contains changes that aren’t present in its data source.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var hasUncommittedUpdates: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) when the table view contains placeholder cells or is handling a drop and is in the middle of reordering its rows. When this property is [true](../../swift/true.md), avoid making any significant changes to the table view. Specifically, don’t call [- reloadData](<reloaddata().md>), which forces the table to delete any uncommitted changes before retrieving fresh data from the data source object.

## See Also

### Reloading the table view

- [- reconfigureRowsAtIndexPaths:](<reconfigurerows(at_).md>) — Updates the data for the rows at the index paths you specify, preserving the existing cells for the rows.
- [- reloadData](<reloaddata().md>) — Reloads the rows and sections of the table view.
- [- reloadRowsAtIndexPaths:withRowAnimation:](<reloadrows(at_with_).md>) — Reloads the specified rows using the provided animation effect.
- [- reloadSections:withRowAnimation:](<reloadsections(__with_).md>) — Reloads the specified sections using the provided animation effect.
- [- reloadSectionIndexTitles](<reloadsectionindextitles().md>) — Reloads the items in the index bar along the right side of the table view.
