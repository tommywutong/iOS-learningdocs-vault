---
title: 'NWListener.State.failed(_:)'
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwlistener/state-swift.enum/failed(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwlistener/state-swift.enum/failed(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwlistener/state-swift.enum/failed%28_%3A%29.json'
content_hash: 'sha256:ac7159e5fca8193c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWListener](../../nwlistener.md) · [State](../state-swift.enum.md)

# NWListener.State.failed(_:)

<sub>Case</sub>

The listener has encountered a fatal error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case failed(NWError)
```

## See Also

### States

- [NWListener.State.setup](setup.md) — The listener has been initialized but not started.
- [NWListener.State.waiting(_:)](<waiting(__).md>) — The listener is waiting for a network to become available.
- [NWListener.State.ready](ready.md) — The listener is running and able to receive incoming connections.
- [NWListener.State.cancelled](cancelled.md) — The listener has been canceled.
