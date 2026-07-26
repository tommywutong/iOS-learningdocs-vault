---
title: PortMessage
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/portmessage
source_url: 'https://developer.apple.com/documentation/foundation/portmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/portmessage.json'
content_hash: 'sha256:d2a9db94db996beb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# PortMessage

<sub>Class</sub>

A low-level, operating system-independent type for inter-application (and inter-thread) messages.

<sub>Mac Catalyst, macOS</sub>

```swift
class PortMessage
```

## Overview

Port messages are used primarily by the distributed objects system. You should implement inter-application communication using distributed objects whenever possible and use [PortMessage](portmessage.md) only when necessary.

An [PortMessage](portmessage.md) object has three major parts: the send and receive ports, which are [Port](port.md) objects that link the sender of the message to the receiver, and the components, which form the body of the message. The components are held as an [NSArray](nsarray.md) object containing [NSData](nsdata.md) and [Port](port.md) objects. The [- sendBeforeDate:](<portmessage/send(before_).md>) message sends the components out through the send port; any replies to the message arrive on the receive port. See the [Port](port.md) class specification for information on handling incoming messages.

An [PortMessage](portmessage.md) instance can be initialized with a pair of [Port](port.md) objects and an array of components. A port message’s body can contain only [Port](port.md) objects or [NSData](nsdata.md) objects. In the distributed objects system the byte/character arrays are usually encoded [NSInvocation](nsinvocation.md) objects that are being forwarded from a proxy to the corresponding real object.

An [PortMessage](portmessage.md) object also maintains a message identifier, which can be used to indicate the class of a message, such as an Objective-C method invocation, a connection request, an error, and so on. Use the [msgid](portmessage/msgid.md) and [msgid](portmessage/msgid.md) methods to access the identifier.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating Instances

- [- initWithSendPort:receivePort:components:](<portmessage/init(send_receive_components_).md>) — Initializes a newly allocated `NSPortMessage` object to send given data on a given port and to receiver replies on another given port.

### Sending the Message

- [- sendBeforeDate:](<portmessage/send(before_).md>) — Attempts to send the message before the specified date.

### Getting the Components

- [components](portmessage/components.md) — Returns the data components of the receiver.

### Getting the Ports

- [receivePort](portmessage/receiveport.md) — For an outgoing message, returns the port on which replies to the receiver will arrive. For an incoming message, returns the port the receiver did arrive on.
- [sendPort](portmessage/sendport.md) — For an outgoing message, returns the port the receiver will send itself through. For an incoming message, returns the port replies to the receiver should be sent through.

### Accessing the Message ID

- [msgid](portmessage/msgid.md) — Returns the identifier for the receiver.

### Initializers

- [init(sendPort:receivePort:components:)](<portmessage/init(sendport_receiveport_components_).md>)

## See Also

### Legacy

- [NSMachPortDelegate](nsmachportdelegate.md) — An interface for handling incoming Mach messages.
- [NSMachPort](nsmachport.md) — A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [MessagePort](messageport.md) — A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [PortDelegate](portdelegate.md) — An interface for handling incoming messages.
- [NSProtocolChecker](nsprotocolchecker.md) — An object that restricts the messages that can be sent to another object (referred to as the checker’s delegate).
