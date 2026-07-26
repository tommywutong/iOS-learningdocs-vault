---
title: 'dispatchWithComponents:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsconnection/dispatchwithcomponents:'
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/dispatchwithcomponents:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/dispatchwithcomponents%3A.json'
content_hash: 'sha256:6438ac1503a8bdbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# dispatchWithComponents:

<sub>Instance Method</sub>

Allows subclasses to ask a connection object to dispatch component data.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) dispatchWithComponents:(NSArray *) components;
```

## Parameters

- `components` — Distributed Objects component data.

## Discussion

[Port](../port.md) subclasses should use this method to ask a connection object to dispatch Distributed Objects component data received over the wire. This will decode the data, authenticate, and send the message.

## See Also

### Getting Ports

- [receivePort](receiveport-c.property.md) — The port on which the receiver receives incoming network messages. _(deprecated)_
- [sendPort](sendport-c.property.md) — The port that the connection sends outgoing network messages through. _(deprecated)_
