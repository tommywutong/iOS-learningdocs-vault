---
title: 'CFDataCreateMutableCopy(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdatacreatemutablecopy(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdatacreatemutablecopy(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdatacreatemutablecopy%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:77a140c317e6fb3e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDataCreateMutableCopy(_:_:_:)

<sub>Function</sub>

Creates a CFMutableData object by copying another CFData object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDataCreateMutableCopy(_ allocator: CFAllocator!, _ capacity: CFIndex, _ theData: CFData!) -> CFMutableData!
```

## Parameters

- `allocator` — The CFAllocator object to be used to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `capacity` — The maximum number of bytes that the CFData object can contain. The CFData object starts with the same length as the original object, and can grow to contain this number of bytes. Pass `0` to specify that the maximum capacity is not limited. If non-`0`, `capacity` must be greater than or equal to the length of `theData`.

- `theData` — The CFData object to be copied.

## Return Value

A CFMutableData object that has the same contents as the original object. Returns `NULL` if there was a problem copying the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a Mutable Data Object

- [CFDataCreateMutable](<cfdatacreatemutable(____).md>) — Creates an empty CFMutableData object.
