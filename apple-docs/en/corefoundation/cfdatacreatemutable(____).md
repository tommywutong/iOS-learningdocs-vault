---
title: 'CFDataCreateMutable(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdatacreatemutable(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdatacreatemutable(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdatacreatemutable%28_%3A_%3A%29.json'
content_hash: 'sha256:41ca1f5d2f7b7621'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDataCreateMutable(_:_:)

<sub>Function</sub>

Creates an empty CFMutableData object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDataCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex) -> CFMutableData!
```

## Parameters

- `allocator` — The CFAllocator object to be used to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `capacity` — The maximum number of bytes that the CFData object can contain. The CFData object starts empty and can grow to contain this number of values (and it can have less). Pass `0` to specify that the maximum capacity is not limited. The value must not be negative.

## Return Value

A CFMutableData object or `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function creates an empty (that is, content-less) CFMutableData object. You can add raw data to this object with the [CFDataAppendBytes](<cfdataappendbytes(______).md>) function, and thereafter you can replace and delete characters with the appropriate CFMutableData functions. If the `capacity` parameter is greater than `0`, any attempt to add characters beyond this limit can result in undefined behavior.

## See Also

### Creating a Mutable Data Object

- [CFDataCreateMutableCopy](<cfdatacreatemutablecopy(______).md>) — Creates a CFMutableData object by copying another CFData object.
