---
title: NSConnectionDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsconnectiondelegate
source_url: 'https://developer.apple.com/documentation/foundation/nsconnectiondelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnectiondelegate.json'
content_hash: 'sha256:da96b3dd8f3e54b9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSConnectionDelegate

<sub>Protocol</sub>

An interface for interacting with low-level, interprocess connections.

> [!warning] Deprecated
> Use [NSXPCConnection](nsxpcconnection.md) instead.

<sub>Mac Catalyst, macOS</sub>

```objc
@protocol NSConnectionDelegate <NSObject>
```

## Overview

The [NSConnectionDelegate](nsconnectiondelegate.md) protocol defines the optional methods implemented by delegates of [NSConnection](nsconnection.md) objects.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Authenticating

- [authenticateComponents:withData:](nsconnectiondelegate/authenticatecomponents_withdata_.md) — Returns a Boolean value that indicates whether given authentication data is valid for a given set of components. _(deprecated)_
- [authenticationDataForComponents:](nsconnectiondelegate/authenticationdataforcomponents_.md) — Returns an `NSData` object to be used as an authentication stamp for an outgoing message. _(deprecated)_

### Responding to a Connection

- [connection:shouldMakeNewConnection:](nsconnectiondelegate/connection_shouldmakenewconnection_.md) — Returns a Boolean value that indicates whether the parent connection should allow a given new connection to be created. _(deprecated)_
- [connection:handleRequest:](nsconnectiondelegate/connection_handlerequest_.md) — This method should be implemented by `NSConnection` object delegates that want to intercept distant object requests. _(deprecated)_
- [createConversationForConnection:](nsconnectiondelegate/createconversationforconnection_.md) — Returns an arbitrary object identifying a new conversation being created for the connection in the current thread. _(deprecated)_
- [makeNewConnection:sender:](nsconnectiondelegate/makenewconnection_sender_.md) — Returns a Boolean value that indicates whether the parent should allow a given new connection to be created and configured. _(deprecated)_

## See Also

### Legacy

- [NSMachPortDelegate](nsmachportdelegate.md) — An interface for handling incoming Mach messages.
- [NSConnection](nsconnection.md) — An object that manages the communication between objects in different threads or between a thread and a process running on a local or remote system. _(deprecated)_
- [NSDistantObject](nsdistantobject.md) — A proxy for objects in other applications or threads. _(deprecated)_
- [NSDistantObjectRequest](nsdistantobjectrequest.md) — An object used by the distributed objects system to help handle invocations between different processes. _(deprecated)_
- [NSMachBootstrapServer](nsmachbootstrapserver.md) — A port name server that takes and returns Mach port objects. _(deprecated)_
- [NSMachPort](nsmachport.md) — A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [MessagePort](messageport.md) — A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [NSMessagePortNameServer](nsmessageportnameserver.md) — A server takes and returns message ports. _(deprecated)_
- [NSPortCoder](nsportcoder.md) — A coder used to transmit object proxies (and sometimes objects themselves) between connections. _(deprecated)_
- [PortDelegate](portdelegate.md) — An interface for handling incoming messages.
- [PortMessage](portmessage.md) — A low-level, operating system-independent type for inter-application (and inter-thread) messages.
- [NSPortNameServer](nsportnameserver.md) — An object-oriented interface to the port registration service used by the distributed objects system. _(deprecated)_
- [NSProtocolChecker](nsprotocolchecker.md) — An object that restricts the messages that can be sent to another object (referred to as the checker’s delegate).
- [NSSocketPortNameServer](nssocketportnameserver.md) — A port name server that takes and returns socket ports. _(deprecated)_
