---
title: PredicateExpressions.SequenceMaximum
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateexpressions/sequencemaximum
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/sequencemaximum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/sequencemaximum.json'
content_hash: 'sha256:727c49f31c508d7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# PredicateExpressions.SequenceMaximum

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SequenceMaximum<Elements> where Elements : PredicateExpression, Elements.Output : Sequence, Elements.Output.Element : Comparable
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Escapable](../../swift/escapable.md), [PredicateExpression](../predicateexpression.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [StandardPredicateExpression](../standardpredicateexpression.md)

## Topics

### Initializers

- [init(elements:)](<sequencemaximum/init(elements_).md>)

### Instance Properties

- [elements](sequencemaximum/elements.md)
