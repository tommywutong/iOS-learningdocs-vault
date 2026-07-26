---
title: requestModes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsconnection/requestmodes-c.property
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/requestmodes-c.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/requestmodes-c.property.json'
content_hash: 'sha256:7d6a935a256d2f84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# requestModes

<sub>Instance Property</sub>

The set of request modes the receiver’s receive port is registered for with its `NSRunLoop` object.

<sub>Mac Catalyst, macOS</sub>

```objc
@property (copy, readonly) NSArray<NSString *> * requestModes;
```

## Discussion

An array of `NSString` objects that represents the set of request modes the receiver’s receive port is registered for with its [RunLoop](../runloop.md) object.

## See Also

### Related Documentation

- [- addPort:forMode:](<../runloop/add(__formode_)-6z982.md>) — Adds a port as an input source to the specified mode of the run loop.

### Configuring Instances

- [requestTimeout](requesttimeout.md) — The timeout interval for outgoing remote messages. _(deprecated)_
- [replyTimeout](replytimeout.md) — The timeout interval for replies to outgoing remote messages. _(deprecated)_
- [independentConversationQueueing](independentconversationqueueing.md) — A Boolean value that indicates whether the receiver handles remote messages atomically. _(deprecated)_
- [addRequestMode:](addrequestmode_.md) — Adds `mode` to the set of run-loop input modes that the receiver uses for connection requests. _(deprecated)_
- [removeRequestMode:](removerequestmode_.md) — Removes `mode` from the set of run-loop input modes the receiver uses for connection requests. _(deprecated)_
- [invalidate](invalidate.md) — Invalidates the receiver. _(deprecated)_
- [valid](valid.md) — A Boolean value that indicates whether the receiver is known to be valid. _(deprecated)_
