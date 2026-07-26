---
title: UIKeyInput
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikeyinput
source_url: 'https://developer.apple.com/documentation/uikit/uikeyinput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeyinput.json'
content_hash: 'sha256:3520394a84db6da5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIKeyInput

<sub>Protocol</sub>

A set of methods a responder uses to implement simple text entry.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIKeyInput : UITextInputTraits
```

## Overview

Adopt this protocol in a subclass of [UIResponder](uiresponder.md) to support text entry. When instances of this subclass are the first responder, the system keyboard displays. Only a small subset of the available keyboards and languages are available to classes that adopt this protocol.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UITextInputTraits](uitextinputtraits.md)

- **Inherited By**: [UITextDocumentProxy](uitextdocumentproxy.md), [UITextDraggable](uitextdraggable.md), [UITextDroppable](uitextdroppable.md), [UITextInput](uitextinput.md)

- **Conforming Types**: [UISearchTextField](uisearchtextfield.md), [UITextField](uitextfield.md), [UITextView](uitextview.md)

## Topics

### Inserting and deleting text

- [- insertText:](<uikeyinput/inserttext(__).md>) — Inserts a character into the displayed text.
- [- deleteBackward](<uikeyinput/deletebackward().md>) — Deletes a character from the displayed text.
- [hasText](uikeyinput/hastext.md) — A Boolean value that indicates whether the text-entry object has any text.

## See Also

### Text input

- [UITextInput](uitextinput.md) — A set of methods for interacting with the text input system and enabling features in documents.
- [UITextInputDelegate](uitextinputdelegate.md) — An intermediary between a document and the text input system.
- [UITextInputTraits](uitextinputtraits.md) — A set of methods that defines features for keyboard input to a text object.
- [UITextInputContext](uitextinputcontext.md) — An object that reports the type of input your app receives.
- [UITextInputMode](uitextinputmode.md) — The current text input mode.
- [UITextInputAssistantItem](uitextinputassistantitem.md) — An object that manages custom bar button items that you add to the shortcuts bar above the keyboard on iPad.
- [UIDictationPhrase](uidictationphrase.md) — An object that represents the textual interpretation of a spoken phrase that the user dictates.
