---
title: 'removeRequestMode:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsconnection/removerequestmode:'
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/removerequestmode:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/removerequestmode%3A.json'
content_hash: 'sha256:d729eace8d473dbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# removeRequestMode:

<sub>Instance Method</sub>

Removes `mode` from the set of run-loop input modes the receiver uses for connection requests.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) removeRequestMode:(NSString *) rmode;
```

## Parameters

- `rmode` — The mode to remove from the set of run-loop input modes the receiver uses for connection requests.

## See Also

### Related Documentation

- [- removePort:forMode:](<../runloop/remove(__formode_).md>) — Removes a port from the specified input mode of the run loop.

### Configuring Instances

- [requestTimeout](requesttimeout.md) — The timeout interval for outgoing remote messages. _(deprecated)_
- [replyTimeout](replytimeout.md) — The timeout interval for replies to outgoing remote messages. _(deprecated)_
- [independentConversationQueueing](independentconversationqueueing.md) — A Boolean value that indicates whether the receiver handles remote messages atomically. _(deprecated)_
- [addRequestMode:](addrequestmode_.md) — Adds `mode` to the set of run-loop input modes that the receiver uses for connection requests. _(deprecated)_
- [requestModes](requestmodes-c.property.md) — The set of request modes the receiver’s receive port is registered for with its `NSRunLoop` object. _(deprecated)_
- [invalidate](invalidate.md) — Invalidates the receiver. _(deprecated)_
- [valid](valid.md) — A Boolean value that indicates whether the receiver is known to be valid. _(deprecated)_
