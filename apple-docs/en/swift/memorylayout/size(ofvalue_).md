---
title: 'size(ofValue:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/memorylayout/size(ofvalue:)'
source_url: 'https://developer.apple.com/documentation/swift/memorylayout/size(ofvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/memorylayout/size%28ofvalue%3A%29.json'
content_hash: 'sha256:651c774835489a6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MemoryLayout](../memorylayout.md)

# size(ofValue:)

<sub>Type Method</sub>

Returns the contiguous memory footprint of the given instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func size(ofValue value: borrowing T) -> Int
```

## Parameters

- `value` — A value representative of the type to describe.

## Return Value

The size, in bytes, of the given value’s type.

## Discussion

The result does not include any dynamically allocated or out of line storage. In particular, pointers and class instances all have the same contiguous memory footprint, regardless of the size of the referenced data.

When you have a type instead of an instance, use the `MemoryLayout<T>.size` static property instead.

```swift
let x: Int = 100

// Finding the size of a value's type
let s = MemoryLayout.size(ofValue: x)
// s == 8

// Finding the size of a type directly
let t = MemoryLayout<Int>.size
// t == 8
```

## See Also

### Accessing the Layout of a Value

- [stride(ofValue:)](<stride(ofvalue_).md>) — Returns the number of bytes from the start of one instance of `T` to the start of the next when stored in contiguous memory or in an `Array<T>`.
- [alignment(ofValue:)](<alignment(ofvalue_).md>) — Returns the default memory alignment of `T`.
