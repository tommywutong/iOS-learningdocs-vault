---
title: NSDistantObjectRequest
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsdistantobjectrequest
source_url: 'https://developer.apple.com/documentation/foundation/nsdistantobjectrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdistantobjectrequest.json'
content_hash: 'sha256:68a6a889c2bf1375'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDistantObjectRequest

<sub>Class</sub>

An object used by the distributed objects system to help handle invocations between different processes.

> [!warning] Deprecated
> Use [NSXPCConnection](nsxpcconnection.md) instead.

<sub>Mac Catalyst, macOS</sub>

```objc
@interface NSDistantObjectRequest : NSObject
```

## Overview

Do not create [NSDistantObjectRequest](nsdistantobjectrequest.md) objects directly. Unless you are getting involved with the low-level details of distributed objects, there should never be a need to access an [NSDistantObjectRequest](nsdistantobjectrequest.md). To intercept and possibly process requests yourself, implement the [NSConnection](nsconnection.md) delegate method [connection:handleRequest:](nsconnectiondelegate/connection_handlerequest_.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

## Topics

### Getting Information About a Request

- [connection](nsdistantobjectrequest/connection.md) — Returns the `NSConnection` object involved in the request. _(deprecated)_
- [conversation](nsdistantobjectrequest/conversation.md) — Returns the token object representing the conversation in which the receiver was created. _(deprecated)_
- [invocation](nsdistantobjectrequest/invocation.md) — Returns the `NSInvocation` object for the request. _(deprecated)_

### Raising a Remote Exception

- [replyWithException:](nsdistantobjectrequest/replywithexception_.md) — Sends a reply back to the remote object making the distant object request. _(deprecated)_

## See Also

### Legacy

- [NSMachPortDelegate](nsmachportdelegate.md) — An interface for handling incoming Mach messages.
- [NSConnectionDelegate](nsconnectiondelegate.md) — An interface for interacting with low-level, interprocess connections. _(deprecated)_
- [NSConnection](nsconnection.md) — An object that manages the communication between objects in different threads or between a thread and a process running on a local or remote system. _(deprecated)_
- [NSDistantObject](nsdistantobject.md) — A proxy for objects in other applications or threads. _(deprecated)_
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
