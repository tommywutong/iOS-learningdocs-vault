---
title: 'encodePredicateExpressionIfPresent(_:variable:predicateConfiguration:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unkeyedencodingcontainer/encodepredicateexpressionifpresent(_:variable:predicateconfiguration:)-75j8t'
source_url: 'https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/encodepredicateexpressionifpresent(_:variable:predicateconfiguration:)-75j8t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyedencodingcontainer/encodepredicateexpressionifpresent%28_%3Avariable%3Apredicateconfiguration%3A%29-75j8t.json'
content_hash: 'sha256:6dd952a88ac60147'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedEncodingContainer](../unkeyedencodingcontainer.md)

# encodePredicateExpressionIfPresent(_:variable:predicateConfiguration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encodePredicateExpressionIfPresent<T, each Input>(_ expression: T?, variable: repeat PredicateExpressions.Variable<each Input>, predicateConfiguration: PredicateCodableConfiguration) throws where T : PredicateExpression, T : Encodable, T.Output == Bool
```
