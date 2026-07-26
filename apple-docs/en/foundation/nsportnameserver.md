---
title: NSPortNameServer
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsportnameserver
source_url: 'https://developer.apple.com/documentation/foundation/nsportnameserver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsportnameserver.json'
content_hash: 'sha256:ee45f31903b6c315'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSPortNameServer

<sub>Class</sub>

An object-oriented interface to the port registration service used by the distributed objects system.

> [!warning] Deprecated
> Use [NSXPCConnection](nsxpcconnection.md) instead.

<sub>Mac Catalyst, macOS</sub>

```objc
@interface NSPortNameServer : NSObject
```

## Overview

[NSConnection](nsconnection.md) objects use this interface to contact each other and to distribute objects over the network; you should rarely need to interact directly with an [NSPortNameServer](nsportnameserver.md).

You get an [NSPortNameServer](nsportnameserver.md) object by using the [systemDefaultPortNameServer](nsportnameserver/systemdefaultportnameserver.md) class method—never allocate and initialize an instance directly. With the default server object you can register an [Port](port.md) object under a given name, making it available on the network, and also unregister it so that it can’t be looked up (although other applications that have already looked up the [Port](port.md) object  can still use it until it becomes invalid). See the [Port](port.md) class specification for more information.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSMachBootstrapServer](nsmachbootstrapserver.md), [NSMessagePortNameServer](nsmessageportnameserver.md), [NSSocketPortNameServer](nssocketportnameserver.md)

## Topics

### Getting the Server Object

- [systemDefaultPortNameServer](nsportnameserver/systemdefaultportnameserver.md) — Returns the single instance of `NSPortNameServer` for the application. _(deprecated)_

### Looking up Ports

- [portForName:](nsportnameserver/portforname_.md) — Looks up and returns the port registered under the specified name on the local host. _(deprecated)_
- [portForName:host:](nsportnameserver/portforname_host_.md) — Looks up and returns the port registered under the specified name on a specified host. _(deprecated)_

### Registering Ports

- [registerPort:name:](nsportnameserver/registerport_name_.md) — Makes a given port available on the network under a specified name. _(deprecated)_
- [removePortForName:](nsportnameserver/removeportforname_.md) — Unregisters the port for a given name on the local host. _(deprecated)_

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
- [NSMessagePortNameServer](nsmessageportnameserver.md) — A server takes and returns message ports. _(deprecated)_
- [NSPortCoder](nsportcoder.md) — A coder used to transmit object proxies (and sometimes objects themselves) between connections. _(deprecated)_
- [PortDelegate](portdelegate.md) — An interface for handling incoming messages.
- [PortMessage](portmessage.md) — A low-level, operating system-independent type for inter-application (and inter-thread) messages.
- [NSProtocolChecker](nsprotocolchecker.md) — An object that restricts the messages that can be sent to another object (referred to as the checker’s delegate).
- [NSSocketPortNameServer](nssocketportnameserver.md) — A port name server that takes and returns socket ports. _(deprecated)_
