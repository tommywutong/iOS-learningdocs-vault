---
title: NSConnection
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsconnection
source_url: 'https://developer.apple.com/documentation/foundation/nsconnection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconnection.json'
content_hash: 'sha256:eaedb07e7e170854'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSConnection

<sub>Class</sub>

An object that manages the communication between objects in different threads or between a thread and a process running on a local or remote system.

> [!warning] Deprecated
> Use [NSXPCConnection](nsxpcconnection.md) instead.

<sub>Mac Catalyst, macOS</sub>

```objc
@interface NSConnection : NSObject
```

## Overview

Connection objects form the backbone of the distributed objects mechanism and normally operate in the background. You use the methods of [NSConnection](nsconnection.md) explicitly when vending an object to other applications, when accessing such a vended object through a proxy, and when altering default communication parameters. At other times, you simply interact with a vended object or its proxy.

A single connection object may be shared by multiple threads and used to access a vended object.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

## Topics

### Getting the Default Instance

- [defaultConnection](nsconnection/defaultconnection.md) — Returns the default `NSConnection` object for the current thread. _(deprecated)_

### Creating Instances

- [connectionWithReceivePort:sendPort:](nsconnection/connectionwithreceiveport_sendport_.md) — Returns an `NSConnection` object that communicates using given send and receive ports. _(deprecated)_
- [initWithReceivePort:sendPort:](nsconnection/initwithreceiveport_sendport_.md) — Returns an `NSConnection` object initialized with given send and receive ports. _(deprecated)_

### Running the Connection in a New Thread

- [runInNewThread](nsconnection/runinnewthread.md) — Creates and starts a new `NSThread` object and then runs the receiving connection in the new thread. _(deprecated)_
- [enableMultipleThreads](nsconnection/enablemultiplethreads.md) — Configures the receiver to allow requests from multiple threads to the remote object, without requiring each thread to each maintain its own connection. _(deprecated)_
- [multipleThreadsEnabled](nsconnection/multiplethreadsenabled.md) — A Boolean value that indicates whether the receiver supports requests from multiple threads. _(deprecated)_
- [addRunLoop:](nsconnection/addrunloop_.md) — Adds the specified run loop to the list of run loops the receiver monitors and from which it responds to requests. _(deprecated)_
- [removeRunLoop:](nsconnection/removerunloop_.md) — Removes a given `NSRunLoop` object from the list of run loops the receiver monitors and from which it responds to requests. _(deprecated)_

### Vending a Service

- [serviceConnectionWithName:rootObject:usingNameServer:](nsconnection/serviceconnectionwithname_rootobject_usingnameserver_.md) — Creates and returns a new connection object representing a vended service on the specified port name server. _(deprecated)_
- [serviceConnectionWithName:rootObject:](nsconnection/serviceconnectionwithname_rootobject_.md) — Creates and returns a new connection object representing a vended service on the default system port name server. _(deprecated)_
- [registerName:](nsconnection/registername_.md) — Registers the specified service using with the default system port name server. _(deprecated)_
- [registerName:withNameServer:](nsconnection/registername_withnameserver_.md) — Registers a service with the specified port name server. _(deprecated)_
- [rootObject](nsconnection/rootobject-c.property.md) — The object that the receiver (or its parent) makes available to other applications or threads. _(deprecated)_

### Getting a Remote Object

- [connectionWithRegisteredName:host:](nsconnection/connectionwithregisteredname_host_.md) — Returns the `NSConnection` object whose send port links it to the `NSConnection` object registered with the default `NSPortNameServer` under a given name on a given host. _(deprecated)_
- [connectionWithRegisteredName:host:usingNameServer:](nsconnection/connectionwithregisteredname_host_usingnameserver_.md) — Returns the `NSConnection` object whose send port links it to the `NSConnection` object registered under a given name with a given server on a given host. _(deprecated)_
- [rootProxy](nsconnection/rootproxy.md) — The proxy for the root object of the receiver’s peer in another application or thread. _(deprecated)_
- [rootProxyForConnectionWithRegisteredName:host:](nsconnection/rootproxyforconnectionwithregisteredname_host_.md) — Returns a proxy for the root object of the `NSConnection` object registered with the default `NSPortNameServer` under a given name on a given host. _(deprecated)_
- [rootProxyForConnectionWithRegisteredName:host:usingNameServer:](nsconnection/rootproxyforconnectionwithregisteredname_host_usingnameserver_.md) — Returns a proxy for the root object of the `NSConnection` object registered with `server` under `name` on a given host. _(deprecated)_
- [remoteObjects](nsconnection/remoteobjects.md) — The local proxies for remote objects that have been received over the connection but not deallocated yet. _(deprecated)_
- [localObjects](nsconnection/localobjects.md) — The local objects that have been sent over the connection and still have proxies at the other end. _(deprecated)_

### Getting a Conversation

- [currentConversation](nsconnection/currentconversation.md) — Returns a token object representing any conversation in progress in the current thread. _(deprecated)_

### Getting All NSConnection Objects

- [allConnections](nsconnection/allconnections.md) — Returns all valid `NSConnection` objects in the process. _(deprecated)_

### Configuring Instances

- [requestTimeout](nsconnection/requesttimeout.md) — The timeout interval for outgoing remote messages. _(deprecated)_
- [replyTimeout](nsconnection/replytimeout.md) — The timeout interval for replies to outgoing remote messages. _(deprecated)_
- [independentConversationQueueing](nsconnection/independentconversationqueueing.md) — A Boolean value that indicates whether the receiver handles remote messages atomically. _(deprecated)_
- [addRequestMode:](nsconnection/addrequestmode_.md) — Adds `mode` to the set of run-loop input modes that the receiver uses for connection requests. _(deprecated)_
- [removeRequestMode:](nsconnection/removerequestmode_.md) — Removes `mode` from the set of run-loop input modes the receiver uses for connection requests. _(deprecated)_
- [requestModes](nsconnection/requestmodes-c.property.md) — The set of request modes the receiver’s receive port is registered for with its `NSRunLoop` object. _(deprecated)_
- [invalidate](nsconnection/invalidate.md) — Invalidates the receiver. _(deprecated)_
- [valid](nsconnection/valid.md) — A Boolean value that indicates whether the receiver is known to be valid. _(deprecated)_

### Getting Ports

- [receivePort](nsconnection/receiveport-c.property.md) — The port on which the receiver receives incoming network messages. _(deprecated)_
- [sendPort](nsconnection/sendport-c.property.md) — The port that the connection sends outgoing network messages through. _(deprecated)_
- [dispatchWithComponents:](nsconnection/dispatchwithcomponents_.md) — Allows subclasses to ask a connection object to dispatch component data. _(deprecated)_

### Getting Statistics

- [statistics](nsconnection/statistics-c.property.md) — A dictionary containing various statistics for the receiver. _(deprecated)_

### Setting the Delegate

- [delegate](nsconnection/delegate-c.property.md) — The receiver’s delegate. _(deprecated)_

### Constants

- [NSConnection run loop mode](nsconnection-run-loop-mode.md) — `NSConnection` defines the following run loop mode—see [RunLoop](runloop.md) for more details.
- [Connection Exception Names](connection-exception-names.md) — The name of an exception raised in case of authentication failure.

### Notifications

- [NSConnectionDidDieNotification](nsconnectiondiddienotification.md) — Posted when an `NSConnection` object is deallocated or when it’s notified that its `NSPort` object has become invalid. The notification object is the `NSConnection` object. This notification does not contain a `userInfo` dictionary. _(deprecated)_
- [NSConnectionDidInitializeNotification](nsconnectiondidinitializenotification.md) — Posted when an `NSConnection` object is initialized using [initWithReceivePort:sendPort:](nsconnection/initwithreceiveport_sendport_.md) (the designated initializer for `NSConnection`). The notification object is the `NSConnection` object. This notification does not contain a `userInfo` dictionary. _(deprecated)_

### Instance Variables

- [authCheck](nsconnection/authcheck.md) _(deprecated)_
- [authGen](nsconnection/authgen.md) _(deprecated)_
- [busy](nsconnection/busy.md) _(deprecated)_
- [classInfoImported](nsconnection/classinfoimported.md) _(deprecated)_
- [delayedRL](nsconnection/delayedrl.md) _(deprecated)_
- [delegate](nsconnection/delegate-c.ivar.md) _(deprecated)_
- [doRequest](nsconnection/dorequest.md) _(deprecated)_
- [invalidateRP](nsconnection/invalidaterp.md) _(deprecated)_
- [isDead](nsconnection/isdead.md) _(deprecated)_
- [isMulti](nsconnection/ismulti.md) _(deprecated)_
- [isQueueing](nsconnection/isqueueing.md) _(deprecated)_
- [isValid](nsconnection/isvalid.md) _(deprecated)_
- [localProxyCount](nsconnection/localproxycount.md) _(deprecated)_
- [receivePort](nsconnection/receiveport-c.ivar.md) _(deprecated)_
- [registerInfo](nsconnection/registerinfo.md) _(deprecated)_
- [releasedProxies](nsconnection/releasedproxies.md) _(deprecated)_
- [replMode](nsconnection/replmode.md) _(deprecated)_
- [requestModes](nsconnection/requestmodes-c.ivar.md) _(deprecated)_
- [reserved](nsconnection/reserved.md) _(deprecated)_
- [rootObject](nsconnection/rootobject-c.ivar.md) _(deprecated)_
- [runLoops](nsconnection/runloops.md) _(deprecated)_
- [sendPort](nsconnection/sendport-c.ivar.md) _(deprecated)_
- [statistics](nsconnection/statistics-c.ivar.md) _(deprecated)_
- [waitCount](nsconnection/waitcount.md) _(deprecated)_
- [wantsInvalid](nsconnection/wantsinvalid.md) _(deprecated)_

## See Also

### Legacy

- [NSMachPortDelegate](nsmachportdelegate.md) — An interface for handling incoming Mach messages.
- [NSConnectionDelegate](nsconnectiondelegate.md) — An interface for interacting with low-level, interprocess connections. _(deprecated)_
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
