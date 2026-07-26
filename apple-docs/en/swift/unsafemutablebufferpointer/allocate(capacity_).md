---
title: 'allocate(capacity:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablebufferpointer/allocate(capacity:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/allocate(capacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablebufferpointer/allocate%28capacity%3A%29.json'
content_hash: 'sha256:848f56bc5f28b5c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableBufferPointer](../unsafemutablebufferpointer.md)

# allocate(capacity:)

<sub>Type Method</sub>

Allocates uninitialized memory for the specified number of instances of type `Element`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func allocate(capacity count: Int) -> UnsafeMutableBufferPointer<Element>
```

## Parameters

- `count` — The amount of memory to allocate, counted in instances of `Element`.

## Discussion

The resulting buffer references a region of memory that is bound to `Element` and is `count * MemoryLayout<Element>.stride` bytes in size.

The following example allocates a buffer that can store four `Int` instances and then initializes that memory with the elements of a range:

```swift
let buffer = UnsafeMutableBufferPointer<Int>.allocate(capacity: 4)
_ = buffer.initialize(from: 1...4)
print(buffer[2])
// Prints "3"
```

When you allocate memory, always remember to deallocate once you’re finished.

```swift
buffer.deallocate()
```
