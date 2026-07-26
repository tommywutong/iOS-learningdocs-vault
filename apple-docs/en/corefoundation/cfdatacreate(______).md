---
title: 'CFDataCreate(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdatacreate(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdatacreate(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdatacreate%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:5cc653b481891bed'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDataCreate(_:_:_:)

<sub>Function</sub>

Creates an immutable CFData object using data copied from a specified byte buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDataCreate(_ allocator: CFAllocator!, _ bytes: UnsafePointer<UInt8>!, _ length: CFIndex) -> CFData!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `bytes` — A pointer to the byte buffer that contains the raw data to be copied into `theData`.

- `length` — The number of bytes in the buffer (`bytes`).

## Return Value

A new CFData object, or `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

You must supply a count of the bytes in the buffer. This function always copies the bytes in the provided buffer into internal storage.

## See Also

### Creating a CFData Object

- [CFDataCreateCopy](<cfdatacreatecopy(____).md>) — Creates an immutable copy of a CFData object.
- [CFDataCreateWithBytesNoCopy](<cfdatacreatewithbytesnocopy(________).md>) — Creates an immutable CFData object from an external (client-owned) byte buffer.
