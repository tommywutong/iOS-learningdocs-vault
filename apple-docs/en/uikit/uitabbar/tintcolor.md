---
title: tintColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbar/tintcolor
source_url: 'https://developer.apple.com/documentation/uikit/uitabbar/tintcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbar/tintcolor.json'
content_hash: 'sha256:9bdf8921a7ee6d40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBar](../uitabbar.md)

# tintColor

<sub>Instance Property</sub>

The tint color to apply to the tab bar items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var tintColor: UIColor! { get set }
```

## Discussion

Assigning a value to this property applies the specified color only to the tab bar’s items. Even if you do not specify a color, the tab bar may tint items using the tint color of one of its ancestor views. For information on how tinting colors are applied to views in a view hierarchy, see the description of the [tintColor](../uiview/tintcolor.md) property in [UIView](../uiview.md).
