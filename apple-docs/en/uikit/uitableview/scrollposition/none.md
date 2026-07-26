---
title: UITableView.ScrollPosition.none
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/scrollposition/none
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/scrollposition/none'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/scrollposition/none.json'
content_hash: 'sha256:3d63473f1f08a2f2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITableView](../../uitableview.md) · [ScrollPosition](../scrollposition.md)

# UITableView.ScrollPosition.none

<sub>Case</sub>

The table view scrolls the row of interest to be fully visible with a minimum of movement.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case none
```

## Discussion

If the row is already fully visible, no scrolling occurs. For example, if the row is above the visible area, the behavior is identical to that specified by [UITableViewScrollPositionTop](top.md). This is the default.

## See Also

### Constants

- [UITableViewScrollPositionTop](top.md) — The table view scrolls the row of interest to the top of the visible table view.
- [UITableViewScrollPositionMiddle](middle.md) — The table view scrolls the row of interest to the middle of the visible table view.
- [UITableViewScrollPositionBottom](bottom.md) — The table view scrolls the row of interest to the bottom of the visible table view.
