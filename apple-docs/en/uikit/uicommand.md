---
title: UICommand
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicommand
source_url: 'https://developer.apple.com/documentation/uikit/uicommand'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicommand.json'
content_hash: 'sha256:48f3a81ccc95125e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICommand

<sub>Class</sub>

A menu element that performs its action in a selector.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UICommand
```

## Overview

Create a [UICommand](uicommand.md) object when you want a menu element that performs its action in a selector available in the responder chain.

```swift
// Create a selector-based action to use as a menu element.
let refreshCommand = UICommand(title: "Refresh", action: #selector(refreshData(_:)))

// Use the .displayInline option to avoid displaying the menu as a submenu,
// and to separate it from the other menu elements using a line separator.
let refreshMenuItem = UIMenu(title: "", options: .displayInline, children: [refreshCommand])

// Insert the menu into the File menu before the Close menu.
builder.insertSibling(refreshMenuItem, beforeMenu: .close)
```

## Relationships

- **Inherits From**: [UIMenuElement](uimenuelement.md)

- **Inherited By**: [UIKeyCommand](uikeycommand.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIMenuLeaf](uimenuleaf.md)

## Topics

### Creating a command

- [init(title:subtitle:image:action:propertyList:alternates:discoverabilityTitle:attributes:state:)](<uicommand/init(title_subtitle_image_action_propertylist_alternates_discoverabilitytitle_attributes_state_).md>) — Creates a command with the specified title, subtitle, image, action, property list, alternative commands, discoverability title, attributes, and state.
- [init(title:image:action:propertyList:alternates:discoverabilityTitle:attributes:state:)](<uicommand/init(title_image_action_propertylist_alternates_discoverabilitytitle_attributes_state_).md>) — Creates a command with the specified title, image, action, property list, alternative commands, discoverability title, attributes, and state.
- [- initWithCoder:](<uicommand/init(coder_).md>) — Creates a command from data in an unarchiver.
- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.

### Getting information about the command

- [title](uicommand/title.md) — The command’s title.
- [image](uicommand/image.md) — The command’s image.
- [action](uicommand/action.md) — The selector identifying the action method called after the user selects the command.
- [discoverabilityTitle](uicommand/discoverabilitytitle.md) — An elaborated title that explains the purpose of the command.
- [attributes](uicommand/attributes.md) — The attributes indicating the style of the command.
- [state](uicommand/state.md) — The state of the command.

### Getting command alternatives

- [alternates](uicommand/alternates.md) — An array of alternative actions to take for the command.
- [UICommandAlternate](uicommandalternate.md) — An object representing an alternative action for a command.

### Associating data

- [propertyList](uicommand/propertylist.md) — An object that contains data to associate with the command.
- [UICommandTagShare](uicommandtagshare.md) — A value that identifies a command as a Share menu.

### Initializers

- [init(title:subtitle:image:selectedImage:action:propertyList:alternates:discoverabilityTitle:attributes:state:)](<uicommand/init(title_subtitle_image_selectedimage_action_propertylist_alternates_discoverabilitytitle_attributes_state_).md>)
- [init(title:subtitle:image:selectedImage:preferredImageVisibility:action:propertyList:alternates:discoverabilityTitle:attributes:state:)](<uicommand/init(title_subtitle_image_selectedimage_preferredimagevisibility_action_propertylist_alternates_discoverabilitytitle_attributes_state_).md>)

## See Also

### Menu elements and keyboard shortcuts

- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [Adopting menus and UIActions in your user interface](adopting-menus-and-uiactions-in-your-user-interface.md) — Add menus to your user interface, with built-in button support and bar-button items, and create custom menu experiences.
- [UIMenuElement](uimenuelement.md) — An object representing a menu, action, or command.
- [UIAction](uiaction.md) — A menu element that performs its action in a closure.
- [UIKeyCommand](uikeycommand.md) — An object that specifies a key press perform on a hardware keyboard and the resulting action.
- [UIDeferredMenuElement](uideferredmenuelement.md) — A placeholder menu element that the system replaces with the result of the block’s completion handler.
- [Provider](uideferredmenuelement/provider.md)
- [Attributes](uimenuelement/attributes.md) — Attributes that determine the style of the menu element.
- [State](uimenuelement/state.md) — Constants that indicate the state of an action- or command-based menu element.
- [UIMenuLeaf](uimenuleaf.md) — An interface for an object that represents a menu element without child elements.
