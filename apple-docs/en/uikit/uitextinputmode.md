---
title: UITextInputMode
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputmode
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputmode.json'
content_hash: 'sha256:dcea8fdd3a045d48'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextInputMode

<sub>Class</sub>

The current text input mode.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UITextInputMode
```

## Overview

You can use this object to determine the primary language currently being used for text input.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md)

## Topics

### Getting the current and active text-input modes

- [activeInputModes](uitextinputmode/activeinputmodes.md) — The active text-input modes.

### Getting the primary language

- [primaryLanguage](uitextinputmode/primarylanguage.md) — The primary language, if any, of the input mode.

### Notifications

- [UITextInputCurrentInputModeDidChangeNotification](uitextinputmode/currentinputmodedidchangenotification.md) — A notification that posts when the current input mode changes.

### Structures

- [CurrentInputModeDidChangeMessage](uitextinputmode/currentinputmodedidchangemessage.md)

### Initializers

- [init(coder:)](<uitextinputmode/init(coder_).md>)

## See Also

### Text input

- [UITextInput](uitextinput.md) — A set of methods for interacting with the text input system and enabling features in documents.
- [UITextInputDelegate](uitextinputdelegate.md) — An intermediary between a document and the text input system.
- [UIKeyInput](uikeyinput.md) — A set of methods a responder uses to implement simple text entry.
- [UITextInputTraits](uitextinputtraits.md) — A set of methods that defines features for keyboard input to a text object.
- [UITextInputContext](uitextinputcontext.md) — An object that reports the type of input your app receives.
- [UITextInputAssistantItem](uitextinputassistantitem.md) — An object that manages custom bar button items that you add to the shortcuts bar above the keyboard on iPad.
- [UIDictationPhrase](uidictationphrase.md) — An object that represents the textual interpretation of a spoken phrase that the user dictates.
