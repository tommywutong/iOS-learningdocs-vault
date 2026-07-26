---
title: NSSocketPortNameServer
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nssocketportnameserver
source_url: 'https://developer.apple.com/documentation/foundation/nssocketportnameserver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssocketportnameserver.json'
content_hash: 'sha256:16dde6347141f20e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSSocketPortNameServer

<sub>Class</sub>

A port name server that takes and returns socket ports.

> [!warning] Deprecated
> Use [NSXPCConnection](nsxpcconnection.md) instead.

<sub>macOS</sub>

```objc
@interface NSSocketPortNameServer : NSPortNameServer
```

## Overview

Port removal functionality is supported by the [removePortForName:](nssocketportnameserver/removeportforname_.md) method and should be used to remove invalid socket ports.

Unlike the other port name servers, [NSSocketPortNameServer](nssocketportnameserver.md) can operate over a network. By registering your socket ports, you make them available to other computers on the local network without hard-coding the TCP port numbers. Clients just need to know the name of the port.

[NSPortNameServer](nsportnameserver.md) is implemented using [NetService](netservice.md) and registers ports in the local network domain. The registered name of a port must be unique within the local domain, not just the local host. The name server only supports TCP/IP (either IPv4 or IPv6) sockets.

> [!note] Note
> Prior to OS X 10.2, [NSSocketPortNameServer](nssocketportnameserver.md) was inoperable.

## Relationships

- **Inherits From**: [NSPortNameServer](nsportnameserver.md)

## Topics

### Getting the Server Object

- [sharedInstance](nssocketportnameserver/sharedinstance.md) — Returns the shared socket port name server. _(deprecated)_

### Looking up Ports

- [portForName:](nssocketportnameserver/portforname_.md) — Looks up and returns the port registered under the specified name on the local host. _(deprecated)_
- [portForName:host:](nssocketportnameserver/portforname_host_.md) — Looks up and returns the port registered under the specified name on a specified host. _(deprecated)_
- [portForName:host:nameServerPortNumber:](nssocketportnameserver/portforname_host_nameserverportnumber_.md) — Looks up and returns the port registered under the specified name on a specified host. _(deprecated)_

### Registering and Removing Ports

- [registerPort:name:](nssocketportnameserver/registerport_name_.md) — Registers a given port as a network service with the specified name in the local domain. _(deprecated)_
- [registerPort:name:nameServerPortNumber:](nssocketportnameserver/registerport_name_nameserverportnumber_.md) — Registers a given port as a network service with the specified name in the local domain. _(deprecated)_
- [removePortForName:](nssocketportnameserver/removeportforname_.md) — Unregisters the port for a given name on the local host. _(deprecated)_

### Configuring the Default Port Number

- [defaultNameServerPortNumber](nssocketportnameserver/defaultnameserverportnumber.md) — Returns the port number used to contact the name server. _(deprecated)_

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
- [NSPortNameServer](nsportnameserver.md) — An object-oriented interface to the port registration service used by the distributed objects system. _(deprecated)_
- [NSProtocolChecker](nsprotocolchecker.md) — An object that restricts the messages that can be sent to another object (referred to as the checker’s delegate).
