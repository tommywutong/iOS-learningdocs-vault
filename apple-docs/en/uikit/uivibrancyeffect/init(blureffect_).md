---
title: 'init(blurEffect:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uivibrancyeffect/init(blureffect:)'
source_url: 'https://developer.apple.com/documentation/uikit/uivibrancyeffect/init(blureffect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uivibrancyeffect/init%28blureffect%3A%29.json'
content_hash: 'sha256:fe19fd142c70df15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIVibrancyEffect](../uivibrancyeffect.md)

# init(blurEffect:)

<sub>Initializer</sub>

Creates a vibrancy effect for a specific blur effect.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(blurEffect: UIBlurEffect)
```

## Parameters

- `blurEffect` — The [UIBlurEffect](../uiblureffect.md) used by the blurred view the vibrancy effect is attached to.

## Return Value

The vibrancy effect to be used by a [UIVisualEffectView](../uivisualeffectview.md) object.

## Discussion

When you create a new vibrancy effect, use the same [UIBlurEffect](../uiblureffect.md) that you used to create the blur view. Using a different [UIBlurEffect](../uiblureffect.md) can cause unwanted visual effect combinations.

## See Also

### Creating a vibrancy effect

- [init(forBlurEffect:style:)](<init(forblureffect_style_).md>) — Creates a vibrancy effect with the specified blur and style values.
- [UIVibrancyEffectStyle](../uivibrancyeffectstyle.md) — Constants for the vibrancy styles.
