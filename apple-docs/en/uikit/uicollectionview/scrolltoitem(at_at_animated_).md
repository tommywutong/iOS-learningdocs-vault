---
title: 'scrollToItem(at:at:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/scrolltoitem(at:at:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/scrolltoitem(at:at:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/scrolltoitem%28at%3Aat%3Aanimated%3A%29.json'
content_hash: 'sha256:8c4b81ff89cce43f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# scrollToItem(at:at:animated:)

<sub>Instance Method</sub>

Scrolls the collection view contents until the specified item is visible.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func scrollToItem(at indexPath: IndexPath, at scrollPosition: UICollectionView.ScrollPosition, animated: Bool)
```

## Parameters

- `indexPath` — The index path of the item to scroll into view.

- `scrollPosition` — An option that specifies where the item should be positioned when scrolling finishes. For a list of possible values, see [ScrollPosition](scrollposition.md).

- `animated` — Specify [true](../../swift/true.md) to animate the scrolling behavior or [false](../../swift/false.md) to adjust the scroll view’s visible content immediately.

## See Also

### Scrolling an item into view

- [ScrollPosition](scrollposition.md) — Constants that indicate how to scroll an item into the visible portion of the collection view.
- [ScrollDirection](scrolldirection.md) — Constants that indicate the direction of scrolling for the layout.
