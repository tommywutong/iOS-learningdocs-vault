---
title: AVLegibleMediaOptionsMenuController
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, visionOS 26.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avlegiblemediaoptionsmenucontroller
source_url: 'https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avlegiblemediaoptionsmenucontroller.json'
content_hash: 'sha256:8bc4450f592dd108'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVLegibleMediaOptionsMenuController

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class AVLegibleMediaOptionsMenuController
```

## Overview

A menu controller for legible media options (subtitles/captions)

Supports both media track selection and caption appearance customization. When initialized without a player, only caption appearance options are available. When initialized with a player, both media tracks and caption appearance are available.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a menu controller

- [- initWithPlayer:](<avlegiblemediaoptionsmenucontroller/init(player_).md>)

### Managing the menu

- [- menuWithContents:](<avlegiblemediaoptionsmenucontroller/menu(contents_).md>)
- [menuState](avlegiblemediaoptionsmenucontroller/menustate.md)
- [MenuContents](avlegiblemediaoptionsmenucontroller/menucontents.md)
- [AVLegibleMediaOptionsMenuState](avlegiblemediaoptionsmenustate.md)
- [StateChangeReason](avlegiblemediaoptionsmenucontroller/statechangereason.md)

### Accessing the player

- [player](avlegiblemediaoptionsmenucontroller/player.md)

### Configuring a delegate

- [delegate](avlegiblemediaoptionsmenucontroller/delegate-swift.property.md)
- [Delegate](avlegiblemediaoptionsmenucontroller/delegate-swift.protocol.md)

## See Also

### Legible media options

- [AVLegibleMediaOptionsMenuState](avlegiblemediaoptionsmenustate.md)
