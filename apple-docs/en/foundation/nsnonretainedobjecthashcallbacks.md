---
title: NSNonRetainedObjectHashCallBacks
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnonretainedobjecthashcallbacks
source_url: 'https://developer.apple.com/documentation/foundation/nsnonretainedobjecthashcallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnonretainedobjecthashcallbacks.json'
content_hash: 'sha256:114f5a250399ce00'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSNonRetainedObjectHashCallBacks

<sub>Global Variable</sub>

For sets of objects, but without retaining/releasing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSNonRetainedObjectHashCallBacks: NSHashTableCallBacks
```

## See Also

### Constants

- [NSIntegerHashCallBacks](nsintegerhashcallbacks.md) — For sets of `NSInteger`-sized quantities or smaller (for example, `int`, `long`, or `unichar`).
- [NSNonOwnedPointerHashCallBacks](nsnonownedpointerhashcallbacks.md) — For sets of pointers, hashed by address.
- [NSObjectHashCallBacks](nsobjecthashcallbacks.md) — For sets of objects (similar to `NSSet`).
- [NSOwnedObjectIdentityHashCallBacks](nsownedobjectidentityhashcallbacks.md) — For sets of objects, with transfer of ownership upon insertion, using pointer equality.
- [NSOwnedPointerHashCallBacks](nsownedpointerhashcallbacks.md) — For sets of pointers, with transfer of ownership upon insertion.
- [NSPointerToStructHashCallBacks](nspointertostructhashcallbacks.md) — For sets of pointers to structs, when the first field of the struct is `int`-sized.
