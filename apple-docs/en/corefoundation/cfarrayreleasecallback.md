---
title: CFArrayReleaseCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfarrayreleasecallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarrayreleasecallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarrayreleasecallback.json'
content_hash: 'sha256:162cad79946c0649'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayReleaseCallBack

<sub>Type Alias</sub>

Prototype of a callback function used to release a value before it’s removed from an array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFArrayReleaseCallBack = (CFAllocator?, UnsafeRawPointer?) -> Void
```

## Parameters

- `allocator` — The array’s allocator.

- `value` — The value being removed from an array.

## Discussion

This callback is passed to [CFArrayCreate](<cfarraycreate(________).md>) in a [CFArrayCallBacks](cfarraycallbacks.md) structure.

## See Also

### Callbacks

- [CFArrayApplierFunction](cfarrayapplierfunction.md) — Prototype of a callback function that may be applied to every value in an array.
- [CFArrayCopyDescriptionCallBack](cfarraycopydescriptioncallback.md) — Prototype of a callback function used to get a description of a value in an array.
- [CFArrayEqualCallBack](cfarrayequalcallback.md) — Prototype of a callback function used to determine if two values in an array are equal.
- [CFArrayRetainCallBack](cfarrayretaincallback.md) — Prototype of a callback function used to retain a value being added to an array.
