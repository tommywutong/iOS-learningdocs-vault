---
title: collectionViewLayout
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewcontroller/collectionviewlayout
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/collectionviewlayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcontroller/collectionviewlayout.json'
content_hash: 'sha256:852b6c0631598657'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewController](../uicollectionviewcontroller.md)

# collectionViewLayout

<sub>Instance Property</sub>

The layout object used to initialize the collection view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var collectionViewLayout: UICollectionViewLayout { get }
```

## Discussion

This property contains the layout object you passed to the [- initWithCollectionViewLayout:](<init(collectionviewlayout_).md>) method. The layout object in this property isn’t updated to reflect changes to the collection view itself. You can use this property to refer to the layout object you originally configured the collection view to use.

## See Also

### Getting the collection view

- [collectionView](collectionview.md) — The collection view object managed by this view controller.
