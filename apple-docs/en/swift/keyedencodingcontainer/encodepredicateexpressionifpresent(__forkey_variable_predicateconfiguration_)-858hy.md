---
title: 'encodePredicateExpressionIfPresent(_:forKey:variable:predicateConfiguration:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyedencodingcontainer/encodepredicateexpressionifpresent(_:forkey:variable:predicateconfiguration:)-858hy'
source_url: 'https://developer.apple.com/documentation/swift/keyedencodingcontainer/encodepredicateexpressionifpresent(_:forkey:variable:predicateconfiguration:)-858hy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyedencodingcontainer/encodepredicateexpressionifpresent%28_%3Aforkey%3Avariable%3Apredicateconfiguration%3A%29-858hy.json'
content_hash: 'sha256:5087acb556cbf242'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedEncodingContainer](../keyedencodingcontainer.md)

# encodePredicateExpressionIfPresent(_:forKey:variable:predicateConfiguration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encodePredicateExpressionIfPresent<T, each Input>(_ expression: T?, forKey key: KeyedEncodingContainer<K>.Key, variable: repeat PredicateExpressions.Variable<each Input>, predicateConfiguration: PredicateCodableConfiguration) throws where T : PredicateExpression, T : Encodable
```
