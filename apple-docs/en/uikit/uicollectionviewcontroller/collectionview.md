---
title: collectionView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewcontroller/collectionview
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/collectionview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcontroller/collectionview.json'
content_hash: 'sha256:47854eefeacf599e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewController](../uicollectionviewcontroller.md)

# collectionView

<sub>Instance Property</sub>

The collection view object managed by this view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var collectionView: UICollectionView! { get set }
```

## Discussion

If you assign a new collection view object to this property and that view’s data source or delegate aren’t yet set, the collection view controller makes itself the delegate or data source or both.

## See Also

### Getting the collection view

- [collectionViewLayout](collectionviewlayout.md) — The layout object used to initialize the collection view controller.
