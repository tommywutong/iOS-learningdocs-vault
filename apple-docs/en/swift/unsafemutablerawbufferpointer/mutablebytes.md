---
title: mutableBytes
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsafemutablerawbufferpointer/mutablebytes
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/mutablebytes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawbufferpointer/mutablebytes.json'
content_hash: 'sha256:5fd8a217c7117a43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableRawBufferPointer](../unsafemutablerawbufferpointer.md)

# mutableBytes

<sub>Instance Property</sub>

A mutable span over the bytes of this buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mutableBytes: MutableRawSpan { get }
```

## Return Value

A `MutableRawSpan` over the bytes of this buffer.

## Discussion

The lifetime of the returned span matches the lifetime of the binding which returns it. This lifetime is a convenience, as there can be no enforcement that there is no concurrent access to the underlying memory. The programmer must ensure that the memory remains allocated, initialized and exclusively accessed for the lifetime of the returned span.

> [!note] Note
> This property is unsafe because it cannot guarantee that the underlying memory remains valid and exclusively accessed for the lifetime of the returned span.

> [!abstract] Complexity
> O(1)
