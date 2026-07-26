---
title: CFTreeRetainCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cftreeretaincallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cftreeretaincallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftreeretaincallback.json'
content_hash: 'sha256:8646a1c6581e7718'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTreeRetainCallBack

<sub>Type Alias</sub>

Callback function used to retain a program-defined information pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFTreeRetainCallBack = (UnsafeRawPointer?) -> UnsafeRawPointer?
```

## Parameters

- `info` — The program-supplied information pointer provided in a [CFTreeContext](cftreecontext.md) structure.

## Return Value

The value to use whenever the information pointer is retained, which is usually the `info` parameter passed to this callback, but may be a different value if a different value should be used.

## See Also

### Callbacks

- [CFTreeApplierFunction](cftreeapplierfunction.md) — Type of the callback function used by the CFTree apply function.
- [CFTreeCopyDescriptionCallBack](cftreecopydescriptioncallback.md) — Callback function used to provide a description of the program-defined information pointer.
- [CFTreeReleaseCallBack](cftreereleasecallback.md) — Callback function used to release a previously retained program-defined information pointer.
