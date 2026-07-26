---
title: CFSetCopyDescriptionCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfsetcopydescriptioncallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsetcopydescriptioncallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsetcopydescriptioncallback.json'
content_hash: 'sha256:b3176c488d495a61'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSetCopyDescriptionCallBack

<sub>Type Alias</sub>

Prototype of a callback function used to get a description of a value in a set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFSetCopyDescriptionCallBack = (UnsafeRawPointer?) -> Unmanaged<CFString>?
```

## Parameters

- `value` — The value to be described.

## Return Value

A textual description of `value`. The caller is responsible for releasing this object.

## Discussion

This callback is passed to [CFSetCreate](<cfsetcreate(________).md>) in a [CFSetCallBacks](cfsetcallbacks.md) structure. This callback is used by the [CFCopyDescription](<cfcopydescription(__).md>) function.

## See Also

### Callbacks

- [CFSetApplierFunction](cfsetapplierfunction.md) — Prototype of a callback function that may be applied to every value in a set.
- [CFSetEqualCallBack](cfsetequalcallback.md) — Prototype of a callback function used to determine if two values in a set are equal.
- [CFSetHashCallBack](cfsethashcallback.md) — Prototype of a callback function called to compute a hash code for a value. Hash codes are used when values are accessed, added, or removed from a collection.
- [CFSetReleaseCallBack](cfsetreleasecallback.md) — Prototype of a callback function used to release a value before it’s removed from a set.
- [CFSetRetainCallBack](cfsetretaincallback.md) — Prototype of a callback function used to retain a value being added to a set.
