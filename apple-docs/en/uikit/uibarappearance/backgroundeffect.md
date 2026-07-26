---
title: backgroundEffect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarappearance/backgroundeffect
source_url: 'https://developer.apple.com/documentation/uikit/uibarappearance/backgroundeffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarappearance/backgroundeffect.json'
content_hash: 'sha256:991a035d7c1f52fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarAppearance](../uibarappearance.md)

# backgroundEffect

<sub>Instance Property</sub>

The blur effect to apply to the bar’s background.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var backgroundEffect: UIBlurEffect? { get set }
```

## Discussion

The blur effect provides the base layer for the bar’s appearance, and it determines how much of the underlying content is visible. UIKit applies the [backgroundColor](backgroundcolor.md) and [backgroundImage](backgroundimage.md) on top of this effect.

## See Also

### Configuring the background appearance

- [backgroundColor](backgroundcolor.md) — The background color of the bar.
- [backgroundImage](backgroundimage.md) — The image to display on top of the bar’s background color.
- [backgroundImageContentMode](backgroundimagecontentmode.md) — The content mode to use when displaying the bar’s background image.
