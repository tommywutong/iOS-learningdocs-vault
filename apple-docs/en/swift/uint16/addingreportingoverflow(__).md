---
title: 'addingReportingOverflow(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint16/addingreportingoverflow(_:)'
source_url: 'https://developer.apple.com/documentation/swift/uint16/addingreportingoverflow(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint16/addingreportingoverflow%28_%3A%29.json'
content_hash: 'sha256:9bce87e93e4aab0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt16](../uint16.md)

# addingReportingOverflow(_:)

<sub>Instance Method</sub>

Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addingReportingOverflow(_ other: UInt16) -> (partialValue: UInt16, overflow: Bool)
```

## Return Value

A tuple containing the result of the addition along with a Boolean value indicating whether overflow occurred. If the `overflow` component is `false`, the `partialValue` component contains the entire sum. If the `overflow` component is `true`, an overflow occurred and the `partialValue` component contains the truncated sum of this value and `rhs`.
