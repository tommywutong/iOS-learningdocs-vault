---
title: 'decodePredicateExpressionIfPresent(forKey:input:output:predicateConfiguration:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyeddecodingcontainer/decodepredicateexpressionifpresent(forkey:input:output:predicateconfiguration:)'
source_url: 'https://developer.apple.com/documentation/swift/keyeddecodingcontainer/decodepredicateexpressionifpresent(forkey:input:output:predicateconfiguration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyeddecodingcontainer/decodepredicateexpressionifpresent%28forkey%3Ainput%3Aoutput%3Apredicateconfiguration%3A%29.json'
content_hash: 'sha256:8848fb82f8de892e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedDecodingContainer](../keyeddecodingcontainer.md)

# decodePredicateExpressionIfPresent(forKey:input:output:predicateConfiguration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func decodePredicateExpressionIfPresent<each Input, Output>(forKey key: KeyedDecodingContainer<K>.Key, input: repeat (each Input).Type, output: Output.Type, predicateConfiguration: PredicateCodableConfiguration) throws -> (expression: any PredicateExpression<Output>, variable: (repeat PredicateExpressions.Variable<each Input>))?
```
