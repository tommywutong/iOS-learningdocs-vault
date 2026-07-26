---
title: CFSetHashCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfsethashcallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsethashcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsethashcallback.json'
content_hash: 'sha256:ab66d224ebc46142'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSetHashCallBack

<sub>Type Alias</sub>

Prototype of a callback function called to compute a hash code for a value. Hash codes are used when values are accessed, added, or removed from a collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFSetHashCallBack = (UnsafeRawPointer?) -> CFHashCode
```

## Parameters

- `value` — The value used to compute the hash code.

## Return Value

An integer that can be used as a table address in a hash table structure.

## Discussion

This callback is passed to [CFSetCreate](<cfsetcreate(________).md>) in a [CFSetCallBacks](cfsetcallbacks.md) structure.

## See Also

### Callbacks

- [CFSetApplierFunction](cfsetapplierfunction.md) — Prototype of a callback function that may be applied to every value in a set.
- [CFSetCopyDescriptionCallBack](cfsetcopydescriptioncallback.md) — Prototype of a callback function used to get a description of a value in a set.
- [CFSetEqualCallBack](cfsetequalcallback.md) — Prototype of a callback function used to determine if two values in a set are equal.
- [CFSetReleaseCallBack](cfsetreleasecallback.md) — Prototype of a callback function used to release a value before it’s removed from a set.
- [CFSetRetainCallBack](cfsetretaincallback.md) — Prototype of a callback function used to retain a value being added to a set.
