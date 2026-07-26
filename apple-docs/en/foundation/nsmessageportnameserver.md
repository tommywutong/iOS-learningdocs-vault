---
title: NSMessagePortNameServer
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsmessageportnameserver
source_url: 'https://developer.apple.com/documentation/foundation/nsmessageportnameserver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmessageportnameserver.json'
content_hash: 'sha256:6c81b9e498ce268d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMessagePortNameServer

<sub>Class</sub>

A server takes and returns message ports.

> [!warning] Deprecated
> Use [NSXPCConnection](nsxpcconnection.md) instead.

<sub>Mac Catalyst, macOS</sub>

```objc
@interface NSMessagePortNameServer : NSPortNameServer
```

## Overview

This port name server takes and returns instances of [MessagePort](messageport.md). Port removal functionality is not supported in [NSMessagePortNameServer](nsmessageportnameserver.md); if you want to cancel a service, you have to destroy the port (invalidate the [MessagePort](messageport.md) object given to [registerPort:name:](nsportnameserver/registerport_name_.md)).

## Relationships

- **Inherits From**: [NSPortNameServer](nsportnameserver.md)

## Topics

### Getting the Server Object

- [sharedInstance](nsmessageportnameserver/sharedinstance.md) — Returns the singleton instance of `NSMessagePortNameServer`. _(deprecated)_

### Getting Ports By Name

- [portForName:](nsmessageportnameserver/portforname_.md) — Returns the `NSPort` object registered under a given name on the local host. _(deprecated)_
- [portForName:host:](nsmessageportnameserver/portforname_host_.md) — Returns the `NSPort` object registered under a given name on the local host. _(deprecated)_

## See Also

### Legacy

- [NSMachPortDelegate](nsmachportdelegate.md) — An interface for handling incoming Mach messages.
- [NSConnectionDelegate](nsconnectiondelegate.md) — An interface for interacting with low-level, interprocess connections. _(deprecated)_
- [NSConnection](nsconnection.md) — An object that manages the communication between objects in different threads or between a thread and a process running on a local or remote system. _(deprecated)_
- [NSDistantObject](nsdistantobject.md) — A proxy for objects in other applications or threads. _(deprecated)_
- [NSDistantObjectRequest](nsdistantobjectrequest.md) — An object used by the distributed objects system to help handle invocations between different processes. _(deprecated)_
- [NSMachBootstrapServer](nsmachbootstrapserver.md) — A port name server that takes and returns Mach port objects. _(deprecated)_
- [NSMachPort](nsmachport.md) — A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [MessagePort](messageport.md) — A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [NSPortCoder](nsportcoder.md) — A coder used to transmit object proxies (and sometimes objects themselves) between connections. _(deprecated)_
- [PortDelegate](portdelegate.md) — An interface for handling incoming messages.
- [PortMessage](portmessage.md) — A low-level, operating system-independent type for inter-application (and inter-thread) messages.
- [NSPortNameServer](nsportnameserver.md) — An object-oriented interface to the port registration service used by the distributed objects system. _(deprecated)_
- [NSProtocolChecker](nsprotocolchecker.md) — An object that restricts the messages that can be sent to another object (referred to as the checker’s delegate).
- [NSSocketPortNameServer](nssocketportnameserver.md) — A port name server that takes and returns socket ports. _(deprecated)_
