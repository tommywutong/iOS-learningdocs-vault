---
title: UIKeyCommand
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikeycommand
source_url: 'https://developer.apple.com/documentation/uikit/uikeycommand'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeycommand.json'
content_hash: 'sha256:afa5f47eccd1bb4f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIKeyCommand

<sub>Class</sub>

An object that specifies a key press perform on a hardware keyboard and the resulting action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIKeyCommand
```

## Overview

Hardware keyboards allow a user to hold down the Control, Option, Command, or other modifier key and press another key in combination to initiate commands such as Cut, Copy, or Paste. You can use instances of this class to define custom command sequences that your app recognizes and then provide an appropriate response.

To use this class, you create instances and associate them with your app’s responder objects. Each responder has a [keyCommands](uiresponder/keycommands.md) property that you can redefine and use to return the key command objects that responder supports. Key command sequences are generated only for devices with an attached hardware keyboard.

The system always has the first opportunity to handle key commands. Key commands that map to known system events (such as Cut, Copy, and Paste) are automatically routed to the appropriate responder methods. For other key commands, the system looks for an object in the responder chain with a key command object that matches the pressed keys. If it finds such an object, it then searches the responder chain, looking for the first object that implements the corresponding action method, and calls the first one it finds.

iPad apps that run in macOS can use [UIKeyCommand](uikeycommand.md) to create menu elements that have keyboard shortcuts.

## Relationships

- **Inherits From**: [UICommand](uicommand.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIMenuLeaf](uimenuleaf.md)

## Topics

### Creating a key command object

- [init(title:image:action:input:modifierFlags:propertyList:alternates:discoverabilityTitle:attributes:state:)](<uikeycommand/init(title_image_action_input_modifierflags_propertylist_alternates_discoverabilitytitle_attributes_state_).md>) — Creates a key command that you can use as a menu element with a shortcut key, or a shortcut key only for a view controller.
- [+ keyCommandWithInput:modifierFlags:action:](<uikeycommand/init(input_modifierflags_action_).md>) — Creates a key command that matches the specified input.
- [- initWithCoder:](<uikeycommand/init(coder_).md>) — Creates a key command from data in an unarchiver.
- [- init](<uikeycommand/init().md>) — Creates a key command.
- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [Navigating an app’s user interface using a keyboard](navigating-an-app-s-user-interface-using-a-keyboard.md) — Navigate between user interface elements using a keyboard and focusable UI elements in iPad apps and apps built with Mac Catalyst.

### Getting information about the key command

- [title](uikeycommand/title.md) — The key command’s title.
- [image](uikeycommand/image.md) — The key command’s image.
- [input](uikeycommand/input.md) — The string of characters corresponding to the keys that must be pressed to match this key command.
- [action](uikeycommand/action.md) — The command’s action-method selector.
- [modifierFlags](uikeycommand/modifierflags.md) — The bit mask of modifier flags that must be pressed to match this key command.
- [UIKeyModifierFlags](uikeymodifierflags.md) — Constants that indicate which modifier keys are pressed.
- [discoverabilityTitle](uikeycommand/discoverabilitytitle.md) — An elaborated title that explains the purpose of the key command.
- [attributes](uikeycommand/attributes.md) — The attributes indicating the style of the key command.
- [state](uikeycommand/state.md) — The state of the key command.

### Getting command alternatives

- [alternates](uikeycommand/alternates.md) — An array of alternative actions to take for the key command.
- [UICommandAlternate](uicommandalternate.md) — An object representing an alternative action for a command.

### Localizing keyboard shortcuts

- [allowsAutomaticLocalization](uikeycommand/allowsautomaticlocalization.md) — A Boolean value that determines whether the system automatically remaps keyboard shortcuts based on the keyboard layout.
- [allowsAutomaticMirroring](uikeycommand/allowsautomaticmirroring.md) — A Boolean value that determines whether the system automatically swaps input strings for some keyboard shortcuts when the interface direction changes.

### Overriding the key event delivery behavior

- [wantsPriorityOverSystemBehavior](uikeycommand/wantspriorityoversystembehavior.md) — A Boolean value that indicates whether the key command takes precedence over text input or focus movements.

### Associating data

- [propertyList](uikeycommand/propertylist.md) — An object that contains data to associate with the key command.
- [UICommandTagShare](uicommandtagshare.md) — A value that identifies a command as a Share menu.

### Converting strings to key commands

- [Input strings for special keys](input-strings-for-special-keys.md) — Constants that represent the text input strings that correspond to special nonvisible keys.

### Deprecated

- [+ keyCommandWithInput:modifierFlags:action:discoverabilityTitle:](<uikeycommand/init(input_modifierflags_action_discoverabilitytitle_).md>) — Creates a key command object that matches the specified input and has a title. _(deprecated)_

### Initializers

- [init(title:subtitle:image:selectedImage:preferredImageVisibility:action:input:modifierFlags:propertyList:alternates:discoverabilityTitle:attributes:state:)](<uikeycommand/init(title_subtitle_image_selectedimage_preferredimagevisibility_action_input_modifierflags_propertylist_alternates_discoverabilitytitle_attributes_state_).md>)

## See Also

### Menu elements and keyboard shortcuts

- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [Adopting menus and UIActions in your user interface](adopting-menus-and-uiactions-in-your-user-interface.md) — Add menus to your user interface, with built-in button support and bar-button items, and create custom menu experiences.
- [UIMenuElement](uimenuelement.md) — An object representing a menu, action, or command.
- [UIAction](uiaction.md) — A menu element that performs its action in a closure.
- [UICommand](uicommand.md) — A menu element that performs its action in a selector.
- [UIDeferredMenuElement](uideferredmenuelement.md) — A placeholder menu element that the system replaces with the result of the block’s completion handler.
- [Provider](uideferredmenuelement/provider.md)
- [Attributes](uimenuelement/attributes.md) — Attributes that determine the style of the menu element.
- [State](uimenuelement/state.md) — Constants that indicate the state of an action- or command-based menu element.
- [UIMenuLeaf](uimenuleaf.md) — An interface for an object that represents a menu element without child elements.
