---
title: UIDeferredMenuElement.Provider
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uideferredmenuelement/provider
source_url: 'https://developer.apple.com/documentation/uikit/uideferredmenuelement/provider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uideferredmenuelement/provider.json'
content_hash: 'sha256:9f1b6c6af21af971'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDeferredMenuElement](../uideferredmenuelement.md)

# UIDeferredMenuElement.Provider

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class Provider
```

## Overview

Represents an element provider for a deferred menu element. When the containing menu for a responder-based deferred element is presented, the system asks the responder chain for one of these element providers for the deferred element.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [Sendable](../../swift/sendable.md)

## Topics

### Initializers

- [+ providerWithElementProvider:](<provider/init(__).md>)

## See Also

### Menu elements and keyboard shortcuts

- [Adding menus and shortcuts to the menu bar and user interface](../adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [Adopting menus and UIActions in your user interface](../adopting-menus-and-uiactions-in-your-user-interface.md) — Add menus to your user interface, with built-in button support and bar-button items, and create custom menu experiences.
- [UIMenuElement](../uimenuelement.md) — An object representing a menu, action, or command.
- [UIAction](../uiaction.md) — A menu element that performs its action in a closure.
- [UICommand](../uicommand.md) — A menu element that performs its action in a selector.
- [UIKeyCommand](../uikeycommand.md) — An object that specifies a key press perform on a hardware keyboard and the resulting action.
- [UIDeferredMenuElement](../uideferredmenuelement.md) — A placeholder menu element that the system replaces with the result of the block’s completion handler.
- [Attributes](../uimenuelement/attributes.md) — Attributes that determine the style of the menu element.
- [State](../uimenuelement/state.md) — Constants that indicate the state of an action- or command-based menu element.
- [UIMenuLeaf](../uimenuleaf.md) — An interface for an object that represents a menu element without child elements.
