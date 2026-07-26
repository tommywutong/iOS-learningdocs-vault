---
title: 'remainderReportingOverflow(dividingBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int128/remainderreportingoverflow(dividingby:)'
source_url: 'https://developer.apple.com/documentation/swift/int128/remainderreportingoverflow(dividingby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int128/remainderreportingoverflow%28dividingby%3A%29.json'
content_hash: 'sha256:88bd7f557192ac6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int128](../int128.md)

# remainderReportingOverflow(dividingBy:)

<sub>Instance Method</sub>

Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func remainderReportingOverflow(dividingBy other: Int128) -> (partialValue: Int128, overflow: Bool)
```

## Return Value

A tuple containing the result of the operation along with a Boolean value indicating whether overflow occurred. If the `overflow` component is `false`, the `partialValue` component contains the entire remainder. If the `overflow` component is `true`, an overflow occurred during division and the `partialValue` component contains either the entire remainder or, if the remainder is undefined, the dividend.

## Discussion

Dividing by zero is not an error when using this method. For a value `x`, the result of `x.remainderReportingOverflow(dividingBy: 0)` is `(x, true)`.
