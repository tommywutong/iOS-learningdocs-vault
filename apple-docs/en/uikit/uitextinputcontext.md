---
title: UITextInputContext
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, tvOS 16.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputcontext
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputcontext.json'
content_hash: 'sha256:98661b64f8741ef9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextInputContext

<sub>Class</sub>

An object that reports the type of input your app receives.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class UITextInputContext
```

## Overview

Use the shared [UITextInputContext](uitextinputcontext.md) object to get information about the type of input your app receives. UIKit apps can receive text input from sources other than the software keyboard, including from dictation, Apple Pencil, and a connected keyboard. Use information about the likely input sources to adjust your UI to accommodate that input. For example, you might increase the size of text fields to accommodate handwriting input from Apple Pencil.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the input context object

- [+ current](<uitextinputcontext/current().md>) — Returns the shared text-input context object.

### Getting the expected input type

- [dictationInputExpected](uitextinputcontext/isdictationinputexpected.md) — Returns a Boolean value that indicates whether someone is likely to use dictation to input text to the app.
- [hardwareKeyboardInputExpected](uitextinputcontext/ishardwarekeyboardinputexpected.md) — Returns a Boolean value that indicates whether someone is likely to enter text using a hardware keyboard.
- [pencilInputExpected](uitextinputcontext/ispencilinputexpected.md) — Returns a Boolean value that indicates whether someone is likely to use Apple Pencil for input.

## See Also

### Text input

- [UITextInput](uitextinput.md) — A set of methods for interacting with the text input system and enabling features in documents.
- [UITextInputDelegate](uitextinputdelegate.md) — An intermediary between a document and the text input system.
- [UIKeyInput](uikeyinput.md) — A set of methods a responder uses to implement simple text entry.
- [UITextInputTraits](uitextinputtraits.md) — A set of methods that defines features for keyboard input to a text object.
- [UITextInputMode](uitextinputmode.md) — The current text input mode.
- [UITextInputAssistantItem](uitextinputassistantitem.md) — An object that manages custom bar button items that you add to the shortcuts bar above the keyboard on iPad.
- [UIDictationPhrase](uidictationphrase.md) — An object that represents the textual interpretation of a spoken phrase that the user dictates.
