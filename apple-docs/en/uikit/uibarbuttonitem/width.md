---
title: width
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarbuttonitem/width
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/width'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/width.json'
content_hash: 'sha256:3246398d1272544c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# width

<sub>Instance Property</sub>

The width of the item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var width: CGFloat { get set }
```

## Discussion

If this property value is positive, the width of the combined image and title are fixed. If the value is `0.0` or negative, the item sets the width of the combined image and title to fit. This property is ignored if the style uses radio mode. The default value is `0.0`.

## See Also

### Customizing item appearance

- [style](style-swift.property.md) — The style of the item.
- [Style](style-swift.enum.md) — Constants that specify the style of an item.
- [tintColor](tintcolor.md) — The tint color to apply to the button item.
- [hidden](ishidden.md) — A Boolean that determines the visibility of the item.
- [selected](isselected.md) — A Boolean value that indicates whether the button is in a selected state.
- [possibleTitles](possibletitles.md) — The set of possible titles to display on the bar button.
