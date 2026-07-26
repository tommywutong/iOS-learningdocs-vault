---
title: CFMessagePortCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfmessageportcallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmessageportcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmessageportcallback.json'
content_hash: 'sha256:9ebd9b0cc53bd244'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMessagePortCallBack

<sub>Type Alias</sub>

Callback invoked to process a message received on a CFMessagePort object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFMessagePortCallBack = (CFMessagePort?, Int32, CFData?, UnsafeMutableRawPointer?) -> Unmanaged<CFData>?
```

## Parameters

- `local` — The local message port that received the message.

- `msgid` — An arbitrary integer value assigned to the message by the sender.

- `data` — The message data.

- `info` — The `info` member of the [CFMessagePortContext](cfmessageportcontext.md) structure that was used when creating `local`.

## Return Value

Data to send back to the sender of the message. The system releases the returned CFData object. Return `NULL` if you want an empty reply returned to the sender.

## Discussion

If you want the message data to persist beyond this callback, you must explicitly create a copy of `data` rather than merely retain it; the contents of `data` will be deallocated after the callback exits.

## See Also

### Callbacks

- [CFMessagePortInvalidationCallBack](cfmessageportinvalidationcallback.md) — Callback invoked when a CFMessagePort object is invalidated.
