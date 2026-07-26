---
title: 'CFWriteStreamCreateWithFile(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfwritestreamcreatewithfile(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfwritestreamcreatewithfile(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfwritestreamcreatewithfile%28_%3A_%3A%29.json'
content_hash: 'sha256:a90244715dd35943'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFWriteStreamCreateWithFile(_:_:)

<sub>Function</sub>

Creates a writable stream for a file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFWriteStreamCreateWithFile(_ alloc: CFAllocator!, _ fileURL: CFURL!) -> CFWriteStream!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `fileURL` — The URL of the file to which to write. The URL must use a file scheme.

## Return Value

The new write stream, or `NULL` on failure. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The stream overwrites an existing file unless you set the kCFStreamPropertyAppendToFile to kCFBooleanTrue with [CFWriteStreamSetProperty](<cfwritestreamsetproperty(______).md>), in which case the stream appends data to the file.

You must open the stream, using [CFWriteStreamOpen](<cfwritestreamopen(__).md>), before writing to it.

## See Also

### Creating a Write Stream

- [CFWriteStreamCreateWithAllocatedBuffers](<cfwritestreamcreatewithallocatedbuffers(____).md>) — Creates a writable stream for a growable block of memory.
- [CFWriteStreamCreateWithBuffer](<cfwritestreamcreatewithbuffer(______).md>) — Creates a writable stream for a fixed-size block of memory.
