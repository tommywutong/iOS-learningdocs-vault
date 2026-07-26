---
title: UITextInputStringTokenizer
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputstringtokenizer
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputstringtokenizer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputstringtokenizer.json'
content_hash: 'sha256:9996d656ecbb123b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextInputStringTokenizer

<sub>Class</sub>

A base implementation of the text-input tokenizer protocol.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UITextInputStringTokenizer
```

## Overview

If you want to take advantage of this base implementation of the [UITextInputTokenizer](uitextinputtokenizer.md) protocol, you should subclass this class and handle application-specific directions and granularities affected by layout. When you instantiate a class you must supply the document class that’s adopting the [UITextInput](uitextinput.md) protocol for your application.

### Subclassing notes

When you subclass [UITextInputStringTokenizer](uitextinputstringtokenizer.md), override all [UITextInputTokenizer](uitextinputtokenizer.md) methods, calling the superclass implementation (`super`) when method parameters aren’t affected by layout. For example, the subclass needs a custom implementation of all methods for line granularity. For the left direction, it needs to decide whether left corresponds at a given position to forward or backward, and then call `super` passing in the storage direction ([UITextStorageDirection](uitextstoragedirection.md)).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UITextInputTokenizer](uitextinputtokenizer.md)

## Topics

### Initializing a tokenizer

- [- initWithTextInput:](<uitextinputstringtokenizer/init(textinput_).md>) — Returns an object initialized with the document object that directly communicates with the text input system.

## See Also

### Text tokenizer

- [UITextInputTokenizer](uitextinputtokenizer.md) — A tokenizer, which is an object that allows the text input system to evaluate text units of different granularities.
