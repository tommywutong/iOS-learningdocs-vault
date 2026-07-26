---
title: UIContextMenuConfiguration
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontextmenuconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenuconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenuconfiguration.json'
content_hash: 'sha256:804dcac0e526a1c4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIContextMenuConfiguration

<sub>Class</sub>

An object containing the configuration details for the contextual menu.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIContextMenuConfiguration
```

## Overview

Before displaying a contextual menu, the system asks your [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md) to provide a [UIContextMenuConfiguration](uicontextmenuconfiguration.md) object with details about that menu. In your [- contextMenuInteraction:configurationForMenuAtLocation:](<uicontextmenuinteractiondelegate/contextmenuinteraction(__configurationformenuatlocation_).md>) method, use the location parameter to determine where the interaction occurred, and use the content at that location to configure your contextual menu and view controller. Provide custom blocks to generate:

- The contextual menu with the actions for your content.
- An optional view controller to use when displaying your content.

If you specify a default object without any custom handler blocks, the system displays a default preview interface with no menu.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating the menu configuration object

- [init(identifier:previewProvider:actionProvider:)](<uicontextmenuconfiguration/init(identifier_previewprovider_actionprovider_).md>) — Creates a menu configuration object with the specified action and preview providers.
- [UIContextMenuContentPreviewProvider](uicontextmenucontentpreviewprovider.md) — Returns the custom view controller to use when previewing your content.
- [UIContextMenuActionProvider](uicontextmenuactionprovider.md) — Returns an action-based contextual menu, optionally incorporating the system-suggested actions.

### Getting the configuration identifier

- [identifier](uicontextmenuconfiguration/identifier.md) — The unique identifier for this configuration object.

### Handling multiple-item interactions

- [secondaryItemIdentifiers](uicontextmenuconfiguration/secondaryitemidentifiers.md) — A set of identifiers corresponding to each item other than the primary item in a multiple-item interaction.
- [badgeCount](uicontextmenuconfiguration/badgecount.md) — The number of items in a multiple-item interaction.

### Specifying the order of menu elements

- [preferredMenuElementOrder](uicontextmenuconfiguration/preferredmenuelementorder.md) — The preferred menu-element ordering strategy for the menu.
- [ElementOrder](uicontextmenuconfiguration/elementorder.md) — Constants that define the ordering strategy for menu elements in a context menu.

### Instance Properties

- [allowsTypeSelect](uicontextmenuconfiguration/allowstypeselect.md) — A Boolean value that indicates whether the context menu supports keystroke-based navigation. _(beta)_

## See Also

### Providing the preview configuration data

- [- contextMenuInteraction:configurationForMenuAtLocation:](<uicontextmenuinteractiondelegate/contextmenuinteraction(__configurationformenuatlocation_).md>) — Returns the configuration data to use when previewing the content.
