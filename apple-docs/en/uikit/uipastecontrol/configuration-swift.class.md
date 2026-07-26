---
title: UIPasteControl.Configuration
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipastecontrol/configuration-swift.class
source_url: 'https://developer.apple.com/documentation/uikit/uipastecontrol/configuration-swift.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipastecontrol/configuration-swift.class.json'
content_hash: 'sha256:417ce9f536f14ea9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteControl](../uipastecontrol.md)

# UIPasteControl.Configuration

<sub>Class</sub>

An object that determines a paste button’s color, corner style, icon, and text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class Configuration
```

## Overview

The paste button ([UIPasteControl](../uipastecontrol.md)) property [configuration](configuration-swift.property.md) is of this type.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSCoding](../../foundation/nscoding.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [NSSecureCoding](../../foundation/nssecurecoding.md), [Sendable](../../swift/sendable.md)

## Topics

### Coloring the button

- [baseBackgroundColor](configuration-swift.class/basebackgroundcolor.md) — A color for the paste button’s background.
- [baseForegroundColor](configuration-swift.class/baseforegroundcolor.md) — A color for the paste button’s icon and text.

### Shaping button corners

- [cornerRadius](configuration-swift.class/cornerradius.md) — A value that rounds the edges of a paste button.
- [cornerStyle](configuration-swift.class/cornerstyle.md) — A shape for the button among a predetermined set of templates.

### Choosing control icon and text

- [displayMode](configuration-swift.class/displaymode.md) — An option that determines whether the paste button composes an icon, textual label, or both.
- [DisplayMode](displaymode.md) — Options that determine whether a paste button composes an icon, textual label, or both.

### Initializers

- [init(coder:)](<configuration-swift.class/init(coder_).md>)

### Instance Properties

- [imagePlacement](configuration-swift.class/imageplacement.md)

## See Also

### Pasteboard

- [UIPasteControl](../uipastecontrol.md) — A button that a person taps to place pasteboard contents in your app.
- [DisplayMode](displaymode.md) — Options that determine whether a paste button composes an icon, textual label, or both.
- [UIPasteboard](../uipasteboard.md) — An object that helps a user share data from one place to another within your app, and from your app to other apps.
- [UIPasteConfiguration](../uipasteconfiguration.md) — The interface that an object implements to declare its ability to accept specific data types for pasting and for drag-and-drop activities.
- [UIPasteConfigurationSupporting](../uipasteconfigurationsupporting.md) — The interface that determines whether a responder object supports paste configuration.
