---
title: 'NWConnection.State.waiting(_:)'
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwconnection/state-swift.enum/waiting(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwconnection/state-swift.enum/waiting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/state-swift.enum/waiting%28_%3A%29.json'
content_hash: 'sha256:35724f73d56ad30d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWConnection](../../nwconnection.md) · [State](../state-swift.enum.md)

# NWConnection.State.waiting(_:)

<sub>Case</sub>

The connection is waiting for a network path change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case waiting(NWError)
```

## Discussion

Connections that are waiting will indicate the reason that the connection couldn’t be established in the associated error. These errors are not fatal.

## See Also

### States

- [NWConnection.State.setup](setup.md) — The connection has been initialized but not started.
- [NWConnection.State.preparing](preparing.md) — The connection in the process of being established.
- [NWConnection.State.ready](ready.md) — The connection is established, and ready to send and receive data.
- [NWConnection.State.failed(_:)](<failed(__).md>) — The connection has disconnected or encountered an error.
- [NWConnection.State.cancelled](cancelled.md) — The connection has been canceled.
