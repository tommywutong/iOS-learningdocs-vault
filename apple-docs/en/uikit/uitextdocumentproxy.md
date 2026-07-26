---
title: UITextDocumentProxy
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdocumentproxy
source_url: 'https://developer.apple.com/documentation/uikit/uitextdocumentproxy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdocumentproxy.json'
content_hash: 'sha256:799f7f66492d66e2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextDocumentProxy

<sub>Protocol</sub>

An object that provides textual context to a custom keyboard.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UITextDocumentProxy : UIKeyInput
```

## Overview

Through conformance to the [UIKeyInput](uikeyinput.md) protocol, a text document proxy enables a custom keyboard (which is based on the [UIInputViewController](uiinputviewcontroller.md) class) to insert and delete text, to adjust the position of the insertion point, and to determine whether a text input object is empty. The text document proxy uses the keyboard’s [textDocumentProxy](uiinputviewcontroller/textdocumentproxy.md) property to do this.

For more about using a text document proxy, see [UIInputViewController](uiinputviewcontroller.md) and [Creating a custom keyboard](creating-a-custom-keyboard.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIKeyInput](uikeyinput.md), [UITextInputTraits](uitextinputtraits.md)

## Topics

### Getting the text-input mode

- [documentInputMode](uitextdocumentproxy/documentinputmode.md) — The text-input mode for the keyboard.

### Obtaining textual context around the insertion point

- [documentContextAfterInput](uitextdocumentproxy/documentcontextafterinput.md) — Textual context after the insertion point in the current text input object.
- [documentContextBeforeInput](uitextdocumentproxy/documentcontextbeforeinput.md) — Textual context before the insertion point in the current text input object.

### Adjusting the insertion point position

- [- adjustTextPositionByCharacterOffset:](<uitextdocumentproxy/adjusttextposition(bycharacteroffset_).md>) — Moves the insertion point forward or backward in the current text input object.

### Getting the selected text

- [selectedText](uitextdocumentproxy/selectedtext.md) — The currently selected text in the document.

### Managing marked text

- [- setMarkedText:selectedRange:](<uitextdocumentproxy/setmarkedtext(__selectedrange_).md>) — Inserts the provided text and marks it to indicate that it’s part of an active input session.
- [- unmarkText](<uitextdocumentproxy/unmarktext().md>) — Unmarks the currently marked text.

### Distinguishing changes in the document

- [documentIdentifier](uitextdocumentproxy/documentidentifier.md) — The unique identifier for the document.

## See Also

### Custom keyboard

- [UIInputViewAudioFeedback](uiinputviewaudiofeedback.md) — A property that enables a custom input or keyboard accessory view to play standard keyboard input clicks.
- [UIInputViewController](uiinputviewcontroller.md) — The primary view controller for a custom keyboard app extension.
- [UILexicon](uilexicon.md) — A read-only array of term pairs, each in a lexicon entry object, for a custom keyboard.
- [UILexiconEntry](uilexiconentry.md) — A read-only term pair, available within a lexicon object, for a custom keyboard.
