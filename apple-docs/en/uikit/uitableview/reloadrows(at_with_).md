---
title: 'reloadRows(at:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/reloadrows(at:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/reloadrows(at:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/reloadrows%28at%3Awith%3A%29.json'
content_hash: 'sha256:dc0016f072761862'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# reloadRows(at:with:)

<sub>Instance Method</sub>

Reloads the specified rows using the provided animation effect.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func reloadRows(at indexPaths: [IndexPath], with animation: UITableView.RowAnimation)
```

## Parameters

- `indexPaths` — An array of [NSIndexPath](../../foundation/nsindexpath.md) objects identifying the rows to reload.

- `animation` — A constant that indicates how the reloading is to be animated, for example, fade out or slide out from the bottom. See [RowAnimation](rowanimation.md) for descriptions of these constants. The animation constant affects the direction in which both the old and the new rows slide. For example, if the animation constant is [UITableViewRowAnimationRight](rowanimation/right.md), the old rows slide out to the right and the new cells slide in from the right.

## Discussion

Reloading a row causes the table view to ask its data source for a new cell for that row. The table animates that new cell in as it animates the old row out. Call this method if you want to alert the user that the value of a cell is changing. If, however, notifying the user isn’t important — that is, you just want to change the value that a cell is displaying — you can get the cell for a particular row and set its new value.

When this method is called in an animation block defined by the [- beginUpdates](<beginupdates().md>) and [- endUpdates](<endupdates().md>) methods, it behaves similarly to [- deleteRowsAtIndexPaths:withRowAnimation:](<deleterows(at_with_).md>). The indexes that [UITableView](../uitableview.md) passes to the method are specified in the state of the table view prior to any updates. This happens regardless of ordering of the insertion, deletion, and reloading method calls within the animation block.

## See Also

### Related Documentation

- [- insertRowsAtIndexPaths:withRowAnimation:](<insertrows(at_with_).md>) — Inserts rows in the table view at the locations that an array of index paths identifies, with an option to animate the insertion.

### Reloading the table view

- [hasUncommittedUpdates](hasuncommittedupdates.md) — A Boolean value that indicates whether the table view’s appearance contains changes that aren’t present in its data source.
- [- reconfigureRowsAtIndexPaths:](<reconfigurerows(at_).md>) — Updates the data for the rows at the index paths you specify, preserving the existing cells for the rows.
- [- reloadData](<reloaddata().md>) — Reloads the rows and sections of the table view.
- [- reloadSections:withRowAnimation:](<reloadsections(__with_).md>) — Reloads the specified sections using the provided animation effect.
- [- reloadSectionIndexTitles](<reloadsectionindextitles().md>) — Reloads the items in the index bar along the right side of the table view.
