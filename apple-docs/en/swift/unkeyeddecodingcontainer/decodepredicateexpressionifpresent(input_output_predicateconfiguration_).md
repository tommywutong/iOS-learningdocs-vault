---
title: 'decodePredicateExpressionIfPresent(input:output:predicateConfiguration:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unkeyeddecodingcontainer/decodepredicateexpressionifpresent(input:output:predicateconfiguration:)'
source_url: 'https://developer.apple.com/documentation/swift/unkeyeddecodingcontainer/decodepredicateexpressionifpresent(input:output:predicateconfiguration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyeddecodingcontainer/decodepredicateexpressionifpresent%28input%3Aoutput%3Apredicateconfiguration%3A%29.json'
content_hash: 'sha256:243da81abce088f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedDecodingContainer](../unkeyeddecodingcontainer.md)

# decodePredicateExpressionIfPresent(input:output:predicateConfiguration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func decodePredicateExpressionIfPresent<each Input, Output>(input: repeat (each Input).Type, output: Output.Type, predicateConfiguration: PredicateCodableConfiguration) throws -> (expression: any PredicateExpression<Output>, variable: (repeat PredicateExpressions.Variable<each Input>))?
```
