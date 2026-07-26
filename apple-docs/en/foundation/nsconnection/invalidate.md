---
title: invalidate
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsconnection/invalidate
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/invalidate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/invalidate.json'
content_hash: 'sha256:a3c0b9d9e06a6f98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# invalidate

<sub>Instance Method</sub>

Invalidates the receiver.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) invalidate;
```

## Discussion

After withdrawing the ports the receiver has registered with the current run loop, `invalidate` posts an [NSConnectionDidDieNotification](../nsconnectiondiddienotification.md) and then invalidates all remote objects and exported local proxies.

## See Also

### Related Documentation

- [- removePort:forMode:](<../runloop/remove(__formode_).md>) — Removes a port from the specified input mode of the run loop.

### Configuring Instances

- [requestTimeout](requesttimeout.md) — The timeout interval for outgoing remote messages. _(deprecated)_
- [replyTimeout](replytimeout.md) — The timeout interval for replies to outgoing remote messages. _(deprecated)_
- [independentConversationQueueing](independentconversationqueueing.md) — A Boolean value that indicates whether the receiver handles remote messages atomically. _(deprecated)_
- [addRequestMode:](addrequestmode_.md) — Adds `mode` to the set of run-loop input modes that the receiver uses for connection requests. _(deprecated)_
- [removeRequestMode:](removerequestmode_.md) — Removes `mode` from the set of run-loop input modes the receiver uses for connection requests. _(deprecated)_
- [requestModes](requestmodes-c.property.md) — The set of request modes the receiver’s receive port is registered for with its `NSRunLoop` object. _(deprecated)_
- [valid](valid.md) — A Boolean value that indicates whether the receiver is known to be valid. _(deprecated)_
