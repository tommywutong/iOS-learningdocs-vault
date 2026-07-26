---
title: PredicateExpressions.RangeExpressionContains
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateexpressions/rangeexpressioncontains
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/rangeexpressioncontains'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/rangeexpressioncontains.json'
content_hash: 'sha256:ca78a2590c5e4991'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# PredicateExpressions.RangeExpressionContains

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RangeExpressionContains<RangeExpression, Element> where RangeExpression : PredicateExpression, Element : PredicateExpression, RangeExpression.Output : RangeExpression, Element.Output == RangeExpression.Output.Bound
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Escapable](../../swift/escapable.md), [PredicateExpression](../predicateexpression.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [StandardPredicateExpression](../standardpredicateexpression.md)

## Topics

### Initializers

- [init(range:element:)](<rangeexpressioncontains/init(range_element_).md>)

### Instance Properties

- [element](rangeexpressioncontains/element.md)
- [range](rangeexpressioncontains/range.md)
