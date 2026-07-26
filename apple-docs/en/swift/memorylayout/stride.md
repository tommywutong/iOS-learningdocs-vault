---
title: stride
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/memorylayout/stride
source_url: 'https://developer.apple.com/documentation/swift/memorylayout/stride'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/memorylayout/stride.json'
content_hash: 'sha256:701e82ea9f9edf0c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MemoryLayout](../memorylayout.md)

# stride

<sub>Type Property</sub>

The number of bytes from the start of one instance of `T` to the start of the next when stored in contiguous memory or in an `Array<T>`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var stride: Int { get }
```

## Discussion

This is the same as the number of bytes moved when an `UnsafePointer<T>` instance is incremented. `T` may have a lower minimal alignment that trades runtime performance for space efficiency. This value is always positive.

## See Also

### Accessing the Layout of a Type

- [size](size.md) — The contiguous memory footprint of `T`, in bytes.
- [alignment](alignment.md) — The default memory alignment of `T`, in bytes.
