---
title: PredicateExpressions.DictionaryKeyDefaultValueSubscript
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateexpressions/dictionarykeydefaultvaluesubscript
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/dictionarykeydefaultvaluesubscript'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/dictionarykeydefaultvaluesubscript.json'
content_hash: 'sha256:3306d7dfd4a2e036'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# PredicateExpressions.DictionaryKeyDefaultValueSubscript

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DictionaryKeyDefaultValueSubscript<Wrapped, Key, Default> where Wrapped : PredicateExpression, Key : PredicateExpression, Default : PredicateExpression, Wrapped.Output == [Key.Output : Default.Output], Key.Output : Hashable
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Escapable](../../swift/escapable.md), [PredicateExpression](../predicateexpression.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [StandardPredicateExpression](../standardpredicateexpression.md)

## Topics

### Initializers

- [init(wrapped:key:default:)](<dictionarykeydefaultvaluesubscript/init(wrapped_key_default_).md>)

### Instance Properties

- [default](dictionarykeydefaultvaluesubscript/default.md)
- [key](dictionarykeydefaultvaluesubscript/key.md)
- [wrapped](dictionarykeydefaultvaluesubscript/wrapped.md)
