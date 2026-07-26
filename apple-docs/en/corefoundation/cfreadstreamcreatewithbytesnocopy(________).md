---
title: 'CFReadStreamCreateWithBytesNoCopy(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfreadstreamcreatewithbytesnocopy(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfreadstreamcreatewithbytesnocopy(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfreadstreamcreatewithbytesnocopy%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:f099ca5975414a1b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFReadStreamCreateWithBytesNoCopy(_:_:_:_:)

<sub>Function</sub>

Creates a readable stream for a block of memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFReadStreamCreateWithBytesNoCopy(_ alloc: CFAllocator!, _ bytes: UnsafePointer<UInt8>!, _ length: CFIndex, _ bytesDeallocator: CFAllocator!) -> CFReadStream!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `bytes` — The memory buffer to read. This memory must exist for the lifetime of the new stream.

- `length` — The size of `bytes`.

- `bytesDeallocator` — The allocator to use to deallocate `bytes` when the stream is deallocated. Pass kCFAllocatorNull to prevent the stream from deallocating `bytes`.

## Return Value

The new read stream, or `NULL` on failure. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

You must open the stream, using [CFReadStreamOpen](<cfreadstreamopen(__).md>), before reading from it.

## See Also

### Creating a Read Stream

- [CFReadStreamCreateWithFile](<cfreadstreamcreatewithfile(____).md>) — Creates a readable stream for a file.
