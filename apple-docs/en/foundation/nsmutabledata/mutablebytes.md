---
title: mutableBytes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutabledata/mutablebytes
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledata/mutablebytes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledata/mutablebytes.json'
content_hash: 'sha256:d5ea62f12645507e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableData](../nsmutabledata.md)

# mutableBytes

<sub>Instance Property</sub>

A pointer to the data contained by the mutable data object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mutableBytes: UnsafeMutableRawPointer { get }
```

## Discussion

If the length of the receiver’s data is not zero, this property is guaranteed to contain a pointer to the object’s internal bytes. If the length of receiver’s data _is_ zero, this property may or may not contain `NULL` dependent upon many factors related to how the object was created (moreover, in this case the method result might change between different releases). The returned pointer is valid until the data object is deallocated.

> [!note] Note
> This property is similar to, but different than the [bytes](../nsdata/bytes.md) property. The [bytes](../nsdata/bytes.md) property contains a pointer to a constant. You can use The [bytes](../nsdata/bytes.md) pointer to read the data managed by the data object, but you cannot modify that data. However, if the [mutableBytes](mutablebytes.md) property contains a non-`null` pointer, this pointer points to mutable data. You can use the [mutableBytes](mutablebytes.md) pointer to modify the data managed by the data object.

A sample using this method can be found in [Working With Mutable Binary Data](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/BinaryData/Tasks/WorkingMutableData.html#//apple_ref/doc/uid/20002150).

## See Also

### Related Documentation

- [bytes](../nsdata/bytes.md) — A pointer to the data object’s contents.
