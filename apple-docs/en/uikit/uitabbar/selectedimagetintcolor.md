---
title: selectedImageTintColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+（8.0 起废弃）, iPadOS 5.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uitabbar/selectedimagetintcolor
source_url: 'https://developer.apple.com/documentation/uikit/uitabbar/selectedimagetintcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbar/selectedimagetintcolor.json'
content_hash: 'sha256:485576289521f608'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBar](../uitabbar.md)

# selectedImageTintColor

<sub>Instance Property</sub>

The tint color applied to the selected tab bar item.

> [!warning] Deprecated
> Use the [tintColor](tintcolor.md) property instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var selectedImageTintColor: UIColor? { get set }
```

## Discussion

The default value is `nil`, which results in use of the tab bar’s [tintColor](tintcolor.md) property.

## See Also

### Configuring selection appearance

- [unselectedItemTintColor](unselecteditemtintcolor.md) — The tint color to apply to unselected tabs.
- [selectionIndicatorImage](selectionindicatorimage.md) — The image to use for the selection indicator.
