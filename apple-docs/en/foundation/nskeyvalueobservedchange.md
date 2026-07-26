---
title: NSKeyValueObservedChange
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyvalueobservedchange
source_url: 'https://developer.apple.com/documentation/foundation/nskeyvalueobservedchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyvalueobservedchange.json'
content_hash: 'sha256:79807517e0bc0ae3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSKeyValueObservedChange

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSKeyValueObservedChange<Value>
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [indexes](nskeyvalueobservedchange/indexes.md) — indexes will be nil unless the observed KeyPath refers to an ordered to-many property
- [isPrior](nskeyvalueobservedchange/isprior.md) — ‘isPrior’ will be true if this change observation is being sent before the change happens, due to .prior being passed to `observe()`
- [kind](nskeyvalueobservedchange/kind-swift.property.md)
- [newValue](nskeyvalueobservedchange/newvalue.md) — newValue and oldValue will only be non-nil if .new/.old is passed to `observe()`. In general, get the most up to date value by accessing it directly on the observed object instead.
- [oldValue](nskeyvalueobservedchange/oldvalue.md)

### Type Aliases

- [Kind](nskeyvalueobservedchange/kind-swift.typealias.md)

## See Also

### Structures

- [AsyncCharacterSequence](asynccharactersequence.md) — An asynchronous sequence of characters.
- [AsyncLineSequence](asynclinesequence.md) — An asynchronous sequence of lines of text.
- [AsyncUnicodeScalarSequence](asyncunicodescalarsequence.md) — An asychronous sequence of Unicode scalar values.
- [Expression](expression.md)
- [NSAttributedStringFormattingContextKey](nsattributedstringformattingcontextkey.md) — A type that represents a key in the formatting context dictionary.
- [NSKeyValueChangeKey](nskeyvaluechangekey.md) — The keys that can appear in the change dictionary.
- [NSKeyValueOperator](nskeyvalueoperator.md) — These constants define the available array operators. See [Using Collection Operators](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/CollectionOperators.html) for more information.
- [PresentationIntent](presentationintent.md) — A type that defines presentation intent for blocks of characters like paragraphs, lists, block quotes, and tables.
