---
title: msgid
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/portmessage/msgid
source_url: 'https://developer.apple.com/documentation/foundation/portmessage/msgid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/portmessage/msgid.json'
content_hash: 'sha256:37265095aa17389d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PortMessage](../portmessage.md)

# msgid

<sub>Instance Property</sub>

Returns the identifier for the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
var msgid: UInt32 { get set }
```

## Return Value

The identifier for the receiver.

## Discussion

Cooperating applications can use this to define different types of messages, such as connection requests, RPCs, errors, and so on.
