---
title: UIMenuSystem
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimenusystem
source_url: 'https://developer.apple.com/documentation/uikit/uimenusystem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenusystem.json'
content_hash: 'sha256:be3076d45a6d2ce6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIMenuSystem

<sub>Class</sub>

An object representing a main or contextual menu system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIMenuSystem
```

## Overview

A menu system groups root menus together. The [mainSystem](uimenusystem/main.md) system has only one root menu while the [contextSystem](uimenusystem/context.md) system can have multiple root menus, each built in different [UIResponder](uiresponder.md) objects like a view controller.

Use [UIMenuSystem](uimenusystem.md) in your implementation of [- buildMenuWithBuilder:](<uiresponder/buildmenu(with_).md>) to isolate changes to a specific system.

```swift
override func buildMenu(with builder: UIMenuBuilder) {
    super.buildMenu(with: builder)
    
    // Ensure that the builder is modifying the menu bar system.
    guard builder.system == UIMenuSystem.main else { return }

    // ...
}
```

You can also use a menu system to rebuild or revalidate menus as changes occur in your app. To rebuild a menu, call the [- setNeedsRebuild](<uimenusystem/setneedsrebuild().md>) method. Call [- setNeedsRevalidate](<uimenusystem/setneedsrevalidate().md>) when you need the menu system to revalidate a menu.

For more information, see [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UIContextMenuSystem](uicontextmenusystem.md), [UIMainMenuSystem](uimainmenusystem.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Getting a menu system

- [mainSystem](uimenusystem/main.md) — The main menu system.
- [contextSystem](uimenusystem/context.md) — The context menu system.

### Rebuilding a menu system

- [- setNeedsRebuild](<uimenusystem/setneedsrebuild().md>) — Tells the menu system to rebuild all of its menus.

### Revalidating a menu system

- [- setNeedsRevalidate](<uimenusystem/setneedsrevalidate().md>) — Tells the menu system to validate all of its menus.

### Setting group preferences

- [ElementGroupPreference](uimenusystem/elementgrouppreference.md)

## See Also

### App menus

- [UIMenu](uimenu.md) — A container for grouping related menu elements in an app menu or contextual menu.
- [UIMenuBuilder](uimenubuilder.md) — An interface for adding and removing menus from a menu system.
- [UIMainMenuSystem](uimainmenusystem.md) — The main menu system.
