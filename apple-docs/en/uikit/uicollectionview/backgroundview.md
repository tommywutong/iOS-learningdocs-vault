---
title: backgroundView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/backgroundview
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/backgroundview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/backgroundview.json'
content_hash: 'sha256:8172ea9d40736ce0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# backgroundView

<sub>Instance Property</sub>

The view that provides the background appearance.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var backgroundView: UIView? { get set }
```

## Discussion

The view (if any) in this property is positioned underneath all of the other content and sized automatically to fill the entire bounds of the collection view. The background view does not scroll with the collection view’s other content. The collection view maintains a strong reference to the background view object.

This property is `nil` by default, which displays the background color of the collection view.
