---
title: Expression
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/expression
source_url: 'https://developer.apple.com/documentation/foundation/expression'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/expression.json'
content_hash: 'sha256:f8969143821a6810'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Expression

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Expression<each Input, Output>
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Decodable](../swift/decodable.md), [DecodableWithConfiguration](decodablewithconfiguration.md), [Encodable](../swift/encodable.md), [EncodableWithConfiguration](encodablewithconfiguration.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(_:)](<expression/init(__).md>)

### Instance Properties

- [expression](expression/expression.md)
- [variable](expression/variable.md)

### Instance Methods

- [evaluate(_:)](<expression/evaluate(__).md>)

## See Also

### Structures

- [AsyncCharacterSequence](asynccharactersequence.md) — An asynchronous sequence of characters.
- [AsyncLineSequence](asynclinesequence.md) — An asynchronous sequence of lines of text.
- [AsyncUnicodeScalarSequence](asyncunicodescalarsequence.md) — An asychronous sequence of Unicode scalar values.
- [NSAttributedStringFormattingContextKey](nsattributedstringformattingcontextkey.md) — A type that represents a key in the formatting context dictionary.
- [NSKeyValueChangeKey](nskeyvaluechangekey.md) — The keys that can appear in the change dictionary.
- [NSKeyValueObservedChange](nskeyvalueobservedchange.md)
- [NSKeyValueOperator](nskeyvalueoperator.md) — These constants define the available array operators. See [Using Collection Operators](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/CollectionOperators.html) for more information.
- [PresentationIntent](presentationintent.md) — A type that defines presentation intent for blocks of characters like paragraphs, lists, block quotes, and tables.
