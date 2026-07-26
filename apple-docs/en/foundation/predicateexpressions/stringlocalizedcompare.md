---
title: PredicateExpressions.StringLocalizedCompare
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateexpressions/stringlocalizedcompare
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/stringlocalizedcompare'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/stringlocalizedcompare.json'
content_hash: 'sha256:d82f58d4f9f90473'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# PredicateExpressions.StringLocalizedCompare

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct StringLocalizedCompare<Root, Other> where Root : PredicateExpression, Other : PredicateExpression, Root.Output : StringProtocol, Other.Output : StringProtocol
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Escapable](../../swift/escapable.md), [PredicateExpression](../predicateexpression.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [StandardPredicateExpression](../standardpredicateexpression.md)

## Topics

### Initializers

- [init(root:other:)](<stringlocalizedcompare/init(root_other_).md>)

### Instance Properties

- [other](stringlocalizedcompare/other.md)
- [root](stringlocalizedcompare/root.md)
