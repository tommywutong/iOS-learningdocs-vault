---
title: PredicateExpressions.DictionaryKeySubscript
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateexpressions/dictionarykeysubscript
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/dictionarykeysubscript'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/dictionarykeysubscript.json'
content_hash: 'sha256:9eceefd9d0ce32f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# PredicateExpressions.DictionaryKeySubscript

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DictionaryKeySubscript<Wrapped, Key, Value> where Wrapped : PredicateExpression, Key : PredicateExpression, Wrapped.Output == [Key.Output : Value], Key.Output : Hashable
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Escapable](../../swift/escapable.md), [PredicateExpression](../predicateexpression.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [StandardPredicateExpression](../standardpredicateexpression.md)

## Topics

### Initializers

- [init(wrapped:key:)](<dictionarykeysubscript/init(wrapped_key_).md>)

### Instance Properties

- [key](dictionarykeysubscript/key.md)
- [wrapped](dictionarykeysubscript/wrapped.md)
