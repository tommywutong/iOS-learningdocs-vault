---
title: titlePositionAdjustment
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarbuttonitemstateappearance/titlepositionadjustment
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitemstateappearance/titlepositionadjustment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitemstateappearance/titlepositionadjustment.json'
content_hash: 'sha256:cf6844a05fde542e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItemStateAppearance](../uibarbuttonitemstateappearance.md)

# titlePositionAdjustment

<sub>Instance Property</sub>

The additional amount by which to offset the title horizontally and vertically.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var titlePositionAdjustment: UIOffset { get set }
```

## Discussion

Use this property to specify the distance, in points, by which to offset the title. Positive values move the title down and to the right. Negative values move the title up and to the left.

## See Also

### Configuring the title

- [titleTextAttributes](titletextattributes.md) — String attributes to apply to the text of the bar button item’s title.
