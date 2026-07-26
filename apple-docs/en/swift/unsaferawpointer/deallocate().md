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
doc_path: /documentation/swift/unsaferawpointer/deallocate()
source_url: 'https://developer.apple.com/documentation/swift/unsaferawpointer/deallocate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsaferawpointer/deallocate%28%29.json'
content_hash: 'sha256:ef3616a219da164e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeRawPointer](../unsaferawpointer.md)

# deallocate()

<sub>Instance Method</sub>

Deallocates the previously allocated memory block referenced by this pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func deallocate()
```

## Discussion

The memory to be deallocated must be uninitialized or initialized to a trivial type.
