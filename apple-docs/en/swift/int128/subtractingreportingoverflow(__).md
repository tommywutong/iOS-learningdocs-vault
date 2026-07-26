---
title: 'subtractingReportingOverflow(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int128/subtractingreportingoverflow(_:)'
source_url: 'https://developer.apple.com/documentation/swift/int128/subtractingreportingoverflow(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int128/subtractingreportingoverflow%28_%3A%29.json'
content_hash: 'sha256:6443361f95f7e611'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int128](../int128.md)

# subtractingReportingOverflow(_:)

<sub>Instance Method</sub>

Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func subtractingReportingOverflow(_ other: Int128) -> (partialValue: Int128, overflow: Bool)
```

## Return Value

A tuple containing the result of the subtraction along with a Boolean value indicating whether overflow occurred. If the `overflow` component is `false`, the `partialValue` component contains the entire difference. If the `overflow` component is `true`, an overflow occurred and the `partialValue` component contains the truncated result of `rhs` subtracted from this value.
