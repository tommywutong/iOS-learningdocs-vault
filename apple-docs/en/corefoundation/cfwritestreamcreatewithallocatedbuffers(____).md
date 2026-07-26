---
title: 'CFWriteStreamCreateWithAllocatedBuffers(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfwritestreamcreatewithallocatedbuffers(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfwritestreamcreatewithallocatedbuffers(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfwritestreamcreatewithallocatedbuffers%28_%3A_%3A%29.json'
content_hash: 'sha256:e3b384f4553b7f67'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFWriteStreamCreateWithAllocatedBuffers(_:_:)

<sub>Function</sub>

Creates a writable stream for a growable block of memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFWriteStreamCreateWithAllocatedBuffers(_ alloc: CFAllocator!, _ bufferAllocator: CFAllocator!) -> CFWriteStream!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `bufferAllocator` — The allocator to use to allocate memory for the stream’s memory buffers. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

## Return Value

A new write stream. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

New buffers are allocated using `bufferAllocator` as bytes are written to the stream. At any point, you can recover the bytes thus far written by asking for the property kCFStreamPropertyDataWritten with [CFWriteStreamCopyProperty](<cfwritestreamcopyproperty(____).md>).

You must open the stream, using [CFWriteStreamOpen](<cfwritestreamopen(__).md>), before writing to it.

## See Also

### Creating a Write Stream

- [CFWriteStreamCreateWithBuffer](<cfwritestreamcreatewithbuffer(______).md>) — Creates a writable stream for a fixed-size block of memory.
- [CFWriteStreamCreateWithFile](<cfwritestreamcreatewithfile(____).md>) — Creates a writable stream for a file.
