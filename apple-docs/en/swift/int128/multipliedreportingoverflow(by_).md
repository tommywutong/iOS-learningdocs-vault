---
title: 'multipliedReportingOverflow(by:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int128/multipliedreportingoverflow(by:)'
source_url: 'https://developer.apple.com/documentation/swift/int128/multipliedreportingoverflow(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int128/multipliedreportingoverflow%28by%3A%29.json'
content_hash: 'sha256:5ee4f260484d76e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int128](../int128.md)

# multipliedReportingOverflow(by:)

<sub>Instance Method</sub>

Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func multipliedReportingOverflow(by other: Int128) -> (partialValue: Int128, overflow: Bool)
```

## Return Value

A tuple containing the result of the multiplication along with a Boolean value indicating whether overflow occurred. If the `overflow` component is `false`, the `partialValue` component contains the entire product. If the `overflow` component is `true`, an overflow occurred and the `partialValue` component contains the truncated product of this value and `rhs`.
