---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/outputrawspan/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swift/outputrawspan/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/outputrawspan/subscript%28_%3A%29.json'
content_hash: 'sha256:44a9693c3fd6b8b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [OutputRawSpan](../outputrawspan.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the byte at the specified offset in the span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(byteOffset: Int) -> UInt8 { get set }
```

## Parameters

- `byteOffset` — The offset of the byte to access. `byteOffset` must be greater than or equal to zero, and less than `byteCount`.
