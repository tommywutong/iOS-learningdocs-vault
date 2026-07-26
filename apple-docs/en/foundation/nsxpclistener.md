---
title: NSXPCListener
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpclistener
source_url: 'https://developer.apple.com/documentation/foundation/nsxpclistener'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpclistener.json'
content_hash: 'sha256:fa745fe632d289d3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSXPCListener

<sub>Class</sub>

A listener that waits for new incoming connections, configures them, and accepts or rejects them.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSXPCListener
```

## Overview

Each XPC service, launchd agent, or launchd daemon typically has at least one [NSXPCListener](nsxpclistener.md) object that listens for connections to a specified service name. Each listener must have a delegate that conforms to the [NSXPCListenerDelegate](nsxpclistenerdelegate.md) protocol. When the listener receives a new connection request, it creates a new [NSXPCConnection](nsxpcconnection.md) object, then asks the delegate to inspect, configure, and resume the connection object by calling the delegate’s [- listener:shouldAcceptNewConnection:](<nsxpclistenerdelegate/listener(__shouldacceptnewconnection_).md>) method.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a listener

- [- initWithMachServiceName:](<nsxpclistener/init(machservicename_).md>) — Initializes a listener in a LaunchAgent or LaunchDaemon which has a name advertised in a `launchd.plist` file.

### Using standard listeners

- [+ serviceListener](<nsxpclistener/service().md>) — Returns the singleton listener used to listen for incoming connections in an XPC service.
- [+ anonymousListener](<nsxpclistener/anonymous().md>) — Returns a new anonymous listener connection.

### Working with a delegate

- [delegate](nsxpclistener/delegate.md) — The delegate for the listener.

### Providing access to clients

- [endpoint](nsxpclistener/endpoint.md) — Returns an endpoint object that may be sent over an existing connection.

### Managing connection state

- [- activate](<nsxpclistener/activate().md>) — Activates the listener.
- [- resume](<nsxpclistener/resume().md>) — Starts processing of incoming requests.
- [- invalidate](<nsxpclistener/invalidate().md>) — Invalidates the listener.
- [- suspend](<nsxpclistener/suspend().md>) — Suspends the listener.

### Working with code-signing

- [- setConnectionCodeSigningRequirement:](<nsxpclistener/setconnectioncodesigningrequirement(__).md>) — Sets the code signing requirement for connections to this listener.

## See Also

### XPC Services

- [NSXPCListenerDelegate](nsxpclistenerdelegate.md) — The protocol that delegates to the XPC listener use to accept or reject new connections.
- [NSXPCListenerEndpoint](nsxpclistenerendpoint.md) — An object that names a specific XPC listener.
