---
title: NSProtocolChecker
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsprotocolchecker
source_url: 'https://developer.apple.com/documentation/foundation/nsprotocolchecker'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsprotocolchecker.json'
content_hash: 'sha256:a59d77c612b57532'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSProtocolChecker

<sub>Class</sub>

An object that restricts the messages that can be sent to another object (referred to as the checker’s delegate).

<sub>Mac Catalyst, macOS</sub>

```swift
class NSProtocolChecker
```

## Overview

A [NSProtocolChecker](nsprotocolchecker.md) object can be particularly useful when an object with many methods, only a few of which ought to be remotely accessible, is made available using the distributed objects system.

A protocol checker acts as a kind of proxy; when it receives a message that is in its designated protocol, it forwards the message to its target and consequently appears to be the target object itself. However, when it receives a message not in its protocol, it raises an [NSInvalidArgumentException](nsexceptionname/invalidargumentexception.md) to indicate that the message isn’t allowed, whether or not the target object implements the method.

Typically, an object that is to be distributed (yet must restrict messages) creates an [NSProtocolChecker](nsprotocolchecker.md) for itself and returns the checker rather than returning itself in response to any messages. The object might also register the checker as the root object of an NSConnection.

The object should be careful about vending references to `self`—the protocol checker will convert a return value of `self` to indicate the checker rather than the object for any messages forwarded by the checker, but direct references to the object (bypassing the checker) could be passed around by other objects.

## Relationships

- **Inherits From**: [NSProxy](nsproxy.md)

- **Conforms To**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a checker

- [- initWithTarget:protocol:](<nsprotocolchecker/init(target_protocol_).md>) — Initializes a newly allocated `NSProtocolChecker` instance that will forward any messages in `aProtocol` to `anObject`, the protocol checker’s target.

### Getting information

- [protocol](nsprotocolchecker/protocol.md) — Returns the protocol object the receiver uses.
- [target](nsprotocolchecker/target.md) — Returns the target of the receiver.

## See Also

### Legacy

- [NSMachPortDelegate](nsmachportdelegate.md) — An interface for handling incoming Mach messages.
- [NSMachPort](nsmachport.md) — A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [MessagePort](messageport.md) — A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [PortDelegate](portdelegate.md) — An interface for handling incoming messages.
- [PortMessage](portmessage.md) — A low-level, operating system-independent type for inter-application (and inter-thread) messages.
