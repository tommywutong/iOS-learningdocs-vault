---
title: NSIntegerHashCallBacks
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsintegerhashcallbacks
source_url: 'https://developer.apple.com/documentation/foundation/nsintegerhashcallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsintegerhashcallbacks.json'
content_hash: 'sha256:144b9140477c8b7e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSIntegerHashCallBacks

<sub>Global Variable</sub>

For sets of `NSInteger`-sized quantities or smaller (for example, `int`, `long`, or `unichar`).

<sub>macOS</sub>

```swift
let NSIntegerHashCallBacks: NSHashTableCallBacks
```

## See Also

### Constants

- [NSNonOwnedPointerHashCallBacks](nsnonownedpointerhashcallbacks.md) — For sets of pointers, hashed by address.
- [NSNonRetainedObjectHashCallBacks](nsnonretainedobjecthashcallbacks.md) — For sets of objects, but without retaining/releasing.
- [NSObjectHashCallBacks](nsobjecthashcallbacks.md) — For sets of objects (similar to `NSSet`).
- [NSOwnedObjectIdentityHashCallBacks](nsownedobjectidentityhashcallbacks.md) — For sets of objects, with transfer of ownership upon insertion, using pointer equality.
- [NSOwnedPointerHashCallBacks](nsownedpointerhashcallbacks.md) — For sets of pointers, with transfer of ownership upon insertion.
- [NSPointerToStructHashCallBacks](nspointertostructhashcallbacks.md) — For sets of pointers to structs, when the first field of the struct is `int`-sized.
