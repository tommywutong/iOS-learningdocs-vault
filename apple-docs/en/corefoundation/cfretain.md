---
title: CFRetain
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfretain
source_url: 'https://developer.apple.com/documentation/corefoundation/cfretain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfretain.json'
content_hash: 'sha256:15faf1decc4ebf7c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRetain

<sub>Function</sub>

Retains a Core Foundation object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CFTypeRefCFRetain(CFTypeRef cf);
```

## Parameters

- `cf` — The CFType object to retain. This value must not be `NULL`

## Return Value

The input value, `cf`.

## Discussion

You should retain a Core Foundation object when you receive it from elsewhere (that is, you did not create or copy it) and you want it to persist. If you retain a Core Foundation object you are responsible for releasing it (see [Memory Management Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i)).

### Special Considerations

If `cf` is `NULL`, this will cause a runtime error and your application will crash.

## See Also

### Memory Management

- [CFGetAllocator](<cfgetallocator(__).md>) — Returns the allocator used to allocate a Core Foundation object.
- [CFGetRetainCount](<cfgetretaincount(__).md>) — Returns the reference count of a Core Foundation object.
- [CFMakeCollectable](cfmakecollectable.md) — Makes a newly-allocated Core Foundation object eligible for garbage collection.
- [CFRelease](cfrelease.md) — Releases a Core Foundation object.
