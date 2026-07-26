---
title: CFMessagePortInvalidationCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfmessageportinvalidationcallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmessageportinvalidationcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmessageportinvalidationcallback.json'
content_hash: 'sha256:c2f3da0ab5a178f8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMessagePortInvalidationCallBack

<sub>Type Alias</sub>

Callback invoked when a CFMessagePort object is invalidated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFMessagePortInvalidationCallBack = (CFMessagePort?, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `ms` — The message port that has been invalidated.

- `info` — The `info` member of the [CFMessagePortContext](cfmessageportcontext.md) structure that was used when creating `ms`, if `ms` is a local port; `NULL` if `ms` is a remote port.

## Discussion

Your callback should free any resources allocated for `ms`.

You specify this callback with [CFMessagePortSetInvalidationCallBack](<cfmessageportsetinvalidationcallback(____).md>).

## See Also

### Callbacks

- [CFMessagePortCallBack](cfmessageportcallback.md) — Callback invoked to process a message received on a CFMessagePort object.
