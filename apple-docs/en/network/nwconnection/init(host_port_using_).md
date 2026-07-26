---
title: 'init(host:port:using:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwconnection/init(host:port:using:)'
source_url: 'https://developer.apple.com/documentation/network/nwconnection/init(host:port:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/init%28host%3Aport%3Ausing%3A%29.json'
content_hash: 'sha256:565bb20941b531e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# init(host:port:using:)

<sub>Initializer</sub>

Initializes a new connection to a host and port.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(host: NWEndpoint.Host, port: NWEndpoint.Port, using: NWParameters)
```

## See Also

### Creating Connections

- [init(to:using:)](<init(to_using_).md>) — Initializes a new connection to a remote endpoint.
- [start(queue:)](<start(queue_).md>) — Starts establishing a connection, and sets the queue on which to deliver all connection events.
- [restart()](<restart().md>) — Restarts a connection that is in the waiting state.
