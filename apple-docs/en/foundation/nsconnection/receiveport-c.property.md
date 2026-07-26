---
title: receivePort
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsconnection/receiveport-c.property
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/receiveport-c.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/receiveport-c.property.json'
content_hash: 'sha256:c25eb2efe023cec8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# receivePort

<sub>Instance Property</sub>

The port on which the receiver receives incoming network messages.

<sub>Mac Catalyst, macOS</sub>

```objc
@property (retain, readonly) NSPort * receivePort;
```

## Discussion

You can inspect this object for debugging purposes or use it to create another `NSConnection` object, but shouldn’t use it to send or receive messages explicitly. Don’t set the delegate of the receive port; it already has a delegate established by the `NSConnection` object.

## See Also

### Related Documentation

- [initWithReceivePort:sendPort:](initwithreceiveport_sendport_.md) — Returns an `NSConnection` object initialized with given send and receive ports. _(deprecated)_

### Getting Ports

- [sendPort](sendport-c.property.md) — The port that the connection sends outgoing network messages through. _(deprecated)_
- [dispatchWithComponents:](dispatchwithcomponents_.md) — Allows subclasses to ask a connection object to dispatch component data. _(deprecated)_
