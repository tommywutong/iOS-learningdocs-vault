---
title: UIPasteControl.DisplayMode
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipastecontrol/displaymode
source_url: 'https://developer.apple.com/documentation/uikit/uipastecontrol/displaymode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipastecontrol/displaymode.json'
content_hash: 'sha256:e2a981b0f1fcbc9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteControl](../uipastecontrol.md)

# UIPasteControl.DisplayMode

<sub>Enumeration</sub>

Options that determine whether a paste button composes an icon, textual label, or both.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum DisplayMode
```

## Overview

The paste button ([UIPasteControl](../uipastecontrol.md)) property [displayMode](configuration-swift.class/displaymode.md) is of this type.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Choosing a display mode

- [UIPasteControlDisplayModeIconAndLabel](displaymode/iconandlabel.md) — A display mode for a button that composes an icon and a textual label.
- [UIPasteControlDisplayModeIconOnly](displaymode/icononly.md) — A display mode for an icon button.
- [UIPasteControlDisplayModeLabelOnly](displaymode/labelonly.md) — A display mode for a textual label.

### Enumeration Cases

- [UIPasteControlDisplayModeArrowAndLabel](displaymode/arrowandlabel.md)

### Initializers

- [init(rawValue:)](<displaymode/init(rawvalue_).md>)

## See Also

### Pasteboard

- [UIPasteControl](../uipastecontrol.md) — A button that a person taps to place pasteboard contents in your app.
- [Configuration](configuration-swift.class.md) — An object that determines a paste button’s color, corner style, icon, and text.
- [UIPasteboard](../uipasteboard.md) — An object that helps a user share data from one place to another within your app, and from your app to other apps.
- [UIPasteConfiguration](../uipasteconfiguration.md) — The interface that an object implements to declare its ability to accept specific data types for pasting and for drag-and-drop activities.
- [UIPasteConfigurationSupporting](../uipasteconfigurationsupporting.md) — The interface that determines whether a responder object supports paste configuration.
