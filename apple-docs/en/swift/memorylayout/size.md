---
title: size
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/memorylayout/size
source_url: 'https://developer.apple.com/documentation/swift/memorylayout/size'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/memorylayout/size.json'
content_hash: 'sha256:2faca1df4827f3d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MemoryLayout](../memorylayout.md)

# size

<sub>Type Property</sub>

The contiguous memory footprint of `T`, in bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var size: Int { get }
```

## Discussion

A type’s size does not include any dynamically allocated or out of line storage. In particular, `MemoryLayout<T>.size`, when `T` is a class type, is the same regardless of how many stored properties `T` has.

When allocating memory for multiple instances of `T` using an unsafe pointer, use a multiple of the type’s stride instead of its size.

## See Also

### Accessing the Layout of a Type

- [alignment](alignment.md) — The default memory alignment of `T`, in bytes.
- [stride](stride.md) — The number of bytes from the start of one instance of `T` to the start of the next when stored in contiguous memory or in an `Array<T>`.
