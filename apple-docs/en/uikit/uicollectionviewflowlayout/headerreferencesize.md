---
title: headerReferenceSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewflowlayout/headerreferencesize
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/headerreferencesize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewflowlayout/headerreferencesize.json'
content_hash: 'sha256:3ed8c7828b02cb15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewFlowLayout](../uicollectionviewflowlayout.md)

# headerReferenceSize

<sub>Instance Property</sub>

The default sizes to use for section headers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var headerReferenceSize: CGSize { get set }
```

## Discussion

If the delegate does not implement the [- collectionView:layout:referenceSizeForHeaderInSection:](<../uicollectionviewdelegateflowlayout/collectionview(__layout_referencesizeforheaderinsection_).md>) method, the flow layout object uses the default header sizes set in this property.

During layout, only the size that corresponds to the appropriate scrolling direction is used. For example, for the vertical scrolling direction, the layout object uses the height value returned by your method. (In that instance, the width of the header would be set to the width of the collection view.) If the size in the appropriate scrolling dimension is 0, no header is added.

The default size values are (0, 0).

## See Also

### Configuring headers and footers

- [footerReferenceSize](footerreferencesize.md) — The default sizes to use for section footers.
- [Flow layout supplementary views](../flow-layout-supplementary-views.md) — Constants that specify the types of supplementary views that can be presented using a flow layout.
