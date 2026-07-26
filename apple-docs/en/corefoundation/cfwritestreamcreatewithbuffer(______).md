---
title: 'CFWriteStreamCreateWithBuffer(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfwritestreamcreatewithbuffer(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfwritestreamcreatewithbuffer(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfwritestreamcreatewithbuffer%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:3d02c723d7c70648'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFWriteStreamCreateWithBuffer(_:_:_:)

<sub>Function</sub>

Creates a writable stream for a fixed-size block of memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFWriteStreamCreateWithBuffer(_ alloc: CFAllocator!, _ buffer: UnsafeMutablePointer<UInt8>!, _ bufferCapacity: CFIndex) -> CFWriteStream!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `buffer` — The memory buffer into which to write data. This buffer must exist for the lifetime of the stream.

- `bufferCapacity` — The size of `buffer` and the maximum number of bytes that can be written.

## Return Value

A new write stream, or `NULL` on failure. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

When `buffer` is filled after writing `bufferCapacity` bytes, the stream is exhausted and its status becomes [kCFStreamStatusAtEnd](cfstreamstatus/atend.md).

You must open the stream, using [CFWriteStreamOpen](<cfwritestreamopen(__).md>), before writing to it.

## See Also

### Creating a Write Stream

- [CFWriteStreamCreateWithAllocatedBuffers](<cfwritestreamcreatewithallocatedbuffers(____).md>) — Creates a writable stream for a growable block of memory.
- [CFWriteStreamCreateWithFile](<cfwritestreamcreatewithfile(____).md>) — Creates a writable stream for a file.
