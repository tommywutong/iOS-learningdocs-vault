---
title: CFSetEqualCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfsetequalcallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsetequalcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsetequalcallback.json'
content_hash: 'sha256:85b1b42ac1390f55'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSetEqualCallBack

<sub>Type Alias</sub>

Prototype of a callback function used to determine if two values in a set are equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFSetEqualCallBack = (UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean
```

## Parameters

- `value1` — A value in the set.

- `value2` — Another value in the set.

## Return Value

`true` if `value1` and `value2` are equal, `false` otherwise.

## Discussion

This callback is passed to [CFSetCreate](<cfsetcreate(________).md>) in a [CFSetCallBacks](cfsetcallbacks.md) structure.

## See Also

### Callbacks

- [CFSetApplierFunction](cfsetapplierfunction.md) — Prototype of a callback function that may be applied to every value in a set.
- [CFSetCopyDescriptionCallBack](cfsetcopydescriptioncallback.md) — Prototype of a callback function used to get a description of a value in a set.
- [CFSetHashCallBack](cfsethashcallback.md) — Prototype of a callback function called to compute a hash code for a value. Hash codes are used when values are accessed, added, or removed from a collection.
- [CFSetReleaseCallBack](cfsetreleasecallback.md) — Prototype of a callback function used to release a value before it’s removed from a set.
- [CFSetRetainCallBack](cfsetretaincallback.md) — Prototype of a callback function used to retain a value being added to a set.
