---
title: UIVibrancyEffect
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uivibrancyeffect
source_url: 'https://developer.apple.com/documentation/uikit/uivibrancyeffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uivibrancyeffect.json'
content_hash: 'sha256:856017f3a330d494'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIVibrancyEffect

<sub>Class</sub>

An object that amplifies and adjusts the color of the content layered behind a visual effect view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIVibrancyEffect
```

## Overview

A vibrancy effect is intended to be used as a subview of or layered on top of a [UIVisualEffectView](uivisualeffectview.md) that has been configured with a [UIBlurEffect](uiblureffect.md). The use of a vibrancy effect can help the content placed inside the [contentView](uivisualeffectview/contentview.md) become more vivid.

The vibrancy effect is color-dependent. Any subviews that you add to the [contentView](uivisualeffectview/contentview.md) must implement the [- tintColorDidChange](<uiview/tintcolordidchange().md>) method and update themselves accordingly. [UIImageView](uiimageview.md) objects with images that have a rendering mode of [UIImageRenderingModeAlwaysTemplate](uiimage/renderingmode-swift.enum/alwaystemplate.md) as well as [UILabel](uilabel.md) objects update automatically.

## Relationships

- **Inherits From**: [UIVisualEffect](uivisualeffect.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a vibrancy effect

- [init(forBlurEffect:style:)](<uivibrancyeffect/init(forblureffect_style_).md>) — Creates a vibrancy effect with the specified blur and style values.
- [+ effectForBlurEffect:](<uivibrancyeffect/init(blureffect_).md>) — Creates a vibrancy effect for a specific blur effect.
- [UIVibrancyEffectStyle](uivibrancyeffectstyle.md) — Constants for the vibrancy styles.

### Deprecated

- [+ widgetPrimaryVibrancyEffect](<uivibrancyeffect/widgetprimary().md>) — Creates a vibrancy effect suitable for use with certain supporting text and template images within a widget. _(deprecated)_
- [+ widgetSecondaryVibrancyEffect](<uivibrancyeffect/widgetsecondary().md>) — Creates a vibrancy effect suitable for indicating the secondary importance or relevance of supporting text and template images within a widget. _(deprecated)_
- [+ widgetEffectForVibrancyStyle:](<uivibrancyeffect/widgeteffect(forvibrancystyle_).md>) — Creates a vibrancy effect for the specified style. _(deprecated)_
- [+ notificationCenterVibrancyEffect](<uivibrancyeffect/notificationcenter().md>) — Creates a vibrancy effect for use in Notification Center. _(deprecated)_

### Initializers

- [+ effectForBlurEffect:style:](<uivibrancyeffect/init(blureffect_style_).md>)
- [init(forBlurEffect:)](<uivibrancyeffect/init(forblureffect_).md>)

### Default Implementations

- [UIVibrancyEffect Implementations](uivibrancyeffect/uivibrancyeffect-implementations.md)

## See Also

### Visual effects

- [UIVisualEffect](uivisualeffect.md) — An initializer for visual effect views and blur and vibrancy effect objects.
- [UIVisualEffectView](uivisualeffectview.md) — An object that implements some complex visual effects.
- [UIBlurEffect](uiblureffect.md) — An object that applies a blurring effect to the content layered behind a visual effect view.
- [UIColorEffect](uicoloreffect.md) — A visual effect that applies a solid color background.
