---
title: NSXPCConnection
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpcconnection
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnection.json'
content_hash: 'sha256:7780aa499e668395'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSXPCConnection

<sub>Class</sub>

A bidirectional communication channel between two processes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSXPCConnection
```

## Overview

This class is the primary means of creating and configuring the communication mechanism between two processes. Each process has one instance of this class to represent the endpoint in the communication channel.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSXPCProxyCreating](nsxpcproxycreating.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a connection

- [- initWithListenerEndpoint:](<nsxpcconnection/init(listenerendpoint_).md>) — Initializes an [NSXPCConnection](nsxpcconnection.md) object to connect to an [NSXPCListener](nsxpclistener.md) object in another process, identified by an [NSXPCListenerEndpoint](nsxpclistenerendpoint.md) object.
- [- initWithMachServiceName:options:](<nsxpcconnection/init(machservicename_options_).md>) — Initializes an [NSXPCConnection](nsxpcconnection.md) object to connect to a LaunchAgent or LaunchDaemon with a name advertised in a `launchd.plist`.
- [Options](nsxpcconnection/options.md) — Options that you can pass to a connection.
- [- initWithServiceName:](<nsxpcconnection/init(servicename_).md>) — Initializes an [NSXPCConnection](nsxpcconnection.md) object to connect to an [NSXPCListener](nsxpclistener.md) object in an XPC service, identified by a service name.

### Managing connection state

- [- activate](<nsxpcconnection/activate().md>) — Activates the connection.
- [- resume](<nsxpcconnection/resume().md>) — Starts or resumes handling of messages on a connection.
- [- invalidate](<nsxpcconnection/invalidate().md>) — Invalidates the connection.
- [- suspend](<nsxpcconnection/suspend().md>) — Suspends the connection.
- [interruptionHandler](nsxpcconnection/interruptionhandler.md) — An interruption handler that is called if the remote process exits or crashes.
- [invalidationHandler](nsxpcconnection/invalidationhandler.md) — An invalidation handler that is called if the connection can not be formed or the connection has terminated and may not be re-established.
- [+ currentConnection](<nsxpcconnection/current().md>) — Returns the current connection, in the context of a call to a method on your exported object.
- [- scheduleSendBarrierBlock:](<nsxpcconnection/schedulesendbarrierblock(__).md>) — Add a barrier block to execute on the connection.

### Managing the connection interface

- [serviceName](nsxpcconnection/servicename.md) — The name of the XPC service that this connection was configured to connect to.
- [endpoint](nsxpcconnection/endpoint.md) — If the connection was created with an [NSXPCListenerEndpoint](nsxpclistenerendpoint.md) object, returns the endpoint object used.
- [exportedInterface](nsxpcconnection/exportedinterface.md) — The [NSXPCInterface](nsxpcinterface.md) object that describes the protocol for the exported object on this connection.
- [exportedObject](nsxpcconnection/exportedobject.md) — An exported object for the connection.
- [remoteObjectInterface](nsxpcconnection/remoteobjectinterface.md) — Defines the [NSXPCInterface](nsxpcinterface.md) object that describes the protocol for the object represented by the `remoteObjectProxy`.
- [remoteObjectProxy](nsxpcconnection/remoteobjectproxy.md) — Returns a proxy for the remote object (that is, the `exportedObject` from the other side of this connection).

### Working with security attributes

- [auditSessionIdentifier](nsxpcconnection/auditsessionidentifier.md) — The BSM audit session identifier for the connecting process.
- [processIdentifier](nsxpcconnection/processidentifier.md) — The process ID (PID) of the connecting process.
- [effectiveGroupIdentifier](nsxpcconnection/effectivegroupidentifier.md) — The effective group ID (EGID) of the connecting process.
- [effectiveUserIdentifier](nsxpcconnection/effectiveuseridentifier.md) — The effective user ID (EUID) of the connecting process.

### Working with proxy objects

- [- remoteObjectProxyWithErrorHandler:](<nsxpcconnection/remoteobjectproxywitherrorhandler(__).md>) — Returns a proxy for the remote object (that is, the object exported from the other side of this connection) with the specified error handler.
- [- synchronousRemoteObjectProxyWithErrorHandler:](<nsxpcconnection/synchronousremoteobjectproxywitherrorhandler(__).md>) — Returns a proxy that makes a synchronous IPC call instead of the default async behavior.

### Working with code signing

- [- setCodeSigningRequirement:](<nsxpcconnection/setcodesigningrequirement(__).md>) — Sets the code signing requirement for this connection.

### Error codes

- [NSXPCConnectionInterrupted](nsxpcconnectioninterrupted-swift.var.md) — The XPC connection was interrupted.
- [NSXPCConnectionInvalid](nsxpcconnectioninvalid-swift.var.md) — The XPC connection was invalid.
- [NSXPCConnectionReplyInvalid](nsxpcconnectionreplyinvalid-swift.var.md) — The XPC connection reply was invalid.
- [NSXPCConnectionErrorMinimum](nsxpcconnectionerrorminimum-swift.var.md) — The lower bounds of XPC connection error code values.
- [NSXPCConnectionErrorMaximum](nsxpcconnectionerrormaximum-swift.var.md) — The upper bounds of XPC connection error code values.
- [NSXPCConnectionCodeSigningRequirementFailure](nsxpcconnectioncodesigningrequirementfailure-swift.var.md) — A code-signing requirement check failed.

## See Also

### XPC Client

- [NSXPCProxyCreating](nsxpcproxycreating.md) — Methods for creating new proxy objects.
- [NSXPCInterface](nsxpcinterface.md) — An interface that may be sent to an exported object or remote object proxy.
- [NSXPCCoder](nsxpccoder.md) — A coder that encodes and decodes objects that your app sends over an XPC connection.
