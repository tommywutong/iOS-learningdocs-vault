---
title: 'connectionWithReceivePort:sendPort:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsconnection/connectionwithreceiveport:sendport:'
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection/connectionwithreceiveport:sendport:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection/connectionwithreceiveport%3Asendport%3A.json'
content_hash: 'sha256:444ee9a61d8790e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSConnection](../nsconnection.md)

# connectionWithReceivePort:sendPort:

<sub>Type Method</sub>

Returns an `NSConnection` object that communicates using given send and receive ports.

<sub>Mac Catalyst, macOS</sub>

```objc
+ (instancetype) connectionWithReceivePort:(NSPort *) receivePort sendPort:(NSPort *) sendPort;
```

## Parameters

- `receivePort` — A receive port.

- `sendPort` — A send port.

## Return Value

An `NSConnection` object that communicates using `receivePort` and `sendPort`.

## Discussion

See [initWithReceivePort:sendPort:](initwithreceiveport_sendport_.md) for more information.

## See Also

### Related Documentation

- [defaultConnection](defaultconnection.md) — Returns the default `NSConnection` object for the current thread. _(deprecated)_

### Creating Instances

- [initWithReceivePort:sendPort:](initwithreceiveport_sendport_.md) — Returns an `NSConnection` object initialized with given send and receive ports. _(deprecated)_
