---
title: 'NSAllocateMemoryPages(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsallocatememorypages(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsallocatememorypages(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsallocatememorypages%28_%3A%29.json'
content_hash: 'sha256:603a55b9f0b26de6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSAllocateMemoryPages(_:)

<sub>Function</sub>

Allocates a new block of memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSAllocateMemoryPages(_ bytes: Int) -> UnsafeMutableRawPointer
```

## Discussion

Allocates the integral number of pages whose total size is closest to, but not less than, `byteCount`. The allocated pages are guaranteed to be filled with zeros. If the allocation fails, raises `NSInvalidArgumentException`.

## See Also

### Memory Management

- [NSCopyMemoryPages](<nscopymemorypages(______).md>) — Copies a block of memory.
- [NSDeallocateMemoryPages](<nsdeallocatememorypages(____).md>) — Deallocates the specified block of memory.
- [NSLogPageSize](<nslogpagesize().md>) — Returns the binary log of the page size.
- [NSPageSize](<nspagesize().md>) — Returns the number of bytes in a page.
- [NSRealMemoryAvailable](<nsrealmemoryavailable().md>) — Returns information about the user’s system. _(deprecated)_
- [NSRoundDownToMultipleOfPageSize](<nsrounddowntomultipleofpagesize(__).md>) — Returns the specified number of bytes rounded down to a multiple of the page size.
- [NSRoundUpToMultipleOfPageSize](<nsrounduptomultipleofpagesize(__).md>) — Returns the specified number of bytes rounded up to a multiple of the page size.
