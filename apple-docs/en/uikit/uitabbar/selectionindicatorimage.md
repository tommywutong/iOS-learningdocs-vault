---
title: selectionIndicatorImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbar/selectionindicatorimage
source_url: 'https://developer.apple.com/documentation/uikit/uitabbar/selectionindicatorimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbar/selectionindicatorimage.json'
content_hash: 'sha256:0deb0a5dfc13e9e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBar](../uitabbar.md)

# selectionIndicatorImage

<sub>Instance Property</sub>

The image to use for the selection indicator.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var selectionIndicatorImage: UIImage? { get set }
```

## Discussion

Use this property to specify a custom selection image. Your image is rendered on top of the tab bar but behind the contents of the tab bar item itself. The default value of this property is `nil`, which causes the tab bar to apply a default highlight to the selected item.

## See Also

### Configuring selection appearance

- [unselectedItemTintColor](unselecteditemtintcolor.md) — The tint color to apply to unselected tabs.
- [selectedImageTintColor](selectedimagetintcolor.md) — The tint color applied to the selected tab bar item. _(deprecated)_
