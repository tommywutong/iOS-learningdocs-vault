---
title: CFRelease
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrelease
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrelease'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrelease.json'
content_hash: 'sha256:906b85f3b0c5b85b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRelease

<sub>Function</sub>

Releases a Core Foundation object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CFRelease(CFTypeRef cf);
```

## Parameters

- `cf` — A CFType object to release. This value must not be `NULL`.

## Discussion

If the retain count of `cf` becomes zero the memory allocated to the object is deallocated and the object is destroyed. If you create, copy, or explicitly retain (see the [CFRetain](cfretain.md) function) a Core Foundation object, you are responsible for releasing it when you no longer need it (see [Memory Management Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i)).

### Special Considerations

If `cf` is `NULL`, this will cause a runtime error and your application will crash.

## See Also

### Memory Management

- [CFGetAllocator](<cfgetallocator(__).md>) — Returns the allocator used to allocate a Core Foundation object.
- [CFGetRetainCount](<cfgetretaincount(__).md>) — Returns the reference count of a Core Foundation object.
- [CFMakeCollectable](cfmakecollectable.md) — Makes a newly-allocated Core Foundation object eligible for garbage collection.
- [CFRetain](cfretain.md) — Retains a Core Foundation object.
