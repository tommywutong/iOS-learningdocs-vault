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
doc_path: /documentation/swift/unsafemutablepointer/deallocate()
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablepointer/deallocate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablepointer/deallocate%28%29.json'
content_hash: 'sha256:57a91a8964303373'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutablePointer](../unsafemutablepointer.md)

# deallocate()

<sub>Instance Method</sub>

Deallocates the memory block previously allocated at this pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func deallocate()
```

## Discussion

This pointer must be a pointer to the start of a previously allocated memory block. The memory must not be initialized or `Pointee` must be a trivial type.
