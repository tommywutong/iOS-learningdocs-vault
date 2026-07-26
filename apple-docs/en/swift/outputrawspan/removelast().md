---
title: removeLast()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/outputrawspan/removelast()
source_url: 'https://developer.apple.com/documentation/swift/outputrawspan/removelast()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/outputrawspan/removelast%28%29.json'
content_hash: 'sha256:fed0a2c1c77e7958'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [OutputRawSpan](../outputrawspan.md)

# removeLast()

<sub>Instance Method</sub>

Remove the last byte from this span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func removeLast() -> UInt8
```

## Return Value

The removed byte.

## Discussion

Returns the last byte. The `OutputRawSpan` must not be empty.
