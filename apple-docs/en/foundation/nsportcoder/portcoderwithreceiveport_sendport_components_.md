---
title: 'portCoderWithReceivePort:sendPort:components:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.7 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsportcoder/portcoderwithreceiveport:sendport:components:'
source_url: 'https://developer.apple.com/documentation/foundation/nsportcoder/portcoderwithreceiveport:sendport:components:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsportcoder/portcoderwithreceiveport%3Asendport%3Acomponents%3A.json'
content_hash: 'sha256:d5d32204d66ee099'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPortCoder](../nsportcoder.md)

# portCoderWithReceivePort:sendPort:components:

<sub>Type Method</sub>

Creates and returns a new `NSPortCoder` object.

<sub>Mac Catalyst, macOS</sub>

```objc
+ (id) portCoderWithReceivePort:(NSPort *) rcvPort sendPort:(NSPort *) sndPort components:(NSArray *) comps;
```

## Parameters

- `rcvPort` — The receiver port.

- `sndPort` — The send port.

- `comps` — An array containing an encoded distributed objects message.

## Return Value

A new `NSPortCoder` object connected to the communication ports `rcvPort` and `sndPort`, with an encoded distributed objects message stored in `comps`.

## See Also

### Related Documentation

- [dispatch](dispatch.md) — Processes and acts upon the distributed object message with which the receiver was initialized. _(deprecated)_
- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)

### Creating an NSPortCoder Object

- [initWithReceivePort:sendPort:components:](initwithreceiveport_sendport_components_.md) — Initializes and returns an `NSPortCoder` object. _(deprecated)_
