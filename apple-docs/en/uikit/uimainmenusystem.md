---
title: UIMainMenuSystem
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimainmenusystem
source_url: 'https://developer.apple.com/documentation/uikit/uimainmenusystem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimainmenusystem.json'
content_hash: 'sha256:e49c7a7edd4a9ce6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIMainMenuSystem

<sub>Class</sub>

The main menu system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIMainMenuSystem
```

## Relationships

- **Inherits From**: [UIMenuSystem](uimenusystem.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the main menu system

- [sharedSystem](uimainmenusystem/shared.md) — The shared main menu system.

### Configuring a main menu system

- [setBuildConfiguration(_:buildHandler:)](<uimainmenusystem/setbuildconfiguration(__buildhandler_).md>)
- [Configuration](uimainmenusystem/configuration.md) — A configuration for the main menu system. You can specify whether or not certain elements are present in the initial main menu, as well as a block to build the menu using a UIMenuBuilder.

### Inspecting a configuration of find elements

- [FindElementGroupConfiguration](uimenusystem/findelementgroupconfiguration.md) — Represents a configuration for find elements, should they be present. You don’t create one of these directly. A configuration is provided as part of a `UIMainMenuSystemConfiguration`.
- [Style](uimenusystem/findelementgroupconfiguration/style-swift.enum.md) — Represents a preference for the structure of Find elements in the main menu.

## See Also

### App menus

- [UIMenu](uimenu.md) — A container for grouping related menu elements in an app menu or contextual menu.
- [UIMenuBuilder](uimenubuilder.md) — An interface for adding and removing menus from a menu system.
- [UIMenuSystem](uimenusystem.md) — An object representing a main or contextual menu system.
