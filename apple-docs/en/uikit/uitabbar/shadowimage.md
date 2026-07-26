---
title: shadowImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbar/shadowimage
source_url: 'https://developer.apple.com/documentation/uikit/uitabbar/shadowimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbar/shadowimage.json'
content_hash: 'sha256:a1bdc077181e5051'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBar](../uitabbar.md)

# shadowImage

<sub>Instance Property</sub>

The shadow image to use for the tab bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var shadowImage: UIImage? { get set }
```

## Discussion

For tab bars with custom backgrounds, you can use this property to specify a custom shadow image for your bar. The shadow image is positioned outside the bounds of the tab bar itself, usually above or below the tab bar’s frame rectangle. The exact position depends on the current platform. For example, shadow images are positioned above the tab bar on iPhone and iPad.

You must use this property in conjunction with a custom background image. If the [backgroundImage](backgroundimage.md) property is `nil`, the tab bar ignores the value in this property and uses a default shadow.
