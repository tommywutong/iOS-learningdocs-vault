---
title: NSMakeCollectable
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsmakecollectable
source_url: 'https://developer.apple.com/documentation/foundation/nsmakecollectable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmakecollectable.json'
content_hash: 'sha256:af7aac3ec3a4a9f8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMakeCollectable

<sub>Function</sub>

Makes a newly allocated Core Foundation object eligible for collection.

> [!warning] Deprecated
> Garbage collection is deprecated in OS X v10.8; instead,you should use AutomaticReference Counting—see [Transitioning to ARC Release Notes](https://developer.apple.com/library/archive/releasenotes/ObjectiveC/RN-TransitioningToARC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011226).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
static idNSMakeCollectable(CFTypeRef cf);
```

## Discussion

This function is a wrapper for [CFMakeCollectable](../corefoundation/cfmakecollectable.md), but its return type is `id`—avoiding the need for casting when using Cocoa objects.

This function may be useful when returning Core Foundation objects in code that must support both garbage-collected and non-garbage-collected environments, as illustrated in the following example.

```objc
- (CFDateRef)foo {
    CFDateRef aCFDate;
    // ...
    return [NSMakeCollectable(aCFDate) autorelease];
}
```

CFTypeRef style objects are garbage collected, yet only sometime after the last [CFRelease](../corefoundation/cfrelease.md) is performed. Particularly for fully-bridged CFTypeRef objects such as CFStrings and collections (such as CFDictionary), you must call either `CFMakeCollectable` or the more type safe `NSMakeCollectable`, preferably right upon allocation.

## See Also

### Legacy

- [NSGarbageCollector](nsgarbagecollector.md) — A convenient interface to the garbage collection system. _(deprecated)_
- [NSAllocateCollectable](nsallocatecollectable.md) — Allocates collectable memory. _(deprecated)_
- [NSReallocateCollectable](nsreallocatecollectable.md) — Reallocates collectable memory. _(deprecated)_
- [Memory Allocation Options](1539826-memory-allocation-options.md) — Constants used to control behavior when allocating or reallocating collectible memory.
