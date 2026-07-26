---
title: NSRealMemoryAvailable()
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（6.0 起废弃）, iPadOS 2.0+（6.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsrealmemoryavailable()
source_url: 'https://developer.apple.com/documentation/foundation/nsrealmemoryavailable()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsrealmemoryavailable%28%29.json'
content_hash: 'sha256:8c2c3059891e5527'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSRealMemoryAvailable()

<sub>Function</sub>

Returns information about the user’s system.

> [!warning] Deprecated
> Use NSProcessInfo instead

<sub>tvOS, visionOS, watchOS</sub>

```swift
func NSRealMemoryAvailable() -> Int
```

## Return Value

The number of bytes available in RAM.

## See Also

### Memory Management

- [NSAllocateMemoryPages](<nsallocatememorypages(__).md>) — Allocates a new block of memory.
- [NSCopyMemoryPages](<nscopymemorypages(______).md>) — Copies a block of memory.
- [NSDeallocateMemoryPages](<nsdeallocatememorypages(____).md>) — Deallocates the specified block of memory.
- [NSLogPageSize](<nslogpagesize().md>) — Returns the binary log of the page size.
- [NSPageSize](<nspagesize().md>) — Returns the number of bytes in a page.
- [NSRoundDownToMultipleOfPageSize](<nsrounddowntomultipleofpagesize(__).md>) — Returns the specified number of bytes rounded down to a multiple of the page size.
- [NSRoundUpToMultipleOfPageSize](<nsrounduptomultipleofpagesize(__).md>) — Returns the specified number of bytes rounded up to a multiple of the page size.
