---
title: 'CFReadStreamCreateWithFile(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfreadstreamcreatewithfile(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfreadstreamcreatewithfile(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfreadstreamcreatewithfile%28_%3A_%3A%29.json'
content_hash: 'sha256:ea9cadbb4a5d012f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFReadStreamCreateWithFile(_:_:)

<sub>Function</sub>

Creates a readable stream for a file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFReadStreamCreateWithFile(_ alloc: CFAllocator!, _ fileURL: CFURL!) -> CFReadStream!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `fileURL` — The URL of the file to read. The URL must use the file scheme.

## Return Value

The new readable stream object, or `NULL` on failure. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

You must open the stream, using [CFReadStreamOpen](<cfreadstreamopen(__).md>), before reading from it.

## See Also

### Creating a Read Stream

- [CFReadStreamCreateWithBytesNoCopy](<cfreadstreamcreatewithbytesnocopy(________).md>) — Creates a readable stream for a block of memory.
