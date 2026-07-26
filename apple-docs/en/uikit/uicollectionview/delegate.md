---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/delegate.json'
content_hash: 'sha256:4e4bd407e939d94c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# delegate

<sub>Instance Property</sub>

The object that acts as the delegate of the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any UICollectionViewDelegate)? { get set }
```

## Discussion

The delegate must adopt the [UICollectionViewDelegate](../uicollectionviewdelegate.md) protocol. The delegate object is responsible for managing selection behavior and interactions with individual items.

## See Also

### Managing collection view interactions

- [UICollectionViewDelegate](../uicollectionviewdelegate.md) — The methods adopted by the object you use to manage user interactions with items in a collection view.
