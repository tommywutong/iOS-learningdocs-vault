---
title: 'remainderReportingOverflow(dividingBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/fixedwidthinteger/remainderreportingoverflow(dividingby:)'
source_url: 'https://developer.apple.com/documentation/swift/fixedwidthinteger/remainderreportingoverflow(dividingby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/fixedwidthinteger/remainderreportingoverflow%28dividingby%3A%29.json'
content_hash: 'sha256:f49e1da2bd737a61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FixedWidthInteger](../fixedwidthinteger.md)

# remainderReportingOverflow(dividingBy:)

<sub>Instance Method</sub>

Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func remainderReportingOverflow(dividingBy rhs: Self) -> (partialValue: Self, overflow: Bool)
```

## Parameters

- `rhs` — The value to divide this value by.

## Return Value

A tuple containing the result of the operation along with a Boolean value indicating whether overflow occurred. If the `overflow` component is `false`, the `partialValue` component contains the entire remainder. If the `overflow` component is `true`, an overflow occurred during division and the `partialValue` component contains either the entire remainder or, if the remainder is undefined, the dividend.

## Discussion

Dividing by zero is not an error when using this method. For a value `x`, the result of `x.remainderReportingOverflow(dividingBy: 0)` is `(x, true)`.
