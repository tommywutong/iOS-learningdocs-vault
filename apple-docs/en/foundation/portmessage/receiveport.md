---
title: receivePort
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/portmessage/receiveport
source_url: 'https://developer.apple.com/documentation/foundation/portmessage/receiveport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/portmessage/receiveport.json'
content_hash: 'sha256:4dded3631a1b7591'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PortMessage](../portmessage.md)

# receivePort

<sub>Instance Property</sub>

For an outgoing message, returns the port on which replies to the receiver will arrive. For an incoming message, returns the port the receiver did arrive on.

<sub>Mac Catalyst, macOS</sub>

```swift
var receivePort: Port? { get }
```

## Return Value

For an outgoing message, the port on which replies to the receiver will arrive. For an incoming message, the port the receiver did arrive on.

## See Also

### Getting the Ports

- [sendPort](sendport.md) — For an outgoing message, returns the port the receiver will send itself through. For an incoming message, returns the port replies to the receiver should be sent through.
