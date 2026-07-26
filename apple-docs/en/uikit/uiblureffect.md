---
title: UIBlurEffect
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiblureffect
source_url: 'https://developer.apple.com/documentation/uikit/uiblureffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiblureffect.json'
content_hash: 'sha256:56a6fb27a4426de1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIBlurEffect

<sub>Class</sub>

An object that applies a blurring effect to the content layered behind a visual effect view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIBlurEffect
```

## Overview

Views that you add to the [contentView](uivisualeffectview/contentview.md) of a visual effect view aren’t affected by the blur effect.

## Relationships

- **Inherits From**: [UIVisualEffect](uivisualeffect.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a blur effect

- [+ effectWithStyle:](<uiblureffect/init(style_).md>) — Creates a blur effect with the designated style.

### Constants

- [Style](uiblureffect/style.md) — Blur styles available for blur effect objects.

## See Also

### Visual effects

- [UIVisualEffect](uivisualeffect.md) — An initializer for visual effect views and blur and vibrancy effect objects.
- [UIVisualEffectView](uivisualeffectview.md) — An object that implements some complex visual effects.
- [UIVibrancyEffect](uivibrancyeffect.md) — An object that amplifies and adjusts the color of the content layered behind a visual effect view.
- [UIColorEffect](uicoloreffect.md) — A visual effect that applies a solid color background.
