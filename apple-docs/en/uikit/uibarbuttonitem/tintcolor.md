---
title: tintColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarbuttonitem/tintcolor
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/tintcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/tintcolor.json'
content_hash: 'sha256:95ddec4b4eba65c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# tintColor

<sub>Instance Property</sub>

The tint color to apply to the button item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var tintColor: UIColor? { get set }
```

## Discussion

In iOS 7 and later, all subclasses of [UIView](../uiview.md) derive their behavior for [tintColor](../uiview/tintcolor.md) from the base class. Although [UIBarButtonItem](../uibarbuttonitem.md) isn’t a view, its [tintColor](tintcolor.md) property behaves the same as that of [UIView](../uiview.md). See the discussion of [tintColor](../uiview/tintcolor.md) in [UIView](../uiview.md) for more information.

## See Also

### Customizing item appearance

- [style](style-swift.property.md) — The style of the item.
- [Style](style-swift.enum.md) — Constants that specify the style of an item.
- [hidden](ishidden.md) — A Boolean that determines the visibility of the item.
- [selected](isselected.md) — A Boolean value that indicates whether the button is in a selected state.
- [width](width.md) — The width of the item.
- [possibleTitles](possibletitles.md) — The set of possible titles to display on the bar button.
