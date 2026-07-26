---
title: CFTreeReleaseCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cftreereleasecallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cftreereleasecallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftreereleasecallback.json'
content_hash: 'sha256:fc8223c09a63f6eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTreeReleaseCallBack

<sub>Type Alias</sub>

Callback function used to release a previously retained program-defined information pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFTreeReleaseCallBack = (UnsafeRawPointer?) -> Void
```

## Parameters

- `info` — The program-supplied information pointer provided in a [CFTreeContext](cftreecontext.md) structure.

## See Also

### Callbacks

- [CFTreeApplierFunction](cftreeapplierfunction.md) — Type of the callback function used by the CFTree apply function.
- [CFTreeCopyDescriptionCallBack](cftreecopydescriptioncallback.md) — Callback function used to provide a description of the program-defined information pointer.
- [CFTreeRetainCallBack](cftreeretaincallback.md) — Callback function used to retain a program-defined information pointer.
