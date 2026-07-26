---
title: supplementaryContentInsetsReference
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nscollectionlayoutsection/supplementarycontentinsetsreference
source_url: 'https://developer.apple.com/documentation/uikit/nscollectionlayoutsection/supplementarycontentinsetsreference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscollectionlayoutsection/supplementarycontentinsetsreference.json'
content_hash: 'sha256:2e0402041a3b106b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSCollectionLayoutSection](../nscollectionlayoutsection.md)

# supplementaryContentInsetsReference

<sub>Instance Property</sub>

The reference boundary for content insets on boundary supplementary items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var supplementaryContentInsetsReference: UIContentInsetsReference { get set }
```

## Discussion

This property represents the reference boundary to use when defining [contentInsets](../nscollectionlayoutitem/contentinsets.md) on [NSCollectionLayoutBoundarySupplementaryItem](../nscollectionlayoutboundarysupplementaryitem.md) objects.

The default value of this property is [UIContentInsetsReferenceAutomatic](../uicontentinsetsreference/automatic.md), which means any insets specified on a [NSCollectionLayoutBoundarySupplementaryItem](../nscollectionlayoutboundarysupplementaryitem.md) follow the layout configuration’s [contentInsetsReference](../uicollectionviewcompositionallayoutconfiguration/contentinsetsreference.md).

## See Also

### Configuring section spacing

- [interGroupSpacing](intergroupspacing.md) — The amount of space between the groups in the section.
- [contentInsets](contentinsets.md) — The amount of space between the content of the section and its boundaries.
- [contentInsetsReference](contentinsetsreference.md) — The boundary to reference when defining content insets.
- [UIContentInsetsReference](../uicontentinsetsreference.md) — Constants that describe the reference point of the content insets.
