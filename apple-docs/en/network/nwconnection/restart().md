---
title: restart()
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/restart()
source_url: 'https://developer.apple.com/documentation/network/nwconnection/restart()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/restart%28%29.json'
content_hash: 'sha256:422ea77e0ff763f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# restart()

<sub>Instance Method</sub>

Restarts a connection that is in the waiting state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func restart()
```

## Discussion

Restart a connection when it is in the waiting state and you have reason to believe the connection may succeed if it tries again. Connections that are waiting will automatically restart on network path changes.

## See Also

### Creating Connections

- [init(host:port:using:)](<init(host_port_using_).md>) — Initializes a new connection to a host and port.
- [init(to:using:)](<init(to_using_).md>) — Initializes a new connection to a remote endpoint.
- [start(queue:)](<start(queue_).md>) — Starts establishing a connection, and sets the queue on which to deliver all connection events.
