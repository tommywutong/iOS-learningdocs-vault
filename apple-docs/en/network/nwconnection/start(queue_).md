---
title: 'start(queue:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwconnection/start(queue:)'
source_url: 'https://developer.apple.com/documentation/network/nwconnection/start(queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/start%28queue%3A%29.json'
content_hash: 'sha256:14b7eb51e948f17c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# start(queue:)

<sub>Instance Method</sub>

Starts establishing a connection, and sets the queue on which to deliver all connection events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func start(queue: DispatchQueue)
```

## See Also

### Creating Connections

- [init(host:port:using:)](<init(host_port_using_).md>) — Initializes a new connection to a host and port.
- [init(to:using:)](<init(to_using_).md>) — Initializes a new connection to a remote endpoint.
- [restart()](<restart().md>) — Restarts a connection that is in the waiting state.
