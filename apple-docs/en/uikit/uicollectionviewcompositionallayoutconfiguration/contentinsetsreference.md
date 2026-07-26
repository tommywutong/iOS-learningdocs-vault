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
doc_path: /documentation/uikit/uicollectionviewcompositionallayoutconfiguration/contentinsetsreference
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcompositionallayoutconfiguration/contentinsetsreference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcompositionallayoutconfiguration/contentinsetsreference.json'
content_hash: 'sha256:ab133ed5ed1c8bb0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewCompositionalLayoutConfiguration](../uicollectionviewcompositionallayoutconfiguration.md)

# contentInsetsReference

<sub>Instance Property</sub>

The boundary to reference when defining content insets.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contentInsetsReference: UIContentInsetsReference { get set }
```

## Discussion

The default value of this property is [UIContentInsetsReferenceSafeArea](../uicontentinsetsreference/safearea.md).

## See Also

### Configuring spacing

- [interSectionSpacing](intersectionspacing.md) — The amount of space between the sections in the layout.
- [UIContentInsetsReference](../uicontentinsetsreference.md) — Constants that describe the reference point of the content insets.
