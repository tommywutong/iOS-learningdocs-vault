---
title: 'initWithReceivePort:sendPort:components:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.7 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsportcoder/initwithreceiveport:sendport:components:'
source_url: 'https://developer.apple.com/documentation/foundation/nsportcoder/initwithreceiveport:sendport:components:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsportcoder/initwithreceiveport%3Asendport%3Acomponents%3A.json'
content_hash: 'sha256:594a8ebcff4e0e9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPortCoder](../nsportcoder.md)

# initWithReceivePort:sendPort:components:

<sub>Instance Method</sub>

Initializes and returns an `NSPortCoder` object.

<sub>Mac Catalyst, macOS</sub>

```objc
- (id) initWithReceivePort:(NSPort *) rcvPort sendPort:(NSPort *) sndPort components:(NSArray *) comps;
```

## Parameters

- `rcvPort` — The receive port.

- `sndPort` — The send port.

- `comps` — An array containing an encoded distributed objects message.

## Discussion

Initializes a newly allocated `NSPortCoder` object connected to the communication ports `rcvPort` and `sndPort`, with an encoded distributed objects message stored in `comps`.

## See Also

### Related Documentation

- [dispatch](dispatch.md) — Processes and acts upon the distributed object message with which the receiver was initialized. _(deprecated)_

### Creating an NSPortCoder Object

- [portCoderWithReceivePort:sendPort:components:](portcoderwithreceiveport_sendport_components_.md) — Creates and returns a new `NSPortCoder` object. _(deprecated)_
