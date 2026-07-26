---
title: NSMachBootstrapServer
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsmachbootstrapserver
source_url: 'https://developer.apple.com/documentation/foundation/nsmachbootstrapserver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmachbootstrapserver.json'
content_hash: 'sha256:84b4b756540ea51a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMachBootstrapServer

<sub>Class</sub>

A port name server that takes and returns Mach port objects.

> [!warning] Deprecated
> Use [NSXPCConnection](nsxpcconnection.md) instead.

<sub>Mac Catalyst, macOS</sub>

```objc
@interface NSMachBootstrapServer : NSPortNameServer
```

## Overview

Port removal functionality is not supported in [NSMachBootstrapServer](nsmachbootstrapserver.md); if you want to cancel a service, you have to destroy the port (invalidate the [NSMachPort](nsmachport.md) given to [registerPort:name:](nsmachbootstrapserver/registerport_name_.md)).

## Relationships

- **Inherits From**: [NSPortNameServer](nsportnameserver.md)

## Topics

### Getting the Server Object

- [sharedInstance](nsmachbootstrapserver/sharedinstance.md) — Returns the shared instance of the bootstrap server. _(deprecated)_

### Looking up Ports

- [portForName:](nsmachbootstrapserver/portforname_.md) — Looks up and returns the port registered under the specified name on the local host. _(deprecated)_
- [portForName:host:](nsmachbootstrapserver/portforname_host_.md) — Looks up and returns the port registered under the specified name. _(deprecated)_
- [servicePortWithName:](nsmachbootstrapserver/serviceportwithname_.md) — Looks up and returns the port for the vended service that is registered under the specified name. _(deprecated)_

### Registering Ports

- [registerPort:name:](nsmachbootstrapserver/registerport_name_.md) — Registers a port with a specified name. _(deprecated)_

## See Also

### Legacy

- [NSMachPortDelegate](nsmachportdelegate.md) — An interface for handling incoming Mach messages.
- [NSConnectionDelegate](nsconnectiondelegate.md) — An interface for interacting with low-level, interprocess connections. _(deprecated)_
- [NSConnection](nsconnection.md) — An object that manages the communication between objects in different threads or between a thread and a process running on a local or remote system. _(deprecated)_
- [NSDistantObject](nsdistantobject.md) — A proxy for objects in other applications or threads. _(deprecated)_
- [NSDistantObjectRequest](nsdistantobjectrequest.md) — An object used by the distributed objects system to help handle invocations between different processes. _(deprecated)_
- [NSMachPort](nsmachport.md) — A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [MessagePort](messageport.md) — A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [NSMessagePortNameServer](nsmessageportnameserver.md) — A server takes and returns message ports. _(deprecated)_
- [NSPortCoder](nsportcoder.md) — A coder used to transmit object proxies (and sometimes objects themselves) between connections. _(deprecated)_
- [PortDelegate](portdelegate.md) — An interface for handling incoming messages.
- [PortMessage](portmessage.md) — A low-level, operating system-independent type for inter-application (and inter-thread) messages.
- [NSPortNameServer](nsportnameserver.md) — An object-oriented interface to the port registration service used by the distributed objects system. _(deprecated)_
- [NSProtocolChecker](nsprotocolchecker.md) — An object that restricts the messages that can be sent to another object (referred to as the checker’s delegate).
- [NSSocketPortNameServer](nssocketportnameserver.md) — A port name server that takes and returns socket ports. _(deprecated)_
