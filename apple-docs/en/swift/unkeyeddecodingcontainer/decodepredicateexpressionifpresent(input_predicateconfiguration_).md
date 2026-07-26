---
title: 'decodePredicateExpressionIfPresent(input:predicateConfiguration:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unkeyeddecodingcontainer/decodepredicateexpressionifpresent(input:predicateconfiguration:)'
source_url: 'https://developer.apple.com/documentation/swift/unkeyeddecodingcontainer/decodepredicateexpressionifpresent(input:predicateconfiguration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyeddecodingcontainer/decodepredicateexpressionifpresent%28input%3Apredicateconfiguration%3A%29.json'
content_hash: 'sha256:b2ac040f57f5e800'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedDecodingContainer](../unkeyeddecodingcontainer.md)

# decodePredicateExpressionIfPresent(input:predicateConfiguration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func decodePredicateExpressionIfPresent<each Input>(input: repeat (each Input).Type, predicateConfiguration: PredicateCodableConfiguration) throws -> (expression: any PredicateExpression<Bool>, variable: (repeat PredicateExpressions.Variable<each Input>))?
```
