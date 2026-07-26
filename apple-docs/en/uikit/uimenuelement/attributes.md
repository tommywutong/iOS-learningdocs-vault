---
title: UIMenuElement.Attributes
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimenuelement/attributes
source_url: 'https://developer.apple.com/documentation/uikit/uimenuelement/attributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenuelement/attributes.json'
content_hash: 'sha256:fa72f41a43a2b7e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuElement](../uimenuelement.md)

# UIMenuElement.Attributes

<sub>Structure</sub>

Attributes that determine the style of the menu element.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct Attributes
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Attributes

- [UIMenuElementAttributesDestructive](attributes/destructive.md) — An attribute indicating the destructive style.
- [UIMenuElementAttributesDisabled](attributes/disabled.md) — An attribute indicating the disabled style.
- [UIMenuElementAttributesHidden](attributes/hidden.md) — An attribute indicating the hidden style.
- [UIMenuElementAttributesKeepsMenuPresented](attributes/keepsmenupresented.md) — An attribute indicating that the menu remains presented after firing the element’s action instead of dismissing.

### Initializers

- [init(rawValue:)](<attributes/init(rawvalue_).md>) — Creates a menu-element attributes structure with the specified raw value.

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
- [State](state.md) — Constants that indicate the state of an action- or command-based menu element.
- [UIMenuLeaf](../uimenuleaf.md) — An interface for an object that represents a menu element without child elements.
