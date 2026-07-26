---
title: UICollectionView.ScrollPosition
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/scrollposition
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/scrollposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/scrollposition.json'
content_hash: 'sha256:b27461e7c9a74ef2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# UICollectionView.ScrollPosition

<sub>Structure</sub>

Constants that indicate how to scroll an item into the visible portion of the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct ScrollPosition
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [UICollectionViewScrollPositionTop](scrollposition/top.md) — Scroll so that the item is positioned at the top of the collection view’s bounds.
- [UICollectionViewScrollPositionCenteredVertically](scrollposition/centeredvertically.md) — Scroll so that the item is centered vertically in the collection view.
- [UICollectionViewScrollPositionBottom](scrollposition/bottom.md) — Scroll so that the item is positioned at the bottom of the collection view’s bounds.
- [UICollectionViewScrollPositionLeft](scrollposition/left.md) — Scroll so that the item is positioned at the left edge of the collection view’s bounds.
- [UICollectionViewScrollPositionCenteredHorizontally](scrollposition/centeredhorizontally.md) — Scroll so that the item is centered horizontally in the collection view.
- [UICollectionViewScrollPositionRight](scrollposition/right.md) — Scroll so that the item is positioned at the right edge of the collection view’s bounds.

### Initializers

- [init(rawValue:)](<scrollposition/init(rawvalue_).md>) — Creates a scroll-position structure with the specified raw value.

## See Also

### Scrolling an item into view

- [- scrollToItemAtIndexPath:atScrollPosition:animated:](<scrolltoitem(at_at_animated_).md>) — Scrolls the collection view contents until the specified item is visible.
- [ScrollDirection](scrolldirection.md) — Constants that indicate the direction of scrolling for the layout.
