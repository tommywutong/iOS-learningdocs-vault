---
title: 'dividedReportingOverflow(by:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint32/dividedreportingoverflow(by:)'
source_url: 'https://developer.apple.com/documentation/swift/uint32/dividedreportingoverflow(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint32/dividedreportingoverflow%28by%3A%29.json'
content_hash: 'sha256:4658d45d0eac6e65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt32](../uint32.md)

# dividedReportingOverflow(by:)

<sub>Instance Method</sub>

Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dividedReportingOverflow(by other: UInt32) -> (partialValue: UInt32, overflow: Bool)
```

## Return Value

A tuple containing the result of the division along with a Boolean value indicating whether overflow occurred. If the `overflow` component is `false`, the `partialValue` component contains the entire quotient. If the `overflow` component is `true`, an overflow occurred and the `partialValue` component contains either the truncated quotient or, if the quotient is undefined, the dividend.

## Discussion

Dividing by zero is not an error when using this method. For a value `x`, the result of `x.dividedReportingOverflow(by: 0)` is `(x, true)`.
