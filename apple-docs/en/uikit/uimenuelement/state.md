---
title: UIMenuElement.State
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimenuelement/state
source_url: 'https://developer.apple.com/documentation/uikit/uimenuelement/state'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenuelement/state.json'
content_hash: 'sha256:21e10ad818fe0217'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuElement](../uimenuelement.md)

# UIMenuElement.State

<sub>Enumeration</sub>

Constants that indicate the state of an action- or command-based menu element.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum State
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### States

- [UIMenuElementStateOff](state/off.md) — A constant indicating the menu element is in the “off” state.
- [UIMenuElementStateOn](state/on.md) — A constant indicating the menu element is in the “on” state.
- [UIMenuElementStateMixed](state/mixed.md) — A constant indicating the menu element is in the “mixed” state.

### Initializers

- [init(rawValue:)](<state/init(rawvalue_).md>)

## See Also

### Menu elements and keyboard shortcuts

- [Adding menus and shortcuts to the menu bar and user interface](../adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [Adopting menus and UIActions in your user interface](../adopting-menus-and-uiactions-in-your-user-interface.md) — Add menus to your user interface, with built-in button support and bar-button items, and create custom menu experiences.
- [UIMenuElement](../uimenuelement.md) — An object representing a menu, action, or command.
- [UIAction](../uiaction.md) — A menu element that performs its action in a closure.
- [UICommand](../uicommand.md) — A menu element that performs its action in a selector.
- [UIKeyCommand](../uikeycommand.md) — An object that specifies a key press perform on a hardware keyboard and the resulting action.
- [UIDeferredMenuElement](../uideferredmenuelement.md) — A placeholder menu element that the system replaces with the result of the block’s completion handler.
- [Provider](../uideferredmenuelement/provider.md)
- [Attributes](attributes.md) — Attributes that determine the style of the menu element.
- [UIMenuLeaf](../uimenuleaf.md) — An interface for an object that represents a menu element without child elements.
