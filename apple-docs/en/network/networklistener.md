---
title: NetworkListener
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networklistener
source_url: 'https://developer.apple.com/documentation/network/networklistener'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networklistener.json'
content_hash: 'sha256:7df6c6c3987cbcf7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NetworkListener

<sub>Class</sub>

Listen for incoming network connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class NetworkListener<ApplicationProtocol> where ApplicationProtocol : NetworkProtocolOptions
```

## Overview

A listener receives incoming connections by binding to a local endpoint. It accepts connections based on the protocols defined in its protocol stack. Accepted connections will represent new local and remote address and port tuples.

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(for:using:)](<networklistener/init(for_using_)-2hkg.md>) — Create a listener that advertises a service with a protocol stack to use for listening.
- [init(for:using:)](<networklistener/init(for_using_)-2vh87.md>) — Create a listener that advertises a service with a protocol stack and parameters to use for listening.

### Instance Properties

- [newConnectionLimit](networklistener/newconnectionlimit.md) — Configure the listener’s new connection limit.
- [port](networklistener/port.md) — The port that the listener is listening on.
- [service](networklistener/service.md) — An optional service to advertise with the listener.

### Instance Methods

- [newConnectionLimit(_:)](<networklistener/newconnectionlimit(__).md>) — Configure the listener’s new connection limit.
- [onServiceRegistrationUpdate(_:)](<networklistener/onserviceregistrationupdate(__).md>) — Set a closure to be called when the listener has added or removed a registered service.
- [onStateUpdate(_:)](<networklistener/onstateupdate(__).md>) — Set a closure to be called when the listener’s state changes.
- [run(_:)](<networklistener/run(__)-42k25.md>) — Run the listener and receive incoming multiplexed connections.
- [run(_:)](<networklistener/run(__)-4iov3.md>) — Run the listener and receive incoming connections.

### Type Aliases

- [ServiceRegistrationUpdateHandler](networklistener/serviceregistrationupdatehandler.md)
- [StateUpdateHandler](networklistener/stateupdatehandler.md)

### Enumerations

- [ServiceRegistrationChange](networklistener/serviceregistrationchange.md)
- [State](networklistener/state.md)
