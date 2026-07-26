---
title: UIInputViewAudioFeedback
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiinputviewaudiofeedback
source_url: 'https://developer.apple.com/documentation/uikit/uiinputviewaudiofeedback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinputviewaudiofeedback.json'
content_hash: 'sha256:0c1b551d70b4d5ca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIInputViewAudioFeedback

<sub>Protocol</sub>

A property that enables a custom input or keyboard accessory view to play standard keyboard input clicks.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIInputViewAudioFeedback : NSObjectProtocol
```

## Overview

Implement this protocol in your custom subclass of [UIView](uiview.md) that you associate with your custom input nib file. For more information, see [Text Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/TextAndWebiPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009542).

Implementation of this protocol is optional but expected.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Enabling input clicks

- [enableInputClicksWhenVisible](uiinputviewaudiofeedback/enableinputclickswhenvisible.md) — Specifies whether or not an input view enables input clicks.

## See Also

### Custom keyboard

- [UITextDocumentProxy](uitextdocumentproxy.md) — An object that provides textual context to a custom keyboard.
- [UIInputViewController](uiinputviewcontroller.md) — The primary view controller for a custom keyboard app extension.
- [UILexicon](uilexicon.md) — A read-only array of term pairs, each in a lexicon entry object, for a custom keyboard.
- [UILexiconEntry](uilexiconentry.md) — A read-only term pair, available within a lexicon object, for a custom keyboard.
