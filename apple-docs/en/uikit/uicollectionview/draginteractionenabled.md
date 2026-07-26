---
title: dragInteractionEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/draginteractionenabled
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/draginteractionenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/draginteractionenabled.json'
content_hash: 'sha256:4586db229da21796'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# dragInteractionEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the collection view supports dragging content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var dragInteractionEnabled: Bool { get set }
```

## Discussion

To support dragging content from the collection view to a view in your app or another app, set this property value to [true](../../swift/true.md). To disable this behavior, set the value to [false](../../swift/false.md). The default value is [true](../../swift/true.md).

In iOS 14 and earlier, the default value is [true](../../swift/true.md) for iPad and [false](../../swift/false.md) for iPhone. Setting the value to [true](../../swift/true.md) on iPhone enables dragging within your app only. Dragging content to other apps isn’t possible on iPhone prior to iOS 15.

## See Also

### Managing drag interactions

- [dragDelegate](dragdelegate.md) — The delegate object that manages the dragging of items from the collection view.
- [UICollectionViewDragDelegate](../uicollectionviewdragdelegate.md) — The interface for initiating drags from a collection view.
- [hasActiveDrag](hasactivedrag.md) — A Boolean value that indicates whether items were lifted from the collection view and have not yet been dropped.
