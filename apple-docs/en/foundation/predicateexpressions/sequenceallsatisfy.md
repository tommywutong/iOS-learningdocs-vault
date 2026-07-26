---
title: PredicateExpressions.SequenceAllSatisfy
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateexpressions/sequenceallsatisfy
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/sequenceallsatisfy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/sequenceallsatisfy.json'
content_hash: 'sha256:b3d784b6c7130fdc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# PredicateExpressions.SequenceAllSatisfy

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SequenceAllSatisfy<LHS, RHS> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output : Sequence, RHS.Output == Bool
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Escapable](../../swift/escapable.md), [PredicateExpression](../predicateexpression.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [StandardPredicateExpression](../standardpredicateexpression.md)

## Topics

### Initializers

- [init(_:builder:)](<sequenceallsatisfy/init(__builder_).md>)

### Instance Properties

- [sequence](sequenceallsatisfy/sequence.md)
- [test](sequenceallsatisfy/test.md)
- [variable](sequenceallsatisfy/variable.md)

### Type Aliases

- [Element](sequenceallsatisfy/element.md)
