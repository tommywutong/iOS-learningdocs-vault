---
title: 'init(effect:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uivisualeffectview/init(effect:)'
source_url: 'https://developer.apple.com/documentation/uikit/uivisualeffectview/init(effect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uivisualeffectview/init%28effect%3A%29.json'
content_hash: 'sha256:899f71ee6b9cce93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIVisualEffectView](../uivisualeffectview.md)

# init(effect:)

<sub>Initializer</sub>

Creates a new visual effect view with the designated visual effect.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(effect: UIVisualEffect?)
```

## Parameters

- `effect` — The [UIVisualEffect](../uivisualeffect.md) you provide for the view. This can be a [UIBlurEffect](../uiblureffect.md) or a [UIVibrancyEffect](../uivibrancyeffect.md).

## Return Value

The new view containing the designated visual effect.

## See Also

### Creating a visual effect view

- [- initWithCoder:](<init(coder_).md>) — Creates a visual effect view from data in an unarchiver.
