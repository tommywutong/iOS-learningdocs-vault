---
title: UIDeferredMenuElement
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uideferredmenuelement
source_url: 'https://developer.apple.com/documentation/uikit/uideferredmenuelement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uideferredmenuelement.json'
content_hash: 'sha256:161c4484f4b283d1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDeferredMenuElement

<sub>Class</sub>

A placeholder menu element that the system replaces with the result of the block’s completion handler.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIDeferredMenuElement
```

## Relationships

- **Inherits From**: [UIMenuElement](uimenuelement.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md)

## Topics

### Creating a deferred menu element

- [+ elementWithProvider:](<uideferredmenuelement/init(__).md>) — A convenience initializer that creates a placeholder menu element that the system replaces with the result of the provider’s completion handler.
- [+ elementWithUncachedProvider:](<uideferredmenuelement/uncached(__).md>) — Returns a placeholder menu element that the system replaces with the result of the provider’s completion handler.
- [+ elementUsingFocusWithIdentifier:shouldCacheItems:](<uideferredmenuelement/usingfocus(identifier_shouldcacheitems_).md>)

### Setting an identifier

- [identifier](uideferredmenuelement/identifier-swift.property.md) — The identifier of this deferred menu element.
- [Identifier](uideferredmenuelement/identifier-swift.struct.md)

### Initializers

- [init(provider:)](<uideferredmenuelement/init(provider_).md>)
- [init(uncachedProvider:)](<uideferredmenuelement/init(uncachedprovider_).md>)

## See Also

### Menu elements and keyboard shortcuts

- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [Adopting menus and UIActions in your user interface](adopting-menus-and-uiactions-in-your-user-interface.md) — Add menus to your user interface, with built-in button support and bar-button items, and create custom menu experiences.
- [UIMenuElement](uimenuelement.md) — An object representing a menu, action, or command.
- [UIAction](uiaction.md) — A menu element that performs its action in a closure.
- [UICommand](uicommand.md) — A menu element that performs its action in a selector.
- [UIKeyCommand](uikeycommand.md) — An object that specifies a key press perform on a hardware keyboard and the resulting action.
- [Provider](uideferredmenuelement/provider.md)
- [Attributes](uimenuelement/attributes.md) — Attributes that determine the style of the menu element.
- [State](uimenuelement/state.md) — Constants that indicate the state of an action- or command-based menu element.
- [UIMenuLeaf](uimenuleaf.md) — An interface for an object that represents a menu element without child elements.
