---
title: XPCListener
framework: XPC
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xpc/xpclistener
source_url: 'https://developer.apple.com/documentation/xpc/xpclistener'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xpc/xpclistener.json'
content_hash: 'sha256:05a97c887fea701a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [XPC](../xpc.md)

# XPCListener

<sub>Class</sub>

A type that performs tasks for clients across process boundaries.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class XPCListener
```

## Overview

To implement an XPC service, create a listener and respond to incoming session requests.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a listener

- [init(service:targetQueue:options:incomingSessionHandler:)](<xpclistener/init(service_targetqueue_options_incomingsessionhandler_).md>) — Creates the server side of an XPC service using the specified service name.
- [InitializationOptions](xpclistener/initializationoptions.md) — Options that control the listener’s configuration, such as if it’s inactive at creation.
- [IncomingSessionRequest](xpclistener/incomingsessionrequest.md) — A session request from a client that you accept or reject.

### Managing the life cycle

- [activate()](<xpclistener/activate().md>) — Activates an inactive listener.
- [cancel()](<xpclistener/cancel().md>) — Cancels a listener.

### Handling incoming messages

- [XPCPeerHandler](xpcpeerhandler.md) — A type that handles incoming messages from a client and session cancellation.

### Initializers

- [init(service:targetQueue:options:requirement:incomingSessionHandler:)](<xpclistener/init(service_targetqueue_options_requirement_incomingsessionhandler_).md>) — Creates a listener with the service defined by the provided name, and requires that the session peer has the specified requirement.
- [init(targetQueue:options:incomingSessionHandler:)](<xpclistener/init(targetqueue_options_incomingsessionhandler_).md>) — Creates an anonymous listener

### Instance Properties

- [endpoint](xpclistener/endpoint.md) — Creates an endpoint from the listener.

## See Also

### Interprocess communication

- [Creating XPC services](creating-xpc-services.md) — Configure a listener, establish a client session, and exchange messages between processes.
- [XPCSession](xpcsession.md) — A type that sends messages to a server process.
- [XPCReceivedMessage](xpcreceivedmessage.md) — A type that represents a message sent between a session and a listener.
- [xpc_listener_t](xpc_listener_t.md) — A C type that performs tasks for clients across process boundaries.
- [xpc_session_t](xpc_session_t-10if0.md) — A C type that sends messages to a server process.
