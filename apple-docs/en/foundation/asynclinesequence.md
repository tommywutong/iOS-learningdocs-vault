---
title: AsyncLineSequence
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/asynclinesequence
source_url: 'https://developer.apple.com/documentation/foundation/asynclinesequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/asynclinesequence.json'
content_hash: 'sha256:5f43802ff26338ec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# AsyncLineSequence

<sub>Structure</sub>

An asynchronous sequence of lines of text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AsyncLineSequence<Base> where Base : AsyncSequence, Base.Element == UInt8
```

## Relationships

- **Conforms To**: [AsyncSequence](../swift/asyncsequence.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Aliases

- [Element](asynclinesequence/element.md) — The type of elements produced by this asynchronous sequence.

## See Also

### Structures

- [AsyncCharacterSequence](asynccharactersequence.md) — An asynchronous sequence of characters.
- [AsyncUnicodeScalarSequence](asyncunicodescalarsequence.md) — An asychronous sequence of Unicode scalar values.
- [Expression](expression.md)
- [NSAttributedStringFormattingContextKey](nsattributedstringformattingcontextkey.md) — A type that represents a key in the formatting context dictionary.
- [NSKeyValueChangeKey](nskeyvaluechangekey.md) — The keys that can appear in the change dictionary.
- [NSKeyValueObservedChange](nskeyvalueobservedchange.md)
- [NSKeyValueOperator](nskeyvalueoperator.md) — These constants define the available array operators. See [Using Collection Operators](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/CollectionOperators.html) for more information.
- [PresentationIntent](presentationintent.md) — A type that defines presentation intent for blocks of characters like paragraphs, lists, block quotes, and tables.
