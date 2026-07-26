---
title: NSIntHashCallBacks
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.0+（10.5 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsinthashcallbacks
source_url: 'https://developer.apple.com/documentation/foundation/nsinthashcallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsinthashcallbacks.json'
content_hash: 'sha256:e3ecb1715a4c7469'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSIntHashCallBacks

<sub>Global Variable</sub>

For sets of pointer-sized quantities or smaller (for example, `int`, `long`, or `unichar`).

> [!warning] Deprecated
> Use `NSIntegerHashCallBacks` instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern const NSHashTableCallBacks NSIntHashCallBacks;
```

## See Also

### Constants

- [NSIntegerHashCallBacks](nsintegerhashcallbacks.md) — For sets of `NSInteger`-sized quantities or smaller (for example, `int`, `long`, or `unichar`).
- [NSNonOwnedPointerHashCallBacks](nsnonownedpointerhashcallbacks.md) — For sets of pointers, hashed by address.
- [NSNonRetainedObjectHashCallBacks](nsnonretainedobjecthashcallbacks.md) — For sets of objects, but without retaining/releasing.
- [NSObjectHashCallBacks](nsobjecthashcallbacks.md) — For sets of objects (similar to `NSSet`).
- [NSOwnedObjectIdentityHashCallBacks](nsownedobjectidentityhashcallbacks.md) — For sets of objects, with transfer of ownership upon insertion, using pointer equality.
- [NSOwnedPointerHashCallBacks](nsownedpointerhashcallbacks.md) — For sets of pointers, with transfer of ownership upon insertion.
- [NSPointerToStructHashCallBacks](nspointertostructhashcallbacks.md) — For sets of pointers to structs, when the first field of the struct is `int`-sized.
