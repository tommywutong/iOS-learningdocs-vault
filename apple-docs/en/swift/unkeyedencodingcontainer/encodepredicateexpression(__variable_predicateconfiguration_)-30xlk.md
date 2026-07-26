---
title: 'encodePredicateExpression(_:variable:predicateConfiguration:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unkeyedencodingcontainer/encodepredicateexpression(_:variable:predicateconfiguration:)-30xlk'
source_url: 'https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/encodepredicateexpression(_:variable:predicateconfiguration:)-30xlk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unkeyedencodingcontainer/encodepredicateexpression%28_%3Avariable%3Apredicateconfiguration%3A%29-30xlk.json'
content_hash: 'sha256:2e288667a3a9ebc7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnkeyedEncodingContainer](../unkeyedencodingcontainer.md)

# encodePredicateExpression(_:variable:predicateConfiguration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encodePredicateExpression<T, each Input>(_ expression: T, variable: repeat PredicateExpressions.Variable<each Input>, predicateConfiguration: PredicateCodableConfiguration) throws where T : PredicateExpression, T : Encodable, T.Output == Bool
```
