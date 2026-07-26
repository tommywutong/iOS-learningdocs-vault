---
title: bytes
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsafemutablerawbufferpointer/bytes
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/bytes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawbufferpointer/bytes.json'
content_hash: 'sha256:71462cd4a9823687'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableRawBufferPointer](../unsafemutablerawbufferpointer.md)

# bytes

<sub>Instance Property</sub>

A span over the bytes of this buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var bytes: RawSpan { get }
```

## Return Value

A `RawSpan` over the bytes of this buffer.

## Discussion

The lifetime of the returned span matches the lifetime of the binding which returns it. This lifetime is a convenience, as there can be no enforcement that there is no concurrent write to the underlying memory. The programmer must ensure that the memory remains allocated, initialized and immutable for the lifetime of the returned span.

> [!note] Note
> This property is unsafe because it cannot guarantee that the underlying memory remains valid and immutable for the lifetime of the returned span.

> [!abstract] Complexity
> O(1)
