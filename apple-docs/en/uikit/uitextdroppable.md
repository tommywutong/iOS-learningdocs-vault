---
title: UITextDroppable
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdroppable
source_url: 'https://developer.apple.com/documentation/uikit/uitextdroppable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdroppable.json'
content_hash: 'sha256:fd797a396748bd5a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextDroppable

<sub>Protocol</sub>

The interface that determines if a text view is a drop destination.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UITextDroppable : UITextInput, UITextPasteConfigurationSupporting
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIKeyInput](uikeyinput.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UITextInput](uitextinput.md), [UITextInputTraits](uitextinputtraits.md), [UITextPasteConfigurationSupporting](uitextpasteconfigurationsupporting.md)

- **Conforming Types**: [UISearchTextField](uisearchtextfield.md), [UITextField](uitextfield.md), [UITextView](uitextview.md)

## Topics

### Checking the text drop activity status

- [textDropActive](uitextdroppable/istextdropactive.md) — A Boolean value that indicates whether the text view has at least one active drop session.

### Managing the text drop interaction

- [textDropInteraction](uitextdroppable/textdropinteraction.md) — The drop interaction object added by UIKit to the text view.

### Setting the text drop delegate

- [textDropDelegate](uitextdroppable/textdropdelegate.md) — The text drop delegate for interacting with a drop activity in the text view.

## See Also

### Text view additions

- [UITextDragDelegate](uitextdragdelegate.md) — The interface for customizing the behavior of a drag activity for a text view.
- [UITextDropDelegate](uitextdropdelegate.md) — The interface for configuring a text view’s drop behavior.
- [UITextDraggable](uitextdraggable.md) — The interface that determines if a text view is a drag source.
- [UITextDragOptions](uitextdragoptions.md) — A set of options that determine the behavior of a draggable text view.
- [UITextDropEditability](uitextdropeditability.md) — The text-drop editability styles for noneditable text views.
