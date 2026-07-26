---
title: footerReferenceSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewflowlayout/footerreferencesize
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/footerreferencesize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewflowlayout/footerreferencesize.json'
content_hash: 'sha256:191f29fba262f4c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewFlowLayout](../uicollectionviewflowlayout.md)

# footerReferenceSize

<sub>Instance Property</sub>

The default sizes to use for section footers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var footerReferenceSize: CGSize { get set }
```

## Discussion

If the delegate does not implement the [- collectionView:layout:referenceSizeForFooterInSection:](<../uicollectionviewdelegateflowlayout/collectionview(__layout_referencesizeforfooterinsection_).md>) method, the flow layout object uses the default footer sizes set for this property.

During layout, only the size that corresponds to the appropriate scrolling direction is used. For example, for the vertical scrolling direction, the layout object uses the height value specified by this property. (In that instance, the width of the footer would be set to the width of the collection view.) If the size in the appropriate scrolling dimension is 0, no footer is added.

The default size values are (0, 0).

## See Also

### Related Documentation

- [sectionInset](sectioninset.md) — The margins used to lay out content in a section.

### Configuring headers and footers

- [headerReferenceSize](headerreferencesize.md) — The default sizes to use for section headers.
- [Flow layout supplementary views](../flow-layout-supplementary-views.md) — Constants that specify the types of supplementary views that can be presented using a flow layout.
