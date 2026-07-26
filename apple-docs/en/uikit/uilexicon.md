---
title: UILexicon
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilexicon
source_url: 'https://developer.apple.com/documentation/uikit/uilexicon'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilexicon.json'
content_hash: 'sha256:749ef629eca14ddc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UILexicon

<sub>Class</sub>

A read-only array of term pairs, each in a lexicon entry object, for a custom keyboard.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UILexicon
```

## Overview

To obtain the lexicon, call the [- requestSupplementaryLexiconWithCompletion:](<uiinputviewcontroller/requestsupplementarylexicon(completion_).md>) method of the [UIInputViewController](uiinputviewcontroller.md) class. This method can be called only from a custom keyboard app extension. A lexicon contains words from various sources, including:

- Unpaired first names and last names from the user’s Address Book database
- Text shortcuts defined in the Settings \> General \> Keyboard \> Shortcuts list
- A common words dictionary

Apple intends for you to consider the words in a lexicon object as supplementary to an autocorrection/suggestion lexicon of your own design. For information on custom keyboards, see [Custom Keyboard](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/CustomKeyboard.html#//apple_ref/doc/uid/TP40014214-CH16) in [App Extension Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Accessing the lexicon

- [entries](uilexicon/entries.md) — A read-only array of term pairs for use by a custom keyboard.

## See Also

### Custom keyboard

- [UITextDocumentProxy](uitextdocumentproxy.md) — An object that provides textual context to a custom keyboard.
- [UIInputViewAudioFeedback](uiinputviewaudiofeedback.md) — A property that enables a custom input or keyboard accessory view to play standard keyboard input clicks.
- [UIInputViewController](uiinputviewcontroller.md) — The primary view controller for a custom keyboard app extension.
- [UILexiconEntry](uilexiconentry.md) — A read-only term pair, available within a lexicon object, for a custom keyboard.
