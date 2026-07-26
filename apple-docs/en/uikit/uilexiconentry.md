---
title: UILexiconEntry
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilexiconentry
source_url: 'https://developer.apple.com/documentation/uikit/uilexiconentry'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilexiconentry.json'
content_hash: 'sha256:6faa636d52df8fd7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UILexiconEntry

<sub>Class</sub>

A read-only term pair, available within a lexicon object, for a custom keyboard.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UILexiconEntry
```

## Overview

You can employ a lexicon entry by matching user input against the entry’s [userInput](uilexiconentry/userinput.md) value, and then inserting into the current text input object the corresponding [documentText](uilexiconentry/documenttext.md) value. For example, if the user typed the string “iphone”, the lexicon entry with that exact, case-sensitive string in the [userInput](uilexiconentry/userinput.md) property has the string “iPhone” in the corresponding [documentText](uilexiconentry/documenttext.md) property.

In some cases, the [documentText](uilexiconentry/documenttext.md) string is in a different text script than the [userInput](uilexiconentry/userinput.md) string.

For information on custom keyboards, which are based on the [UIInputViewController](uiinputviewcontroller.md) class, see [Creating a custom keyboard](creating-a-custom-keyboard.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Accessing a lexicon entry

- [documentText](uilexiconentry/documenttext.md) — Text to be inserted into a text input object by a custom keyboard, corresponding to the user input value in the same lexicon entry.
- [userInput](uilexiconentry/userinput.md) — Text to match, during user input, to provide appropriate output to a text document from the document text value in the same lexicon entry.

## See Also

### Custom keyboard

- [UITextDocumentProxy](uitextdocumentproxy.md) — An object that provides textual context to a custom keyboard.
- [UIInputViewAudioFeedback](uiinputviewaudiofeedback.md) — A property that enables a custom input or keyboard accessory view to play standard keyboard input clicks.
- [UIInputViewController](uiinputviewcontroller.md) — The primary view controller for a custom keyboard app extension.
- [UILexicon](uilexicon.md) — A read-only array of term pairs, each in a lexicon entry object, for a custom keyboard.
