---
title: 'stride(ofValue:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/memorylayout/stride(ofvalue:)'
source_url: 'https://developer.apple.com/documentation/swift/memorylayout/stride(ofvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/memorylayout/stride%28ofvalue%3A%29.json'
content_hash: 'sha256:d66bb31be3b48e9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MemoryLayout](../memorylayout.md)

# stride(ofValue:)

<sub>Type Method</sub>

Returns the number of bytes from the start of one instance of `T` to the start of the next when stored in contiguous memory or in an `Array<T>`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func stride(ofValue value: borrowing T) -> Int
```

## Parameters

- `value` — A value representative of the type to describe.

## Return Value

The stride, in bytes, of the given value’s type.

## Discussion

This is the same as the number of bytes moved when an `UnsafePointer<T>` instance is incremented. `T` may have a lower minimal alignment that trades runtime performance for space efficiency. The result is always positive.

When you have a type instead of an instance, use the `MemoryLayout<T>.stride` static property instead.

```swift
let x: Int = 100

// Finding the stride of a value's type
let s = MemoryLayout.stride(ofValue: x)
// s == 8

// Finding the stride of a type directly
let t = MemoryLayout<Int>.stride
// t == 8
```

## See Also

### Accessing the Layout of a Value

- [size(ofValue:)](<size(ofvalue_).md>) — Returns the contiguous memory footprint of the given instance.
- [alignment(ofValue:)](<alignment(ofvalue_).md>) — Returns the default memory alignment of `T`.
