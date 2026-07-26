---
title: 'init(forBlurEffect:style:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uivibrancyeffect/init(forblureffect:style:)'
source_url: 'https://developer.apple.com/documentation/uikit/uivibrancyeffect/init(forblureffect:style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uivibrancyeffect/init%28forblureffect%3Astyle%3A%29.json'
content_hash: 'sha256:f015d49e37bf749f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIVibrancyEffect](../uivibrancyeffect.md)

# init(forBlurEffect:style:)

<sub>Initializer</sub>

Creates a vibrancy effect with the specified blur and style values.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(forBlurEffect blurEffect: UIBlurEffect, style: UIVibrancyEffectStyle)
```

## Parameters

- `blurEffect` — The [UIBlurEffect](../uiblureffect.md) used by the blurred view the vibrancy effect is attached to.

- `style` — The style that defines what level of vibrancy to apply to the content. For a list of possible values, see [UIVibrancyEffectStyle](../uivibrancyeffectstyle.md).

## Return Value

The vibrancy effect object to use in your visual effect view.

## Discussion

When you create a new vibrancy effect, use the same [UIBlurEffect](../uiblureffect.md) that you used to create the blur view. Using a different [UIBlurEffect](../uiblureffect.md) can cause unwanted visual effect combinations.

## See Also

### Creating a vibrancy effect

- [+ effectForBlurEffect:](<init(blureffect_).md>) — Creates a vibrancy effect for a specific blur effect.
- [UIVibrancyEffectStyle](../uivibrancyeffectstyle.md) — Constants for the vibrancy styles.
