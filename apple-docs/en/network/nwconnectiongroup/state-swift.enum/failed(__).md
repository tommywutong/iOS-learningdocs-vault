---
title: 'NWConnectionGroup.State.failed(_:)'
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwconnectiongroup/state-swift.enum/failed(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwconnectiongroup/state-swift.enum/failed(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnectiongroup/state-swift.enum/failed%28_%3A%29.json'
content_hash: 'sha256:854efd084a25dcc3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWConnectionGroup](../../nwconnectiongroup.md) · [State](../state-swift.enum.md)

# NWConnectionGroup.State.failed(_:)

<sub>Case</sub>

The connection group encountered a fatal error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case failed(NWError)
```

## See Also

### States

- [NWConnectionGroup.State.setup](setup.md) — You have not yet started the connection group.
- [NWConnectionGroup.State.waiting(_:)](<waiting(__).md>) — The connection group is waiting for a network path change.
- [NWConnectionGroup.State.ready](ready.md) — The connection group is joined, and ready to send and receive data.
- [NWConnectionGroup.State.cancelled](cancelled.md) — The connection group has been canceled.
