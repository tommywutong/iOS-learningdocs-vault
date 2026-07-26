---
title: 'alignment(ofValue:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/memorylayout/alignment(ofvalue:)'
source_url: 'https://developer.apple.com/documentation/swift/memorylayout/alignment(ofvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/memorylayout/alignment%28ofvalue%3A%29.json'
content_hash: 'sha256:084e09987c63bb7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MemoryLayout](../memorylayout.md)

# alignment(ofValue:)

<sub>Type Method</sub>

Returns the default memory alignment of `T`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func alignment(ofValue value: borrowing T) -> Int
```

## Parameters

- `value` — A value representative of the type to describe.

## Return Value

The default memory alignment, in bytes, of the given value’s type. This value is always positive.

## Discussion

Use a type’s alignment when allocating memory using an unsafe pointer.

When you have a type instead of an instance, use the `MemoryLayout<T>.stride` static property instead.

```swift
let x: Int = 100

// Finding the alignment of a value's type
let s = MemoryLayout.alignment(ofValue: x)
// s == 8

// Finding the alignment of a type directly
let t = MemoryLayout<Int>.alignment
// t == 8
```

## See Also

### Accessing the Layout of a Value

- [stride(ofValue:)](<stride(ofvalue_).md>) — Returns the number of bytes from the start of one instance of `T` to the start of the next when stored in contiguous memory or in an `Array<T>`.
- [size(ofValue:)](<size(ofvalue_).md>) — Returns the contiguous memory footprint of the given instance.
