---
title: CFSetRetainCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfsetretaincallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsetretaincallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsetretaincallback.json'
content_hash: 'sha256:c84d06d727261e47'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSetRetainCallBack

<sub>Type Alias</sub>

Prototype of a callback function used to retain a value being added to a set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFSetRetainCallBack = (CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?
```

## Parameters

- `allocator` — The set’s allocator.

- `value` — The value being added to the set.

## Return Value

The value to store in the set, which is usually the `value` parameter passed to this callback, but may be a different   value if a different value should be stored in the collection.

## Discussion

This callback is passed to [CFSetCreate](<cfsetcreate(________).md>) in a [CFSetCallBacks](cfsetcallbacks.md) structure.

## See Also

### Callbacks

- [CFSetApplierFunction](cfsetapplierfunction.md) — Prototype of a callback function that may be applied to every value in a set.
- [CFSetCopyDescriptionCallBack](cfsetcopydescriptioncallback.md) — Prototype of a callback function used to get a description of a value in a set.
- [CFSetEqualCallBack](cfsetequalcallback.md) — Prototype of a callback function used to determine if two values in a set are equal.
- [CFSetHashCallBack](cfsethashcallback.md) — Prototype of a callback function called to compute a hash code for a value. Hash codes are used when values are accessed, added, or removed from a collection.
- [CFSetReleaseCallBack](cfsetreleasecallback.md) — Prototype of a callback function used to release a value before it’s removed from a set.
