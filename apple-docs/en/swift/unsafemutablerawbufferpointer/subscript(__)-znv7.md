---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablerawbufferpointer/subscript(_:)-znv7'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/subscript(_:)-znv7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawbufferpointer/subscript%28_%3A%29-znv7.json'
content_hash: 'sha256:f4437cc0a43826e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableRawBufferPointer](../unsafemutablerawbufferpointer.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the bytes in the specified memory region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(bounds: Range<Int>) -> UnsafeMutableRawBufferPointer.SubSequence { get nonmutating set }
```

## Parameters

- `bounds` — The range of byte offsets to access. The upper and lower bounds of the range must be in the range `0...count`.
