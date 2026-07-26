---
title: UITextDraggable
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdraggable
source_url: 'https://developer.apple.com/documentation/uikit/uitextdraggable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdraggable.json'
content_hash: 'sha256:f435175d9c1f56e7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextDraggable

<sub>Protocol</sub>

The interface that determines if a text view is a drag source.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UITextDraggable : UITextInput
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIKeyInput](uikeyinput.md), [UITextInput](uitextinput.md), [UITextInputTraits](uitextinputtraits.md)

- **Conforming Types**: [UISearchTextField](uisearchtextfield.md), [UITextField](uitextfield.md), [UITextView](uitextview.md)

## Topics

### Checking the text drag activity status

- [textDragActive](uitextdraggable/istextdragactive.md) — A Boolean value indicating whether at least one drag session for the text view is active.

### Managing the text drag interaction

- [textDragInteraction](uitextdraggable/textdraginteraction.md) — The drag interaction object added by UIKit to the text view.

### Setting the text drag delegate

- [textDragDelegate](uitextdraggable/textdragdelegate.md) — A text drag delegate object for customizing the drag source behavior of a text view.

### Setting the text drag options

- [textDragOptions](uitextdraggable/textdragoptions.md) — The options for the text drag operation.

## See Also

### Text view additions

- [UITextDragDelegate](uitextdragdelegate.md) — The interface for customizing the behavior of a drag activity for a text view.
- [UITextDropDelegate](uitextdropdelegate.md) — The interface for configuring a text view’s drop behavior.
- [UITextDragOptions](uitextdragoptions.md) — A set of options that determine the behavior of a draggable text view.
- [UITextDroppable](uitextdroppable.md) — The interface that determines if a text view is a drop destination.
- [UITextDropEditability](uitextdropeditability.md) — The text-drop editability styles for noneditable text views.
