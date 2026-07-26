---
title: UITextInputDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputdelegate.json'
content_hash: 'sha256:a12c068c9bbbba85'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextInputDelegate

<sub>Protocol</sub>

An intermediary between a document and the text input system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UITextInputDelegate : NSObjectProtocol
```

## Overview

A [UITextInputDelegate](uitextinputdelegate.md) conveys notifications of pending or transpired changes in text and selection in the document. UIKit provides a private text input delegate, which it assigns at runtime to the [inputDelegate](uitextinput/inputdelegate.md) property of the object whose class adopts the [UITextInput](uitextinput.md) protocol.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UIInputViewController](uiinputviewcontroller.md)

## Topics

### Notifying the delegate of textual changes

- [- textWillChange:](<uitextinputdelegate/textwillchange(__).md>) — Tells the input delegate when text is about to change in the document.
- [- textDidChange:](<uitextinputdelegate/textdidchange(__).md>) — Tells the input delegate when text has changed in the document.

### Notifying the delegate of selection changes

- [- selectionWillChange:](<uitextinputdelegate/selectionwillchange(__).md>) — Tells the input delegate when the selection is about to change in the document.
- [- selectionDidChange:](<uitextinputdelegate/selectiondidchange(__).md>) — Tells the input delegate when the selection has changed in the document.

### Notifying the delegate of conversation changes

- [- conversationContext:didChange:](<uitextinputdelegate/conversationcontext(__didchange_).md>) — Tells the input delegate when text has changed in the input object for a conversation.

## See Also

### Text input

- [UITextInput](uitextinput.md) — A set of methods for interacting with the text input system and enabling features in documents.
- [UIKeyInput](uikeyinput.md) — A set of methods a responder uses to implement simple text entry.
- [UITextInputTraits](uitextinputtraits.md) — A set of methods that defines features for keyboard input to a text object.
- [UITextInputContext](uitextinputcontext.md) — An object that reports the type of input your app receives.
- [UITextInputMode](uitextinputmode.md) — The current text input mode.
- [UITextInputAssistantItem](uitextinputassistantitem.md) — An object that manages custom bar button items that you add to the shortcuts bar above the keyboard on iPad.
- [UIDictationPhrase](uidictationphrase.md) — An object that represents the textual interpretation of a spoken phrase that the user dictates.
