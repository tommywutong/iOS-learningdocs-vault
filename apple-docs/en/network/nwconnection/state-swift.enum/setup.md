---
title: NWConnection.State.setup
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/state-swift.enum/setup
source_url: 'https://developer.apple.com/documentation/network/nwconnection/state-swift.enum/setup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/state-swift.enum/setup.json'
content_hash: 'sha256:c6ec5ddc9414bd61'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWConnection](../../nwconnection.md) · [State](../state-swift.enum.md)

# NWConnection.State.setup

<sub>Case</sub>

The connection has been initialized but not started.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case setup
```

## See Also

### States

- [NWConnection.State.waiting(_:)](<waiting(__).md>) — The connection is waiting for a network path change.
- [NWConnection.State.preparing](preparing.md) — The connection in the process of being established.
- [NWConnection.State.ready](ready.md) — The connection is established, and ready to send and receive data.
- [NWConnection.State.failed(_:)](<failed(__).md>) — The connection has disconnected or encountered an error.
- [NWConnection.State.cancelled](cancelled.md) — The connection has been canceled.
