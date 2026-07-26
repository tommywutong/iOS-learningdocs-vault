---
title: PredicateExpressions.Range
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateexpressions/range
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/range'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/range.json'
content_hash: 'sha256:fcf52d1bd327ba0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# PredicateExpressions.Range

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Range<LHS, RHS> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output : Comparable, LHS.Output == RHS.Output
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Escapable](../../swift/escapable.md), [PredicateExpression](../predicateexpression.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [StandardPredicateExpression](../standardpredicateexpression.md)

## Topics

### Initializers

- [init(lower:upper:)](<range/init(lower_upper_).md>)

### Instance Properties

- [lower](range/lower.md)
- [upper](range/upper.md)
