---
title: path
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnectiongroup/message/path
source_url: 'https://developer.apple.com/documentation/network/nwconnectiongroup/message/path'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnectiongroup/message/path.json'
content_hash: 'sha256:ca4c6da3bc46577e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWConnectionGroup](../../nwconnectiongroup.md) · [Message](../message.md)

# path

<sub>Instance Property</sub>

The network path on which you receive the message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var path: NWPath? { get }
```

## See Also

### Inspecting Received Messages

- [remoteEndpoint](remoteendpoint.md) — The endpoint that originates the message you receive.
- [localEndpoint](localendpoint.md) — The local address and port you use to receive the message.
