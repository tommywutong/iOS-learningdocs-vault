---
title: 'encodePredicateExpressionIfPresent(_:variable:predicateConfiguration:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unkeyedencodingcontainer/encodepredicateexpressionifpresent(_:variable:predicateconfiguration:)-438on'
source_url: 'https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/encodepredicateexpressionifpresent(_:variable:predicateconfiguration:)-438on'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyedencodingcontainer/encodepredicateexpressionifpresent%28_%3Avariable%3Apredicateconfiguration%3A%29-438on.json'
content_hash: 'sha256:95bded97f19b3ab7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedEncodingContainer](../unkeyedencodingcontainer.md)

# encodePredicateExpressionIfPresent(_:variable:predicateConfiguration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encodePredicateExpressionIfPresent<T, each Input>(_ expression: T?, variable: repeat PredicateExpressions.Variable<each Input>, predicateConfiguration: PredicateCodableConfiguration) throws where T : PredicateExpression, T : Encodable
```
