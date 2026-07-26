---
title: collectionView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayout/collectionview
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/collectionview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/collectionview.json'
content_hash: 'sha256:28210ae5daf670c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# collectionView

<sub>Instance Property</sub>

The collection view object currently using this layout object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var collectionView: UICollectionView? { get }
```

## Discussion

The collection view object sets the value of this property when a new layout object is assigned to it.

## See Also

### Getting the collection view information

- [collectionViewContentSize](collectionviewcontentsize.md) — The width and height of the collection view’s contents.
