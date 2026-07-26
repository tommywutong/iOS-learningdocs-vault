---
title: UIDictationPhrase
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.1+, iPadOS 5.1+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidictationphrase
source_url: 'https://developer.apple.com/documentation/uikit/uidictationphrase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidictationphrase.json'
content_hash: 'sha256:e206e7eb94cdd6e9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDictationPhrase

<sub>Class</sub>

An object that represents the textual interpretation of a spoken phrase that the user dictates.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIDictationPhrase
```

## Overview

When the user chooses dictation input on a supported device, the system automatically inserts recognized phrases into the current text view. You can use an object of the [UIDictationPhrase](uidictationphrase.md) class to obtain a string representing a phrase a user has dictated. In the case of ambiguous dictation results, a dictation phrase object provides an array containing alternative strings. Methods in the [UITextInput](uitextinput.md) protocol allow your app to respond to the completion of dictation.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Obtaining textual interpretations of spoken text

- [alternativeInterpretations](uidictationphrase/alternativeinterpretations.md) — An array of alternative textual interpretations of a dictated phrase.
- [text](uidictationphrase/text.md) — The most likely textual interpretation of a dictated phrase.

## See Also

### Text input

- [UITextInput](uitextinput.md) — A set of methods for interacting with the text input system and enabling features in documents.
- [UITextInputDelegate](uitextinputdelegate.md) — An intermediary between a document and the text input system.
- [UIKeyInput](uikeyinput.md) — A set of methods a responder uses to implement simple text entry.
- [UITextInputTraits](uitextinputtraits.md) — A set of methods that defines features for keyboard input to a text object.
- [UITextInputContext](uitextinputcontext.md) — An object that reports the type of input your app receives.
- [UITextInputMode](uitextinputmode.md) — The current text input mode.
- [UITextInputAssistantItem](uitextinputassistantitem.md) — An object that manages custom bar button items that you add to the shortcuts bar above the keyboard on iPad.
