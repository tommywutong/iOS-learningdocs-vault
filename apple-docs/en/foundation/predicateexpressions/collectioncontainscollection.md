---
title: PredicateExpressions.CollectionContainsCollection
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateexpressions/collectioncontainscollection
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/collectioncontainscollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/collectioncontainscollection.json'
content_hash: 'sha256:c02a3c80fd3a9064'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# PredicateExpressions.CollectionContainsCollection

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CollectionContainsCollection<Base, Other> where Base : PredicateExpression, Other : PredicateExpression, Base.Output : Collection, Other.Output : Collection, Base.Output.Element : Equatable, Base.Output.Element == Other.Output.Element
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Escapable](../../swift/escapable.md), [PredicateExpression](../predicateexpression.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [StandardPredicateExpression](../standardpredicateexpression.md)

## Topics

### Initializers

- [init(base:other:)](<collectioncontainscollection/init(base_other_).md>)

### Instance Properties

- [base](collectioncontainscollection/base.md)
- [other](collectioncontainscollection/other.md)
