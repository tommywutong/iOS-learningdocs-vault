---
title: 'scrollToNearestSelectedRow(at:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/scrolltonearestselectedrow(at:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/scrolltonearestselectedrow(at:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/scrolltonearestselectedrow%28at%3Aanimated%3A%29.json'
content_hash: 'sha256:9f66bc69cf73a8a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# scrollToNearestSelectedRow(at:animated:)

<sub>Instance Method</sub>

Scrolls the table view so that the selected row nearest to a specified position in the table view is at that position.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func scrollToNearestSelectedRow(at scrollPosition: UITableView.ScrollPosition, animated: Bool)
```

## Parameters

- `scrollPosition` — A constant that identifies a relative position in the table view (top, middle, bottom) for the row when scrolling concludes. See [ScrollPosition](scrollposition.md) for a descriptions of valid constants.

- `animated` — [true](../../swift/true.md) if you want to animate the change in position; [false](../../swift/false.md) if it should be immediate.

## See Also

### Scrolling the table view

- [- scrollToRowAtIndexPath:atScrollPosition:animated:](<scrolltorow(at_at_animated_).md>) — Scrolls through the table view until a row that an index path identifies is at a particular location on the screen.
- [ScrollPosition](scrollposition.md) — The position in the table view (top, middle, bottom) to scroll a specified row to.
