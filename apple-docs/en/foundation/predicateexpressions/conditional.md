---
title: PredicateExpressions.Conditional
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateexpressions/conditional
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/conditional'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/conditional.json'
content_hash: 'sha256:d9f4fdfc098bbdea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# PredicateExpressions.Conditional

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Conditional<Test, If, Else> where Test : PredicateExpression, If : PredicateExpression, Else : PredicateExpression, Test.Output == Bool, If.Output == Else.Output
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Escapable](../../swift/escapable.md), [PredicateExpression](../predicateexpression.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [StandardPredicateExpression](../standardpredicateexpression.md)

## Topics

### Initializers

- [init(test:trueBranch:falseBranch:)](<conditional/init(test_truebranch_falsebranch_).md>)

### Instance Properties

- [falseBranch](conditional/falsebranch.md)
- [test](conditional/test.md)
- [trueBranch](conditional/truebranch.md)
