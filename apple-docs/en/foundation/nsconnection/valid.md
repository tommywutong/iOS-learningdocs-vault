---
title: valid
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsconnection/valid
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/valid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/valid.json'
content_hash: 'sha256:6765c7760de575b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# valid

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver is known to be valid.

<sub>Mac Catalyst, macOS</sub>

```objc
@property (readonly, getter=isValid) BOOL valid;
```

## Discussion

[true](../../swift/true.md) if the receiver is known to be valid, otherwise [false](../../swift/false.md).

An `NSConnection` object becomes invalid when either of its ports becomes invalid, but only notes that it has become invalid when it tries to send or receive a message. When this happens it posts an [NSConnectionDidDieNotification](../nsconnectiondiddienotification.md) to the default notification center.

## See Also

### Related Documentation

- [valid](../port/isvalid.md) — A Boolean value that indicates whether the receiver is valid.

### Configuring Instances

- [requestTimeout](requesttimeout.md) — The timeout interval for outgoing remote messages. _(deprecated)_
- [replyTimeout](replytimeout.md) — The timeout interval for replies to outgoing remote messages. _(deprecated)_
- [independentConversationQueueing](independentconversationqueueing.md) — A Boolean value that indicates whether the receiver handles remote messages atomically. _(deprecated)_
- [addRequestMode:](addrequestmode_.md) — Adds `mode` to the set of run-loop input modes that the receiver uses for connection requests. _(deprecated)_
- [removeRequestMode:](removerequestmode_.md) — Removes `mode` from the set of run-loop input modes the receiver uses for connection requests. _(deprecated)_
- [requestModes](requestmodes-c.property.md) — The set of request modes the receiver’s receive port is registered for with its `NSRunLoop` object. _(deprecated)_
- [invalidate](invalidate.md) — Invalidates the receiver. _(deprecated)_
