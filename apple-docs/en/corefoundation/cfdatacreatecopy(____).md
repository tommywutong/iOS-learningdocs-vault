---
title: 'CFDataCreateCopy(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdatacreatecopy(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdatacreatecopy(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdatacreatecopy%28_%3A_%3A%29.json'
content_hash: 'sha256:bf4aa38c28c1aabe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDataCreateCopy(_:_:)

<sub>Function</sub>

Creates an immutable copy of a CFData object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDataCreateCopy(_ allocator: CFAllocator!, _ theData: CFData!) -> CFData!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `theData` — The CFData object to copy.

## Return Value

An immutable copy of `theData`, or `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The resulting object has the same byte contents as the original object, but it is always immutable. If the specified allocator and the allocator of the original object are the same, and the string is already immutable, this function may simply increment the retain count without making a true copy. To the caller, however, the resulting object is a true immutable copy, except the operation was more efficient.

Use this function when you need to pass a CFData object into another function by value (not reference).

## See Also

### Creating a CFData Object

- [CFDataCreate](<cfdatacreate(______).md>) — Creates an immutable CFData object using data copied from a specified byte buffer.
- [CFDataCreateWithBytesNoCopy](<cfdatacreatewithbytesnocopy(________).md>) — Creates an immutable CFData object from an external (client-owned) byte buffer.
