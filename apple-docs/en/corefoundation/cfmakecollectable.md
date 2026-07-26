---
title: CFMakeCollectable
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfmakecollectable
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmakecollectable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmakecollectable.json'
content_hash: 'sha256:6f6d68971da04ddb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMakeCollectable

<sub>Function</sub>

Makes a newly-allocated Core Foundation object eligible for garbage collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CFTypeRefCFMakeCollectable(CFTypeRef cf);
```

## Parameters

- `cf` — A CFType object to make collectable. This value must not be `NULL`.

## Return Value

`cf`.

## Discussion

For more details, see Garbage Collection Programming Guide.

### Special Considerations

If `cf` is `NULL`, this will cause a runtime error and your application will crash.

## See Also

### Memory Management

- [CFGetAllocator](<cfgetallocator(__).md>) — Returns the allocator used to allocate a Core Foundation object.
- [CFGetRetainCount](<cfgetretaincount(__).md>) — Returns the reference count of a Core Foundation object.
- [CFRelease](cfrelease.md) — Releases a Core Foundation object.
- [CFRetain](cfretain.md) — Retains a Core Foundation object.
