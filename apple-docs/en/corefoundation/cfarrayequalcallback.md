---
title: CFArrayEqualCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfarrayequalcallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarrayequalcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarrayequalcallback.json'
content_hash: 'sha256:ece0fcb631fd8ff0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayEqualCallBack

<sub>Type Alias</sub>

Prototype of a callback function used to determine if two values in an array are equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFArrayEqualCallBack = (UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean
```

## Parameters

- `value1` — A value in an array to be compared with `value2` for equality.

- `value2` — A value in an array to be compared with `value1` for equality.

## Return Value

`true` if `value1` and `value2` are equal, `false` otherwise.

## Discussion

This callback is passed to [CFArrayCreate](<cfarraycreate(________).md>) in a [CFArrayCallBacks](cfarraycallbacks.md) structure.

## See Also

### Callbacks

- [CFArrayApplierFunction](cfarrayapplierfunction.md) — Prototype of a callback function that may be applied to every value in an array.
- [CFArrayCopyDescriptionCallBack](cfarraycopydescriptioncallback.md) — Prototype of a callback function used to get a description of a value in an array.
- [CFArrayReleaseCallBack](cfarrayreleasecallback.md) — Prototype of a callback function used to release a value before it’s removed from an array.
- [CFArrayRetainCallBack](cfarrayretaincallback.md) — Prototype of a callback function used to retain a value being added to an array.
