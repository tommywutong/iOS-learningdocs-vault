---
title: NSPageSize()
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspagesize()
source_url: 'https://developer.apple.com/documentation/foundation/nspagesize()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspagesize%28%29.json'
content_hash: 'sha256:35dcf8a58313713c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSPageSize()

<sub>Function</sub>

Returns the number of bytes in a page.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSPageSize() -> Int
```

## Return Value

The number of bytes in a page.

## See Also

### Memory Management

- [NSAllocateMemoryPages](<nsallocatememorypages(__).md>) — Allocates a new block of memory.
- [NSCopyMemoryPages](<nscopymemorypages(______).md>) — Copies a block of memory.
- [NSDeallocateMemoryPages](<nsdeallocatememorypages(____).md>) — Deallocates the specified block of memory.
- [NSLogPageSize](<nslogpagesize().md>) — Returns the binary log of the page size.
- [NSRealMemoryAvailable](<nsrealmemoryavailable().md>) — Returns information about the user’s system. _(deprecated)_
- [NSRoundDownToMultipleOfPageSize](<nsrounddowntomultipleofpagesize(__).md>) — Returns the specified number of bytes rounded down to a multiple of the page size.
- [NSRoundUpToMultipleOfPageSize](<nsrounduptomultipleofpagesize(__).md>) — Returns the specified number of bytes rounded up to a multiple of the page size.
