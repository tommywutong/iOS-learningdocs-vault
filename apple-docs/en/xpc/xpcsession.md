---
title: XPCSession
framework: XPC
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xpc/xpcsession
source_url: 'https://developer.apple.com/documentation/xpc/xpcsession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xpc/xpcsession.json'
content_hash: 'sha256:1e654ade029b69f4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [XPC](../xpc.md)

# XPCSession

<sub>Class</sub>

A type that sends messages to a server process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class XPCSession
```

## Overview

XPC sessions are stateful connections you use to send structured messages to a separate process. Once established, a session remains active until one side of the connection cancels it, at which point the system invalidates the connection.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a session

- [init(xpcService:targetQueue:options:incomingMessageHandler:cancellationHandler:)](<xpcsession/init(xpcservice_targetqueue_options_incomingmessagehandler_cancellationhandler_)-407h2.md>) — Establishes a connection to an XPC service with the name and decodable message handler you specify.
- [init(xpcService:targetQueue:options:incomingMessageHandler:cancellationHandler:)](<xpcsession/init(xpcservice_targetqueue_options_incomingmessagehandler_cancellationhandler_)-9f4u0.md>) — Establishes a connection to an XPC service with the name and received message handler you specify.
- [init(xpcService:targetQueue:options:incomingMessageHandler:cancellationHandler:)](<xpcsession/init(xpcservice_targetqueue_options_incomingmessagehandler_cancellationhandler_)-bel3.md>) — Establishes a connection to an XPC service with the name and dictionary message handler you specify.
- [init(xpcService:targetQueue:options:cancellationHandler:)](<xpcsession/init(xpcservice_targetqueue_options_cancellationhandler_).md>) — Establishes a connection to an XPC service with the name you specify.
- [init(machService:targetQueue:options:incomingMessageHandler:cancellationHandler:)](<xpcsession/init(machservice_targetqueue_options_incomingmessagehandler_cancellationhandler_)-l3rz.md>) — Establishes a connection to a launch agent or launch daemon with the name and decodable message handler you specify.
- [init(machService:targetQueue:options:incomingMessageHandler:cancellationHandler:)](<xpcsession/init(machservice_targetqueue_options_incomingmessagehandler_cancellationhandler_)-2xuyi.md>) — Establishes a connection to a launch agent or launch daemon with the name and received message handler you specify.
- [init(machService:targetQueue:options:incomingMessageHandler:cancellationHandler:)](<xpcsession/init(machservice_targetqueue_options_incomingmessagehandler_cancellationhandler_)-6jz7y.md>) — Establishes a connection to a launch agent or launch daemon with the name and dictionary message handler you specify.
- [init(machService:targetQueue:options:cancellationHandler:)](<xpcsession/init(machservice_targetqueue_options_cancellationhandler_).md>) — Establishes a connection to a launch agent or launch daemon with the name you specify.
- [InitializationOptions](xpcsession/initializationoptions.md) — Options that control the session’s configuration.
- [setTargetQueue(_:)](<xpcsession/settargetqueue(__).md>) — Sets the target dispatch queue on an inactive session for processing messages.

### Managing the life cycle

- [activate()](<xpcsession/activate().md>) — Activates a session so you can send messages.
- [setIncomingMessageHandler(_:)](<xpcsession/setincomingmessagehandler(__)-2ukdh.md>) — Sets a closure to receive incoming decodable messages for a session.
- [setIncomingMessageHandler(_:)](<xpcsession/setincomingmessagehandler(__)-5lu26.md>) — Sets a closure to receive incoming received messages for a session.
- [setIncomingMessageHandler(_:)](<xpcsession/setincomingmessagehandler(__)-75ou9.md>) — Sets a closure to receive incoming dictionary messages for a session.
- [cancel(reason:)](<xpcsession/cancel(reason_).md>) — Cancels a session, discarding any unsent messages.
- [setCancellationHandler(_:)](<xpcsession/setcancellationhandler(__).md>) — Sets a closure the session calls when it’s canceled.

### Sending messages

- [send(_:)](<xpcsession/send(__).md>) — Sends an encodable message over the session to the destination service.
- [send(_:replyHandler:)](<xpcsession/send(__replyhandler_)-3wjln.md>) — Sends an encodable message over the session to the destination service, using the closure you specify to handle a reply and rich error.
- [send(_:replyHandler:)](<xpcsession/send(__replyhandler_)-9an0u.md>) — Sends an encodable message over the session to the destination service, using the closure you specify to handle a reply.
- [send(message:)](<xpcsession/send(message_).md>) — Sends a dictionary message over the session to the destination service.
- [send(message:replyHandler:)](<xpcsession/send(message_replyhandler_).md>) — Sends a message asynchronously over the session to the destination service, calling a closure after receiving a reply.
- [sendSync(_:)](<xpcsession/sendsync(__)-8a284.md>) — Sends an encodable message over the session to the destination service, blocking the caller until receiving a reply message.
- [sendSync(_:)](<xpcsession/sendsync(__)-88u0s.md>) — Sends an encodable message over the session to the destination service, blocking the caller until receiving an encodable reply message.
- [sendSync(message:)](<xpcsession/sendsync(message_).md>) — Sends a dictionary message over the session to the destination service, blocking the caller until receiving a reply.

### Initializers

- [init(endpoint:targetQueue:options:cancellationHandler:)](<xpcsession/init(endpoint_targetqueue_options_cancellationhandler_).md>) — Creates a new session object representing a connection to the xpc endpoint.
- [init(endpoint:targetQueue:options:incomingMessageHandler:cancellationHandler:)](<xpcsession/init(endpoint_targetqueue_options_incomingmessagehandler_cancellationhandler_)-2jmkk.md>) — Creates a new session object representing a connection to the xpc endpoint.
- [init(endpoint:targetQueue:options:incomingMessageHandler:cancellationHandler:)](<xpcsession/init(endpoint_targetqueue_options_incomingmessagehandler_cancellationhandler_)-546jo.md>) — Creates a new session object representing a connection to the xpc endpoint.
- [init(endpoint:targetQueue:options:incomingMessageHandler:cancellationHandler:)](<xpcsession/init(endpoint_targetqueue_options_incomingmessagehandler_cancellationhandler_)-6zd1x.md>) — Creates a new session object representing a connection to the xpc endpoint.
- [init(machService:targetQueue:options:requirement:cancellationHandler:)](<xpcsession/init(machservice_targetqueue_options_requirement_cancellationhandler_).md>)
- [init(machService:targetQueue:options:requirement:incomingMessageHandler:cancellationHandler:)](<xpcsession/init(machservice_targetqueue_options_requirement_incomingmessagehandler_cancellationhandler_)-5pk9g.md>)
- [init(machService:targetQueue:options:requirement:incomingMessageHandler:cancellationHandler:)](<xpcsession/init(machservice_targetqueue_options_requirement_incomingmessagehandler_cancellationhandler_)-7o5oq.md>)
- [init(machService:targetQueue:options:requirement:incomingMessageHandler:cancellationHandler:)](<xpcsession/init(machservice_targetqueue_options_requirement_incomingmessagehandler_cancellationhandler_)-84ll1.md>)
- [init(xpcService:targetQueue:options:requirement:cancellationHandler:)](<xpcsession/init(xpcservice_targetqueue_options_requirement_cancellationhandler_).md>) — Creates a new session object representing a connection to the named service, and requires that the session peer has the specified requirement.
- [init(xpcService:targetQueue:options:requirement:incomingMessageHandler:cancellationHandler:)](<xpcsession/init(xpcservice_targetqueue_options_requirement_incomingmessagehandler_cancellationhandler_)-3p0jf.md>)
- [init(xpcService:targetQueue:options:requirement:incomingMessageHandler:cancellationHandler:)](<xpcsession/init(xpcservice_targetqueue_options_requirement_incomingmessagehandler_cancellationhandler_)-6jxdc.md>)
- [init(xpcService:targetQueue:options:requirement:incomingMessageHandler:cancellationHandler:)](<xpcsession/init(xpcservice_targetqueue_options_requirement_incomingmessagehandler_cancellationhandler_)-osu4.md>)

### Instance Methods

- [setPeerRequirement(_:)](<xpcsession/setpeerrequirement(__).md>) — Requires that the session peer has the specified requirement

## See Also

### Interprocess communication

- [Creating XPC services](creating-xpc-services.md) — Configure a listener, establish a client session, and exchange messages between processes.
- [XPCListener](xpclistener.md) — A type that performs tasks for clients across process boundaries.
- [XPCReceivedMessage](xpcreceivedmessage.md) — A type that represents a message sent between a session and a listener.
- [xpc_listener_t](xpc_listener_t.md) — A C type that performs tasks for clients across process boundaries.
- [xpc_session_t](xpc_session_t-10if0.md) — A C type that sends messages to a server process.
