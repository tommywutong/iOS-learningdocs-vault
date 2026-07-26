---
title: reloadData()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/reloaddata()
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/reloaddata()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/reloaddata%28%29.json'
content_hash: 'sha256:42a5069ac5af16c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# reloadData()

<sub>Instance Method</sub>

Reloads the rows and sections of the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func reloadData()
```

## Discussion

Call this method to reload all the data that’s used to construct the table, including cells, section headers and footers, index arrays, and so on. For efficiency, the table view redisplays only those rows that are visible. It adjusts offsets if the table shrinks as a result of the reload. The table view’s delegate or data source calls this method when it wants the table view to completely reload its data. It shouldn’t be called in the methods that insert or delete rows, especially within an animation block implemented with calls to [- beginUpdates](<beginupdates().md>) and [- endUpdates](<endupdates().md>).

> [!important] Important
> Don’t call this method when the [hasUncommittedUpdates](hasuncommittedupdates.md) property is [true](../../swift/true.md). Doing so forces the table view to delete any uncommitted changes before reloading the data.

## See Also

### Reloading the table view

- [hasUncommittedUpdates](hasuncommittedupdates.md) — A Boolean value that indicates whether the table view’s appearance contains changes that aren’t present in its data source.
- [- reconfigureRowsAtIndexPaths:](<reconfigurerows(at_).md>) — Updates the data for the rows at the index paths you specify, preserving the existing cells for the rows.
- [- reloadRowsAtIndexPaths:withRowAnimation:](<reloadrows(at_with_).md>) — Reloads the specified rows using the provided animation effect.
- [- reloadSections:withRowAnimation:](<reloadsections(__with_).md>) — Reloads the specified sections using the provided animation effect.
- [- reloadSectionIndexTitles](<reloadsectionindextitles().md>) — Reloads the items in the index bar along the right side of the table view.
