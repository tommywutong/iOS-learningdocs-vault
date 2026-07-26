---
title: UIMenuBuilder
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimenubuilder
source_url: 'https://developer.apple.com/documentation/uikit/uimenubuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenubuilder.json'
content_hash: 'sha256:74596cd248f4334f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIMenuBuilder

<sub>Protocol</sub>

An interface for adding and removing menus from a menu system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIMenuBuilder
```

## Overview

You don’t create a menu builder object. Instead, you override [- buildMenuWithBuilder:](<uiresponder/buildmenu(with_).md>) in your app delegate or view controller to receive a builder object. Where you override this method determines the system that the builder updates. To add and remove menus from the menu bar using the [mainSystem](uimenusystem/main.md) menu system, override [- buildMenuWithBuilder:](<uiresponder/buildmenu(with_).md>) in your app delegate. To build a context menu using the [contextSystem](uimenusystem/context.md) system, override the method in your view controller.

To see an example of how to use a menu builder object, see [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md).

## Topics

### Getting menu systems and elements

- [system](uimenubuilder/system.md) — The menu system that the menu builder modifies.
- [- menuForIdentifier:](<uimenubuilder/menu(for_).md>) — Gets the menu for the specified menu identifier.
- [- actionForIdentifier:](<uimenubuilder/action(for_).md>) — Gets the action for the specified action identifier.
- [command(for:propertyList:)](<uimenubuilder/command(for_propertylist_).md>) — Gets the command for the specified selector and property list.

### Inserting child menus

- [- insertChildMenu:atStartOfMenuForIdentifier:](<uimenubuilder/insertchild(__atstartofmenu_).md>) — Adds a child menu as the first element of the specified parent menu.
- [- insertChildMenu:atEndOfMenuForIdentifier:](<uimenubuilder/insertchild(__atendofmenu_).md>) — Adds a child menu as the last element of the specified parent menu.

### Inserting sibling menus

- [- insertSiblingMenu:beforeMenuForIdentifier:](<uimenubuilder/insertsibling(__beforemenu_).md>) — Inserts a sibling menu before the specified menu.
- [- insertSiblingMenu:afterMenuForIdentifier:](<uimenubuilder/insertsibling(__aftermenu_).md>) — Inserts a sibling menu after the specified menu.

### Replacing menus and child menu elements

- [- replaceChildrenOfMenuForIdentifier:fromChildrenBlock:](<uimenubuilder/replacechildren(ofmenu_from_).md>) — Replaces the elements in a menu with the elements returned by the specified handler block.

### Removing a menu

- [- removeMenuForIdentifier:](<uimenubuilder/remove(menu_).md>) — Removes a menu from the menu system.

### Instance Methods

- [- insertElements:afterActionForIdentifier:](<uimenubuilder/insertelements(__afteraction_).md>) — Insert elements after an identified action.
- [insertElements(_:afterCommand:propertyList:)](<uimenubuilder/insertelements(__aftercommand_propertylist_).md>)
- [- insertElements:afterMenuForIdentifier:](<uimenubuilder/insertelements(__aftermenu_).md>) — Insert elements after an identified menu.
- [- insertElements:atEndOfMenuForIdentifier:](<uimenubuilder/insertelements(__atendofmenu_).md>) — Insert elements at the end of an identified parent menu.
- [- insertElements:atStartOfMenuForIdentifier:](<uimenubuilder/insertelements(__atstartofmenu_).md>) — Insert elements at the start of an identified parent menu.
- [- insertElements:beforeActionForIdentifier:](<uimenubuilder/insertelements(__beforeaction_).md>) — Insert elements before an identified action.
- [insertElements(_:beforeCommand:propertyList:)](<uimenubuilder/insertelements(__beforecommand_propertylist_).md>)
- [- insertElements:beforeMenuForIdentifier:](<uimenubuilder/insertelements(__beforemenu_).md>) — Insert elements before an identified menu.
- [- removeActionForIdentifier:](<uimenubuilder/remove(action_).md>) — Remove an identified action.
- [remove(command:propertyList:)](<uimenubuilder/remove(command_propertylist_).md>)
- [- replaceActionForIdentifier:withElements:](<uimenubuilder/replace(action_with_).md>) — Replace an identified action with menu elements.
- [replace(command:propertyList:with:)](<uimenubuilder/replace(command_propertylist_with_).md>)
- [- replaceMenuForIdentifier:withElements:](<uimenubuilder/replace(menu_with_)-8mwou.md>) — Replace an identified menu with menu elements.
- [- replaceMenuForIdentifier:withMenu:](<uimenubuilder/replace(menu_with_)-95tg2.md>) — Replace an identified menu with a menu.

## See Also

### App menus

- [UIMenu](uimenu.md) — A container for grouping related menu elements in an app menu or contextual menu.
- [UIMenuSystem](uimenusystem.md) — An object representing a main or contextual menu system.
- [UIMainMenuSystem](uimainmenusystem.md) — The main menu system.
