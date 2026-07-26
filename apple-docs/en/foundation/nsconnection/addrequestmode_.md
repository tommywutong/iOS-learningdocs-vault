---
title: 'addRequestMode:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsconnection/addrequestmode:'
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/addrequestmode:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/addrequestmode%3A.json'
content_hash: 'sha256:6ab36d1be97ea04b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# addRequestMode:

<sub>Instance Method</sub>

Adds `mode` to the set of run-loop input modes that the receiver uses for connection requests.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) addRequestMode:(NSString *) rmode;
```

## Parameters

- `rmode` — The mode to add to the receiver.

## Discussion

The default input mode is `NSDefaultRunLoopMode`. See the [RunLoop](../runloop.md) class specification for more information on input modes.

## See Also

### Related Documentation

- [- addPort:forMode:](<../runloop/add(__formode_)-6z982.md>) — Adds a port as an input source to the specified mode of the run loop.

### Configuring Instances

- [requestTimeout](requesttimeout.md) — The timeout interval for outgoing remote messages. _(deprecated)_
- [replyTimeout](replytimeout.md) — The timeout interval for replies to outgoing remote messages. _(deprecated)_
- [independentConversationQueueing](independentconversationqueueing.md) — A Boolean value that indicates whether the receiver handles remote messages atomically. _(deprecated)_
- [removeRequestMode:](removerequestmode_.md) — Removes `mode` from the set of run-loop input modes the receiver uses for connection requests. _(deprecated)_
- [requestModes](requestmodes-c.property.md) — The set of request modes the receiver’s receive port is registered for with its `NSRunLoop` object. _(deprecated)_
- [invalidate](invalidate.md) — Invalidates the receiver. _(deprecated)_
- [valid](valid.md) — A Boolean value that indicates whether the receiver is known to be valid. _(deprecated)_
