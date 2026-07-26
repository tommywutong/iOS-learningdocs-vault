---
title: PresentationIntent
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/presentationintent
source_url: 'https://developer.apple.com/documentation/foundation/presentationintent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/presentationintent.json'
content_hash: 'sha256:e44bc1301ff176f7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# PresentationIntent

<sub>Structure</sub>

A type that defines presentation intent for blocks of characters like paragraphs, lists, block quotes, and tables.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PresentationIntent
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Structures

- [IntentType](presentationintent/intenttype.md)
- [TableColumn](presentationintent/tablecolumn.md)

### Initializers

- [init(_:identity:parent:)](<presentationintent/init(__identity_parent_).md>)
- [init(types:)](<presentationintent/init(types_).md>)

### Instance Properties

- [components](presentationintent/components.md)
- [count](presentationintent/count.md)
- [indentationLevel](presentationintent/indentationlevel.md)
- [isValid](presentationintent/isvalid.md)

### Enumerations

- [Kind](presentationintent/kind.md)

## See Also

### Structures

- [AsyncCharacterSequence](asynccharactersequence.md) — An asynchronous sequence of characters.
- [AsyncLineSequence](asynclinesequence.md) — An asynchronous sequence of lines of text.
- [AsyncUnicodeScalarSequence](asyncunicodescalarsequence.md) — An asychronous sequence of Unicode scalar values.
- [Expression](expression.md)
- [NSAttributedStringFormattingContextKey](nsattributedstringformattingcontextkey.md) — A type that represents a key in the formatting context dictionary.
- [NSKeyValueChangeKey](nskeyvaluechangekey.md) — The keys that can appear in the change dictionary.
- [NSKeyValueObservedChange](nskeyvalueobservedchange.md)
- [NSKeyValueOperator](nskeyvalueoperator.md) — These constants define the available array operators. See [Using Collection Operators](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/CollectionOperators.html) for more information.
