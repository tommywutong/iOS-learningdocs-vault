---
title: CFTreeApplierFunction
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cftreeapplierfunction
source_url: 'https://developer.apple.com/documentation/corefoundation/cftreeapplierfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftreeapplierfunction.json'
content_hash: 'sha256:3620568385f3e7c9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFTreeApplierFunction

<sub>Type Alias</sub>

Type of the callback function used by the CFTree apply function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFTreeApplierFunction = (UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `value` — The current child of a tree that is being iterated.

- `context` — The program-defined context parameter that was passed to the applier function.

## Discussion

This callback is used by the [CFTreeApplyFunctionToChildren](<cftreeapplyfunctiontochildren(______).md>) applier function.

## See Also

### Callbacks

- [CFTreeCopyDescriptionCallBack](cftreecopydescriptioncallback.md) — Callback function used to provide a description of the program-defined information pointer.
- [CFTreeReleaseCallBack](cftreereleasecallback.md) — Callback function used to release a previously retained program-defined information pointer.
- [CFTreeRetainCallBack](cftreeretaincallback.md) — Callback function used to retain a program-defined information pointer.
