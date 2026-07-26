---
title: UITextInputTokenizer
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputtokenizer
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputtokenizer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputtokenizer.json'
content_hash: 'sha256:04c88f24e0460ba3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextInputTokenizer

<sub>Protocol</sub>

A tokenizer, which is an object that allows the text input system to evaluate text units of different granularities.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UITextInputTokenizer : NSObjectProtocol
```

## Overview

Granularities of text units are always evaluated with reference to a storage or reference direction.

Text-processing objects that conform to the [UITextInput](uitextinput.md) protocol must hold a reference to a tokenizer (through the [tokenizer](uitextinput/tokenizer.md) property). The [UITextInputStringTokenizer](uitextinputstringtokenizer.md) class provides a default base implementation of the [UITextInputTokenizer](uitextinputtokenizer.md) protocol. Tokenizers of this class are suitable for most western-language keyboards. Apps with different requirements may adopt the [UITextInputTokenizer](uitextinputtokenizer.md) protocol and create their own tokenizers.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UITextInputStringTokenizer](uitextinputstringtokenizer.md)

## Topics

### Determining text positions relative to unit boundaries

- [- isPosition:atBoundary:inDirection:](<uitextinputtokenizer/isposition(__atboundary_indirection_).md>) — Return whether a text position is at a boundary of a text unit of a specified granularity in a specified direction.
- [- isPosition:withinTextUnit:inDirection:](<uitextinputtokenizer/isposition(__withintextunit_indirection_).md>) — Return whether a text position is within a text unit of a specified granularity in a specified direction.

### Computing text position by unit boundaries

- [- positionFromPosition:toBoundary:inDirection:](<uitextinputtokenizer/position(from_toboundary_indirection_).md>) — Return the next text position at a boundary of a text unit of the given granularity in a given direction.

### Getting ranges of specific text units

- [- rangeEnclosingPosition:withGranularity:inDirection:](<uitextinputtokenizer/rangeenclosingposition(__with_indirection_).md>) — Return the range for the text enclosing a text position in a text unit of a given granularity in a given direction.

### Constants

- [UITextDirection](uitextdirection.md) — The direction of the text.
- [UITextGranularity](uitextgranularity.md) — The granularity of a unit of text.

## See Also

### Text tokenizer

- [UITextInputStringTokenizer](uitextinputstringtokenizer.md) — A base implementation of the text-input tokenizer protocol.
