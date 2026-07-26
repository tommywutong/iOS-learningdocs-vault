---
title: CFMachPortInvalidationCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfmachportinvalidationcallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmachportinvalidationcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmachportinvalidationcallback.json'
content_hash: 'sha256:029823a167c17cce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMachPortInvalidationCallBack

<sub>Type Alias</sub>

Callback invoked when a CFMachPort object is invalidated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFMachPortInvalidationCallBack = (CFMachPort?, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `port` — The CFMachPort object that has been invalidated.

- `info` — The `info` member of the [CFMachPortContext](cfmachportcontext.md) structure used when creating `port`.

## Discussion

Your callback should free any resources allocated for `port`.

You specify this callback with [CFMachPortSetInvalidationCallBack](<cfmachportsetinvalidationcallback(____).md>).

## See Also

### Callbacks

- [CFMachPortCallBack](cfmachportcallback.md) — Callback invoked to process a message received on a CFMachPort object.
