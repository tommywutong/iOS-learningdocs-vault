---
title: CFTreeCopyDescriptionCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cftreecopydescriptioncallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cftreecopydescriptioncallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftreecopydescriptioncallback.json'
content_hash: 'sha256:ef24333a4964cf05'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTreeCopyDescriptionCallBack

<sub>Type Alias</sub>

Callback function used to provide a description of the program-defined information pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFTreeCopyDescriptionCallBack = (UnsafeRawPointer?) -> Unmanaged<CFString>?
```

## Parameters

- `info` — The program-supplied information pointer provided in a [CFTreeContext](cftreecontext.md) structure.

## Return Value

A textual description of `info`. The caller is responsible for releasing this object.

## See Also

### Callbacks

- [CFTreeApplierFunction](cftreeapplierfunction.md) — Type of the callback function used by the CFTree apply function.
- [CFTreeReleaseCallBack](cftreereleasecallback.md) — Callback function used to release a previously retained program-defined information pointer.
- [CFTreeRetainCallBack](cftreeretaincallback.md) — Callback function used to retain a program-defined information pointer.
