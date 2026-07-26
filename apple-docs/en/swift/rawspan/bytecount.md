---
title: byteCount
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/rawspan/bytecount
source_url: 'https://developer.apple.com/documentation/swift/rawspan/bytecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rawspan/bytecount.json'
content_hash: 'sha256:bd1dac2311a61e3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RawSpan](../rawspan.md)

# byteCount

<sub>Instance Property</sub>

The number of bytes in the span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var byteCount: Int { get }
```

## Discussion

To check whether the span is empty, use its `isEmpty` property instead of comparing `byteCount` to zero.

> [!abstract] Complexity
> O(1)
