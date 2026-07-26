---
title: sendPort
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/portmessage/sendport
source_url: 'https://developer.apple.com/documentation/foundation/portmessage/sendport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/portmessage/sendport.json'
content_hash: 'sha256:a484f09dc932e7ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PortMessage](../portmessage.md)

# sendPort

<sub>Instance Property</sub>

For an outgoing message, returns the port the receiver will send itself through. For an incoming message, returns the port replies to the receiver should be sent through.

<sub>Mac Catalyst, macOS</sub>

```swift
var sendPort: Port? { get }
```

## Return Value

For an outgoing message, the port the receiver will send itself through when it receives a [- sendBeforeDate:](<send(before_).md>) message. For an incoming message, the port replies to the receiver should be sent through.

## See Also

### Getting the Ports

- [receivePort](receiveport.md) — For an outgoing message, returns the port on which replies to the receiver will arrive. For an incoming message, returns the port the receiver did arrive on.
