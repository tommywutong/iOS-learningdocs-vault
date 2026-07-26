---
title: CFArrayCopyDescriptionCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfarraycopydescriptioncallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarraycopydescriptioncallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarraycopydescriptioncallback.json'
content_hash: 'sha256:afdb5a5738c39f4a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayCopyDescriptionCallBack

<sub>Type Alias</sub>

Prototype of a callback function used to get a description of a value in an array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFArrayCopyDescriptionCallBack = (UnsafeRawPointer?) -> Unmanaged<CFString>?
```

## Parameters

- `value` — The value to be described.

## Return Value

A textual description of `value`. The caller is responsible for releasing this object.

## Discussion

This callback is passed to [CFArrayCreate](<cfarraycreate(________).md>) in a [CFArrayCallBacks](cfarraycallbacks.md) structure. This callback is used by the [CFCopyDescription](<cfcopydescription(__).md>) function.

## See Also

### Callbacks

- [CFArrayApplierFunction](cfarrayapplierfunction.md) — Prototype of a callback function that may be applied to every value in an array.
- [CFArrayEqualCallBack](cfarrayequalcallback.md) — Prototype of a callback function used to determine if two values in an array are equal.
- [CFArrayReleaseCallBack](cfarrayreleasecallback.md) — Prototype of a callback function used to release a value before it’s removed from an array.
- [CFArrayRetainCallBack](cfarrayretaincallback.md) — Prototype of a callback function used to retain a value being added to an array.
