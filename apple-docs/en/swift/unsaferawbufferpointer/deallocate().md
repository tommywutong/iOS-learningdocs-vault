---
title: deallocate()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsaferawbufferpointer/deallocate()
source_url: 'https://developer.apple.com/documentation/swift/unsaferawbufferpointer/deallocate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsaferawbufferpointer/deallocate%28%29.json'
content_hash: 'sha256:d8469505b1437c47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeRawBufferPointer](../unsaferawbufferpointer.md)

# deallocate()

<sub>Instance Method</sub>

Deallocates the memory block previously allocated at this buffer pointer’s base address.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func deallocate()
```

## Discussion

This buffer pointer’s `baseAddress` must be `nil` or a pointer to a memory block previously returned by a Swift allocation method. If `baseAddress` is `nil`, this function does nothing. Otherwise, the memory must not be initialized or `Pointee` must be a trivial type. This buffer pointer’s byte `count` must be equal to the originally allocated size of the memory block.
