---
title: 'subtractingReportingOverflow(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int16/subtractingreportingoverflow(_:)'
source_url: 'https://developer.apple.com/documentation/swift/int16/subtractingreportingoverflow(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int16/subtractingreportingoverflow%28_%3A%29.json'
content_hash: 'sha256:ccdd60d6ae1700e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int16](../int16.md)

# subtractingReportingOverflow(_:)

<sub>Instance Method</sub>

Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func subtractingReportingOverflow(_ other: Int16) -> (partialValue: Int16, overflow: Bool)
```

## Return Value

A tuple containing the result of the subtraction along with a Boolean value indicating whether overflow occurred. If the `overflow` component is `false`, the `partialValue` component contains the entire difference. If the `overflow` component is `true`, an overflow occurred and the `partialValue` component contains the truncated result of `rhs` subtracted from this value.
