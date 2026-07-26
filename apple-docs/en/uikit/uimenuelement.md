---
title: UIMenuElement
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimenuelement
source_url: 'https://developer.apple.com/documentation/uikit/uimenuelement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenuelement.json'
content_hash: 'sha256:c494731f96ee8c4e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIMenuElement

<sub>Class</sub>

An object representing a menu, action, or command.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIMenuElement
```

## Overview

[UIMenuElement](uimenuelement.md) defines the behavior shared by all menus, actions, and commands. You don’t create [UIMenuElement](uimenuelement.md) objects directly. Instead, you create an appropriate object that inherits from this class, such as [UIMenu](uimenu.md), [UIAction](uiaction.md), or [UICommand](uicommand.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UIAction](uiaction.md), [UICommand](uicommand.md), [UIDeferredMenuElement](uideferredmenuelement.md), [UIMenu](uimenu.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md)

## Topics

### Getting the element attributes

- [title](uimenuelement/title.md) — The title of the menu element.
- [subtitle](uimenuelement/subtitle.md) — The subtitle to display alongside the menu element’s title.
- [image](uimenuelement/image.md) — The image to display alongside the menu element’s title.

### Creating a menu element

- [- initWithCoder:](<uimenuelement/init(coder_).md>) — Creates a menu element from data in an unarchiver.

### Constants

- [Attributes](uimenuelement/attributes.md) — Attributes that determine the style of the menu element.
- [State](uimenuelement/state.md) — Constants that indicate the state of an action- or command-based menu element.
- [RepeatBehavior](uimenuelement/repeatbehavior.md) — Possible repeat behaviors for a menu element.

### Instance Properties

- [highlightStateUpdateHandler](uimenuelement/highlightstateupdatehandler.md) — A closure the system calls when the element’s highlight state changes in a menu. _(beta)_
- [preferredImageVisibility](uimenuelement/preferredimagevisibility.md) — The preferred visibility of the element’s image. _(beta)_

### Enumerations

- [ImageVisibility](uimenuelement/imagevisibility.md) — Visibility options for a menu element’s image. _(beta)_

## See Also

### Menu elements and keyboard shortcuts

- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [Adopting menus and UIActions in your user interface](adopting-menus-and-uiactions-in-your-user-interface.md) — Add menus to your user interface, with built-in button support and bar-button items, and create custom menu experiences.
- [UIAction](uiaction.md) — A menu element that performs its action in a closure.
- [UICommand](uicommand.md) — A menu element that performs its action in a selector.
- [UIKeyCommand](uikeycommand.md) — An object that specifies a key press perform on a hardware keyboard and the resulting action.
- [UIDeferredMenuElement](uideferredmenuelement.md) — A placeholder menu element that the system replaces with the result of the block’s completion handler.
- [Provider](uideferredmenuelement/provider.md)
- [Attributes](uimenuelement/attributes.md) — Attributes that determine the style of the menu element.
- [State](uimenuelement/state.md) — Constants that indicate the state of an action- or command-based menu element.
- [UIMenuLeaf](uimenuleaf.md) — An interface for an object that represents a menu element without child elements.
