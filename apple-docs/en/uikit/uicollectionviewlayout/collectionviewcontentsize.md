---
title: collectionViewContentSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayout/collectionviewcontentsize
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/collectionviewcontentsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/collectionviewcontentsize.json'
content_hash: 'sha256:60745c21fcc16ab2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# collectionViewContentSize

<sub>Instance Property</sub>

The width and height of the collection view’s contents.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var collectionViewContentSize: CGSize { get }
```

## Return Value

The width and height of the collection view’s contents.

## Discussion

Subclasses must override this property and use it to return the width and height of the collection view’s content. These values represent the width and height of all the content, not just the content that is currently visible. The collection view uses this information to configure its own content size for scrolling purposes.

The default implementation of this method returns [CGSizeZero](../../coregraphics/cgsizezero.md).

## See Also

### Getting the collection view information

- [collectionView](collectionview.md) — The collection view object currently using this layout object.
