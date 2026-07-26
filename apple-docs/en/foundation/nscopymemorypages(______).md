---
title: 'NSCopyMemoryPages(_:_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscopymemorypages(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscopymemorypages(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscopymemorypages%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:d43fbe3dead68a4c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCopyMemoryPages(_:_:_:)

<sub>Function</sub>

Copies a block of memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSCopyMemoryPages(_ source: UnsafeRawPointer, _ dest: UnsafeMutableRawPointer, _ bytes: Int)
```

## Discussion

Copies (or copies on write) `byteCount` bytes from `source` to `destination`.

## See Also

### Memory Management

- [NSAllocateMemoryPages](<nsallocatememorypages(__).md>) — Allocates a new block of memory.
- [NSDeallocateMemoryPages](<nsdeallocatememorypages(____).md>) — Deallocates the specified block of memory.
- [NSLogPageSize](<nslogpagesize().md>) — Returns the binary log of the page size.
- [NSPageSize](<nspagesize().md>) — Returns the number of bytes in a page.
- [NSRealMemoryAvailable](<nsrealmemoryavailable().md>) — Returns information about the user’s system. _(deprecated)_
- [NSRoundDownToMultipleOfPageSize](<nsrounddowntomultipleofpagesize(__).md>) — Returns the specified number of bytes rounded down to a multiple of the page size.
- [NSRoundUpToMultipleOfPageSize](<nsrounduptomultipleofpagesize(__).md>) — Returns the specified number of bytes rounded up to a multiple of the page size.
