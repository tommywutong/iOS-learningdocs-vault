---
title: UIMainMenuSystem.Configuration
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimainmenusystem/configuration
source_url: 'https://developer.apple.com/documentation/uikit/uimainmenusystem/configuration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimainmenusystem/configuration.json'
content_hash: 'sha256:61e09b011d11f970'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMainMenuSystem](../uimainmenusystem.md)

# UIMainMenuSystem.Configuration

<sub>Class</sub>

A configuration for the main menu system. You can specify whether or not certain elements are present in the initial main menu, as well as a block to build the menu using a UIMenuBuilder.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class Configuration
```

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSCopying](../../foundation/nscopying.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [Sendable](../../swift/sendable.md)

## Topics

### Instance Properties

- [documentPreference](configuration/documentpreference.md) — Specifies a preference for document elements in the main menu.
- [findingConfiguration](configuration/findingconfiguration.md) — Configuration for the find elements should they be present in the main menu.
- [findingPreference](configuration/findingpreference.md) — Specifies a preference for finding elements in the main menu.
- [inspectorPreference](configuration/inspectorpreference.md) — Specifies a preference for inspector elements in the main menu.
- [newScenePreference](configuration/newscenepreference.md) — Specifies a preference for new scene elements in the main menu.
- [printingPreference](configuration/printingpreference.md) — Specifies a preference for printing elements in the main menu.
- [sidebarPreference](configuration/sidebarpreference.md) — Specifies a preference for sidebar elements in the main menu.
- [textFormattingPreference](configuration/textformattingpreference.md) — Specifies a preference for text formatting elements in the main menu.
- [toolbarPreference](configuration/toolbarpreference.md) — Specifies a preference for toolbar elements in the main menu.

## See Also

### Configuring a main menu system

- [setBuildConfiguration(_:buildHandler:)](<setbuildconfiguration(__buildhandler_).md>)
