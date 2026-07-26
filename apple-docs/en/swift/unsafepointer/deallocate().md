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
doc_path: /documentation/swift/unsafepointer/deallocate()
source_url: 'https://developer.apple.com/documentation/swift/unsafepointer/deallocate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafepointer/deallocate%28%29.json'
content_hash: 'sha256:cc4d4f8adf45a587'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafePointer](../unsafepointer.md)

# deallocate()

<sub>Instance Method</sub>

Deallocates the memory block previously allocated at this pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func deallocate()
```

## Discussion

This pointer must be a pointer to the start of a previously allocated memory block. The memory must not be initialized or `Pointee` must be a trivial type.
