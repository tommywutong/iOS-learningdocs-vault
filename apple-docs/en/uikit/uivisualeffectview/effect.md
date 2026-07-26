---
title: effect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uivisualeffectview/effect
source_url: 'https://developer.apple.com/documentation/uikit/uivisualeffectview/effect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uivisualeffectview/effect.json'
content_hash: 'sha256:31628d69b36306cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIVisualEffectView](../uivisualeffectview.md)

# effect

<sub>Instance Property</sub>

The visual effect provided by the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var effect: UIVisualEffect? { get set }
```

## Discussion

The effect is either a [UIBlurEffect](../uiblureffect.md) or a [UIVibrancyEffect](../uivibrancyeffect.md).

## See Also

### Retrieving view information

- [contentView](contentview.md) — A view object that can have a visual effect view added to it.
