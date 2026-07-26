---
title: CFSocket
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfsocket
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocket'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocket.json'
content_hash: 'sha256:56d47af83d7fb4c1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocket

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFSocket
```

## Overview

A CFSocket is a communications channel implemented with a BSD socket.

For most uses of this API, you will need to include three headers:

```objc
#import <CoreFoundation/CoreFoundation.h> #include <sys/socket.h> #include <netinet/in.h>
```

CFSocket can be created from scratch with [CFSocketCreate](<cfsocketcreate(______________).md>) and [CFSocketCreateWithSocketSignature](<cfsocketcreatewithsocketsignature(__________).md>). CFSocket objects can also be created to wrap an existing BSD socket by calling [CFSocketCreateWithNative](<cfsocketcreatewithnative(__________).md>). Finally, you can create a CFSocket and connect simultaneously to a remote host by calling [CFSocketCreateConnectedToSocketSignature](<cfsocketcreateconnectedtosocketsignature(____________).md>).

To listen for messages, you need to create a run loop source with [CFSocketCreateRunLoopSource](<cfsocketcreaterunloopsource(______).md>) and add it to a run loop with [CFRunLoopAddSource](<cfrunloopaddsource(______).md>). You can select the types of socket activities, such as connection attempts or data arrivals, that cause the source to fire and invoke your CFSocket’s callback function. To send data, you store the data in a CFData and call [CFSocketSendData](<cfsocketsenddata(________).md>).

Unlike Mach and message ports, sockets support communication over a network.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating Sockets

- [CFSocketCreate](<cfsocketcreate(______________).md>) — Creates a CFSocket object of a specified protocol and type.
- [CFSocketCreateConnectedToSocketSignature](<cfsocketcreateconnectedtosocketsignature(____________).md>) — Creates a CFSocket object and opens a connection to a remote socket.
- [CFSocketCreateWithNative](<cfsocketcreatewithnative(__________).md>) — Creates a CFSocket object for a pre-existing native socket.
- [CFSocketCreateWithSocketSignature](<cfsocketcreatewithsocketsignature(__________).md>) — Creates a CFSocket object using information from a CFSocketSignature structure.

### Configuring Sockets

- [CFSocketCopyAddress](<cfsocketcopyaddress(__).md>) — Returns the local address of a CFSocket object.
- [CFSocketCopyPeerAddress](<cfsocketcopypeeraddress(__).md>) — Returns the remote address to which a CFSocket object is connected.
- [CFSocketDisableCallBacks](<cfsocketdisablecallbacks(____).md>) — Disables the callback function of a CFSocket object for certain types of socket activity.
- [CFSocketEnableCallBacks](<cfsocketenablecallbacks(____).md>) — Enables the callback function of a CFSocket object for certain types of socket activity.
- [CFSocketGetContext](<cfsocketgetcontext(____).md>) — Returns the context information for a CFSocket object.
- [CFSocketGetNative](<cfsocketgetnative(__).md>) — Returns the native socket associated with a CFSocket object.
- [CFSocketGetSocketFlags](<cfsocketgetsocketflags(__).md>) — Returns flags that control certain behaviors of a CFSocket object.
- [CFSocketSetAddress](<cfsocketsetaddress(____).md>) — Binds a local address to a CFSocket object and configures it for listening.
- [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>) — Sets flags that control certain behaviors of a CFSocket object.

### Using Sockets

- [CFSocketConnectToAddress](<cfsocketconnecttoaddress(______).md>) — Opens a connection to a remote socket.
- [CFSocketCreateRunLoopSource](<cfsocketcreaterunloopsource(______).md>) — Creates a CFRunLoopSource object for a CFSocket object.
- [CFSocketGetTypeID](<cfsocketgettypeid().md>) — Returns the type identifier for the CFSocket opaque type.
- [CFSocketInvalidate](<cfsocketinvalidate(__).md>) — Invalidates a CFSocket object, stopping it from sending or receiving any more messages.
- [CFSocketIsValid](<cfsocketisvalid(__).md>) — Returns a Boolean value that indicates whether a CFSocket object is valid and able to send or receive messages.
- [CFSocketSendData](<cfsocketsenddata(________).md>) — Sends data over a CFSocket object.

### Callbacks

- [CFSocketCallBack](cfsocketcallback.md) — Callback invoked when certain types of activity takes place on a CFSocket object.

### Data Types

- [CFSocketContext](cfsocketcontext.md) — A structure that contains program-defined data and callbacks with which you can configure a CFSocket object’s behavior.
- [CFSocketNativeHandle](cfsocketnativehandle.md) — Type for the platform-specific native socket handle.
- [CFSocketSignature](cfsocketsignature.md) — A structure that fully specifies the communication protocol and connection address of a CFSocket object.

### Constants

- [CFSocketCallBackType](cfsocketcallbacktype.md) — Types of socket activity that can cause the callback function of a CFSocket object to be called.
- [CFSocket Flags](1560944-cfsocket-flags.md) — Flags that can be set on a CFSocket object to control its behavior.
- [CFSocketError](cfsocketerror.md) — Error codes for many CFSocket functions.

## See Also

### Related Documentation

- [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)
- [CFNetwork Programming Guide](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/CFNetwork/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001132)

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFBundle](cfbundle.md)
- [CFCalendar](cfcalendar.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
