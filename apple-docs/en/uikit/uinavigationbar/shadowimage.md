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
doc_path: /documentation/uikit/uinavigationbar/shadowimage
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar/shadowimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar/shadowimage.json'
content_hash: 'sha256:95ac52ec2afdb3fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBar](../uinavigationbar.md)

# shadowImage

<sub>Instance Property</sub>

The shadow image to be used for the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var shadowImage: UIImage? { get set }
```

## Discussion

The default value is `nil`, which corresponds to the default shadow image. When non-`nil`, this property represents a custom shadow image to show instead of the default. To show a custom shadow image, you must also set a custom background image with the [- setBackgroundImage:forBarMetrics:](<setbackgroundimage(__for_).md>) method. If the default background image is used, then the default shadow image is used regardless of the value of this property.
