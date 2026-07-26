---
title: contentInsetsReference
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nscollectionlayoutsection/contentinsetsreference
source_url: 'https://developer.apple.com/documentation/uikit/nscollectionlayoutsection/contentinsetsreference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscollectionlayoutsection/contentinsetsreference.json'
content_hash: 'sha256:a754ba8bd53143bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSCollectionLayoutSection](../nscollectionlayoutsection.md)

# contentInsetsReference

<sub>Instance Property</sub>

The boundary to reference when defining content insets.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contentInsetsReference: UIContentInsetsReference { get set }
```

## Discussion

This property represents the reference point to use when defining [contentInsets](contentinsets.md).

The default value of this property is [UIContentInsetsReferenceAutomatic](../uicontentinsetsreference/automatic.md), which means the section follows the layout configuration’s [contentInsetsReference](../uicollectionviewcompositionallayoutconfiguration/contentinsetsreference.md).

## See Also

### Configuring section spacing

- [interGroupSpacing](intergroupspacing.md) — The amount of space between the groups in the section.
- [contentInsets](contentinsets.md) — The amount of space between the content of the section and its boundaries.
- [supplementaryContentInsetsReference](supplementarycontentinsetsreference.md) — The reference boundary for content insets on boundary supplementary items.
- [UIContentInsetsReference](../uicontentinsetsreference.md) — Constants that describe the reference point of the content insets.
