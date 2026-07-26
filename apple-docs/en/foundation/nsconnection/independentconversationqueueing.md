---
title: independentConversationQueueing
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsconnection/independentconversationqueueing
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/independentconversationqueueing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/independentconversationqueueing.json'
content_hash: 'sha256:4c447198f9a67ba8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# independentConversationQueueing

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver handles remote messages atomically.

<sub>Mac Catalyst, macOS</sub>

```objc
@property BOOL independentConversationQueueing;
```

## Discussion

[true](../../swift/true.md) if the receiver handles remote messages atomically, otherwise [false](../../swift/false.md).

The default is [false](../../swift/false.md). An `NSConnection` object normally forwards remote message to the intended recipients as they come in. See [Configuring a Connection](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/Tasks/configuring.html#//apple_ref/doc/uid/20000766) for more information.

## See Also

### Configuring Instances

- [requestTimeout](requesttimeout.md) — The timeout interval for outgoing remote messages. _(deprecated)_
- [replyTimeout](replytimeout.md) — The timeout interval for replies to outgoing remote messages. _(deprecated)_
- [addRequestMode:](addrequestmode_.md) — Adds `mode` to the set of run-loop input modes that the receiver uses for connection requests. _(deprecated)_
- [removeRequestMode:](removerequestmode_.md) — Removes `mode` from the set of run-loop input modes the receiver uses for connection requests. _(deprecated)_
- [requestModes](requestmodes-c.property.md) — The set of request modes the receiver’s receive port is registered for with its `NSRunLoop` object. _(deprecated)_
- [invalidate](invalidate.md) — Invalidates the receiver. _(deprecated)_
- [valid](valid.md) — A Boolean value that indicates whether the receiver is known to be valid. _(deprecated)_
