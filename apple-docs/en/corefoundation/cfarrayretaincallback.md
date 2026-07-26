---
title: CFArrayRetainCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfarrayretaincallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarrayretaincallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarrayretaincallback.json'
content_hash: 'sha256:d169478723fd4dcf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayRetainCallBack

<sub>Type Alias</sub>

Prototype of a callback function used to retain a value being added to an array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFArrayRetainCallBack = (CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?
```

## Parameters

- `allocator` — The array’s allocator.

- `value` — The value being added to an array.

## Return Value

The value to store in an array, which is usually the `value` parameter passed to this callback, but may be a different   value if a different value should be stored in an array.

## Discussion

This callback is passed to [CFArrayCreate](<cfarraycreate(________).md>) in a [CFArrayCallBacks](cfarraycallbacks.md) structure.

## See Also

### Callbacks

- [CFArrayApplierFunction](cfarrayapplierfunction.md) — Prototype of a callback function that may be applied to every value in an array.
- [CFArrayCopyDescriptionCallBack](cfarraycopydescriptioncallback.md) — Prototype of a callback function used to get a description of a value in an array.
- [CFArrayEqualCallBack](cfarrayequalcallback.md) — Prototype of a callback function used to determine if two values in an array are equal.
- [CFArrayReleaseCallBack](cfarrayreleasecallback.md) — Prototype of a callback function used to release a value before it’s removed from an array.
