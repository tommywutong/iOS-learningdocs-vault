---
title: 'keepalive(idleTimeInSeconds:count:intervalInSeconds:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/tcp/keepalive(idletimeinseconds:count:intervalinseconds:)'
source_url: 'https://developer.apple.com/documentation/network/tcp/keepalive(idletimeinseconds:count:intervalinseconds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tcp/keepalive%28idletimeinseconds%3Acount%3Aintervalinseconds%3A%29.json'
content_hash: 'sha256:a655241c2fa8d75d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [TCP](../tcp.md)

# keepalive(idleTimeInSeconds:count:intervalInSeconds:)

<sub>Instance Method</sub>

Enable TCP keepalives.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func keepalive(idleTimeInSeconds: UInt32, count: UInt32, intervalInSeconds: UInt32) -> TCP
```

## Parameters

- `idleTimeInSeconds` — The number of seconds of idleness to wait before keepalive probes are sent by TCP (`TCP_KEEPALIVE`).

- `count` — The number of keepalive probes to send before terminating.

- `intervalInSeconds` — The number of seconds of to wait before resending TCP keepalive probes (`TCP_KEEPINTVL`).
