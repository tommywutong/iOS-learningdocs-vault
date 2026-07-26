---
title: replyTimeout
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsconnection/replytimeout
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/replytimeout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/replytimeout.json'
content_hash: 'sha256:4c8bcc69d2f66289'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# replyTimeout

<sub>Instance Property</sub>

The timeout interval for replies to outgoing remote messages.

<sub>Mac Catalyst, macOS</sub>

```objc
@property NSTimeInterval replyTimeout;
```

## Discussion

If a non-oneway remote message is sent and no reply is received by the timeout, an [NSPortTimeoutException](../nsexceptionname/porttimeoutexception.md) is raised. The default timeout is the maximum possible value.

## See Also

### Configuring Instances

- [requestTimeout](requesttimeout.md) — The timeout interval for outgoing remote messages. _(deprecated)_
- [independentConversationQueueing](independentconversationqueueing.md) — A Boolean value that indicates whether the receiver handles remote messages atomically. _(deprecated)_
- [addRequestMode:](addrequestmode_.md) — Adds `mode` to the set of run-loop input modes that the receiver uses for connection requests. _(deprecated)_
- [removeRequestMode:](removerequestmode_.md) — Removes `mode` from the set of run-loop input modes the receiver uses for connection requests. _(deprecated)_
- [requestModes](requestmodes-c.property.md) — The set of request modes the receiver’s receive port is registered for with its `NSRunLoop` object. _(deprecated)_
- [invalidate](invalidate.md) — Invalidates the receiver. _(deprecated)_
- [valid](valid.md) — A Boolean value that indicates whether the receiver is known to be valid. _(deprecated)_
