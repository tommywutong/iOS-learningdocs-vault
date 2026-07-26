---
title: NSPortCoder
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsportcoder
source_url: 'https://developer.apple.com/documentation/foundation/nsportcoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsportcoder.json'
content_hash: 'sha256:9f4db48c75098f1c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSPortCoder

<sub>Class</sub>

A coder used to transmit object proxies (and sometimes objects themselves) between connections.

> [!warning] Deprecated
> Use [NSXPCConnection](nsxpcconnection.md) instead.

<sub>Mac Catalyst, macOS</sub>

```objc
@interface NSPortCoder : NSCoder
```

## Overview

[NSPortCoder](nsportcoder.md) is a concrete subclass of [NSCoder](nscoder.md) used in the distributed objects system to transmit object proxies (and sometimes objects themselves) between [NSConnection](nsconnection.md) objects. An [NSPortCoder](nsportcoder.md) instance is always created and used by an [NSConnection](nsconnection.md) object; you should never need to explicitly create or use one directly yourself.

## Relationships

- **Inherits From**: [NSCoder](nscoder.md)

## Topics

### Creating an NSPortCoder Object

- [portCoderWithReceivePort:sendPort:components:](nsportcoder/portcoderwithreceiveport_sendport_components_.md) — Creates and returns a new `NSPortCoder` object. _(deprecated)_
- [initWithReceivePort:sendPort:components:](nsportcoder/initwithreceiveport_sendport_components_.md) — Initializes and returns an `NSPortCoder` object. _(deprecated)_

### Getting the Connection

- [connection](nsportcoder/connection.md) — Returns the `NSConnection` object that uses the receiver. _(deprecated)_

### Encoding NSPort Objects

- [encodePortObject:](nsportcoder/encodeportobject_.md) — Encodes a given port so it can be properly reconstituted in the receiving process or thread. _(deprecated)_
- [decodePortObject](nsportcoder/decodeportobject.md) — Decodes and returns an `NSPort` object that was previously encoded with any of the general `encode...Object:` messages. _(deprecated)_

### Checking for Encoding

- [isBycopy](nsportcoder/isbycopy.md) — Returns a Boolean value that indicates whether the receiver is encoding an object by copying it. _(deprecated)_
- [isByref](nsportcoder/isbyref.md) — Returns a Boolean value that indicates whether the receiver is encoding an object by reference. _(deprecated)_

### Dispatching

- [dispatch](nsportcoder/dispatch.md) — Processes and acts upon the distributed object message with which the receiver was initialized. _(deprecated)_

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
- [PortDelegate](portdelegate.md) — An interface for handling incoming messages.
- [PortMessage](portmessage.md) — A low-level, operating system-independent type for inter-application (and inter-thread) messages.
- [NSPortNameServer](nsportnameserver.md) — An object-oriented interface to the port registration service used by the distributed objects system. _(deprecated)_
- [NSProtocolChecker](nsprotocolchecker.md) — An object that restricts the messages that can be sent to another object (referred to as the checker’s delegate).
- [NSSocketPortNameServer](nssocketportnameserver.md) — A port name server that takes and returns socket ports. _(deprecated)_
