---
title: PredicateExpressions.SequenceContainsWhere
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateexpressions/sequencecontainswhere
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/sequencecontainswhere'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/sequencecontainswhere.json'
content_hash: 'sha256:665b26ec726dc79b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# PredicateExpressions.SequenceContainsWhere

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SequenceContainsWhere<LHS, RHS> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output : Sequence, RHS.Output == Bool
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Escapable](../../swift/escapable.md), [PredicateExpression](../predicateexpression.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [StandardPredicateExpression](../standardpredicateexpression.md)

## Topics

### Initializers

- [init(_:builder:)](<sequencecontainswhere/init(__builder_).md>)

### Instance Properties

- [sequence](sequencecontainswhere/sequence.md)
- [test](sequencecontainswhere/test.md)
- [variable](sequencecontainswhere/variable.md)

### Type Aliases

- [Element](sequencecontainswhere/element.md)
