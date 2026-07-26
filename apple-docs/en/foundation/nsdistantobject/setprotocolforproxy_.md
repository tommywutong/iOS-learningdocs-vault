---
title: 'setProtocolForProxy:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsdistantobject/setprotocolforproxy:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdistantobject/setprotocolforproxy:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdistantobject/setprotocolforproxy%3A.json'
content_hash: 'sha256:4be3bac9c3e2627a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDistantObject](../nsdistantobject.md)

# setProtocolForProxy:

<sub>Instance Method</sub>

Sets the methods known to be handled by the receiver to those in a given protocol.

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) setProtocolForProxy:(Protocol *) proto;
```

## Parameters

- `proto` — The protocol for the receiver.

## Discussion

Setting a protocol for a remote proxy reduces network traffic needed to determine method argument and return types.

In order to encode a message’s arguments for transmission over the network, the types of those arguments must be known in advance. When they’re not known, the distributed objects system must send an initial message just to get those types, doubling the network traffic for every new message sent. Setting a protocol alleviates this need for methods defined by the protocol. You can still send messages that aren’t declared in `proto`—in this case the initial message is sent to determine the types, and then the real message is sent.
