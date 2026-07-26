---
title: UIEditMenuConfiguration
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uieditmenuconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uieditmenuconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieditmenuconfiguration.json'
content_hash: 'sha256:a961958dc8652831'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIEditMenuConfiguration

<sub>Class</sub>

An object containing the configuration details for the menu your app presents in response to an edit menu interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIEditMenuConfiguration
```

## Overview

You use this object when calling the [- presentEditMenuWithConfiguration:](<uieditmenuinteraction/presenteditmenu(with_).md>) method of [UIEditMenuInteraction](uieditmenuinteraction.md) to provide the configuration details the interaction’s delegate uses to construct the menu that the interaction displays.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating an edit menu configuration

- [init(identifier:sourcePoint:)](<uieditmenuconfiguration/init(identifier_sourcepoint_).md>) — Initializes a new configuration with the source location you specify.

### Getting the configuration identifier

- [identifier](uieditmenuconfiguration/identifier-cjqj.md) — The unique identifier for this configuration object.

### Configuring the menu

- [preferredArrowDirection](uieditmenuconfiguration/preferredarrowdirection.md) — The preferred direction the arrow of the edit menu is pointing.
- [UIEditMenuArrowDirection](uieditmenuarrowdirection.md) — Constants that describe the direction the arrow of the edit menu is pointing.
- [sourcePoint](uieditmenuconfiguration/sourcepoint.md) — The source location of the interaction.

## See Also

### Edit menus

- [UIEditMenuInteraction](uieditmenuinteraction.md) — An interaction that provides edit operations using a menu.
- [UIEditMenuInteractionDelegate](uieditmenuinteractiondelegate.md) — The methods for customizing the menu the interaction displays.
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md) — A set of standard methods that apps can adopt to support editing.
