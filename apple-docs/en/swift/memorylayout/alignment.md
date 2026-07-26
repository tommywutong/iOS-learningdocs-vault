---
title: alignment
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/memorylayout/alignment
source_url: 'https://developer.apple.com/documentation/swift/memorylayout/alignment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/memorylayout/alignment.json'
content_hash: 'sha256:4f4084da1dd64242'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MemoryLayout](../memorylayout.md)

# alignment

<sub>Type Property</sub>

The default memory alignment of `T`, in bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var alignment: Int { get }
```

## Discussion

Use the `alignment` property for a type when allocating memory using an unsafe pointer. This value is always positive.

## See Also

### Accessing the Layout of a Type

- [size](size.md) — The contiguous memory footprint of `T`, in bytes.
- [stride](stride.md) — The number of bytes from the start of one instance of `T` to the start of the next when stored in contiguous memory or in an `Array<T>`.
