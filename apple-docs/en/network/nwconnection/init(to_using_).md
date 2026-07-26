---
title: 'init(to:using:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwconnection/init(to:using:)'
source_url: 'https://developer.apple.com/documentation/network/nwconnection/init(to:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/init%28to%3Ausing%3A%29.json'
content_hash: 'sha256:d9260cafa065f85f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# init(to:using:)

<sub>Initializer</sub>

Initializes a new connection to a remote endpoint.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(to: NWEndpoint, using: NWParameters)
```

## See Also

### Creating Connections

- [init(host:port:using:)](<init(host_port_using_).md>) — Initializes a new connection to a host and port.
- [start(queue:)](<start(queue_).md>) — Starts establishing a connection, and sets the queue on which to deliver all connection events.
- [restart()](<restart().md>) — Restarts a connection that is in the waiting state.
