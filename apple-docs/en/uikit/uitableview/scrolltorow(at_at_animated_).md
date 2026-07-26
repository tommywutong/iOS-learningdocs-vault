---
title: 'scrollToRow(at:at:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/scrolltorow(at:at:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/scrolltorow(at:at:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/scrolltorow%28at%3Aat%3Aanimated%3A%29.json'
content_hash: 'sha256:3239842ee6f7d8f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# scrollToRow(at:at:animated:)

<sub>Instance Method</sub>

Scrolls through the table view until a row that an index path identifies is at a particular location on the screen.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func scrollToRow(at indexPath: IndexPath, at scrollPosition: UITableView.ScrollPosition, animated: Bool)
```

## Parameters

- `indexPath` — An index path that identifies a row in the table view by its row index and its section index. `NSNotFound` is a valid row index for scrolling to a section with zero rows.

- `scrollPosition` — A constant that identifies a relative position in the table view (top, middle, bottom) for `row` when scrolling concludes. See [ScrollPosition](scrollposition.md) for descriptions of valid constants.

- `animated` — [true](../../swift/true.md) if you want to animate the change in position; [false](../../swift/false.md) if it should be immediate.

## Discussion

Invoking this method doesn’t cause the delegate to receive a [- scrollViewDidScroll:](<../uiscrollviewdelegate/scrollviewdidscroll(__).md>) message, as is normal for programmatically invoked user interface operations.

## See Also

### Scrolling the table view

- [- scrollToNearestSelectedRowAtScrollPosition:animated:](<scrolltonearestselectedrow(at_animated_).md>) — Scrolls the table view so that the selected row nearest to a specified position in the table view is at that position.
- [ScrollPosition](scrollposition.md) — The position in the table view (top, middle, bottom) to scroll a specified row to.
