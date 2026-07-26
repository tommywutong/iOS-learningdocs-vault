---
title: remoteEndpoint
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnectiongroup/message/remoteendpoint
source_url: 'https://developer.apple.com/documentation/network/nwconnectiongroup/message/remoteendpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnectiongroup/message/remoteendpoint.json'
content_hash: 'sha256:0f1df5012fc0abc2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWConnectionGroup](../../nwconnectiongroup.md) · [Message](../message.md)

# remoteEndpoint

<sub>Instance Property</sub>

The endpoint that originates the message you receive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var remoteEndpoint: NWEndpoint? { get }
```

## See Also

### Inspecting Received Messages

- [localEndpoint](localendpoint.md) — The local address and port you use to receive the message.
- [path](path.md) — The network path on which you receive the message.
