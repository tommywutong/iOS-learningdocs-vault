---
title: CFMessagePort
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfmessageport
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmessageport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmessageport.json'
content_hash: 'sha256:bb384ff550b78400'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMessagePort

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFMessagePort
```

## Overview

CFMessagePort objects provide a communications channel that can transmit arbitrary data between multiple threads or processes on the local machine.

You create a local message port with [CFMessagePortCreateLocal](<cfmessageportcreatelocal(__________).md>) and make it available to other processes by giving it a name, either when you create it or later with [CFMessagePortSetName](<cfmessageportsetname(____).md>). Other processes then connect to it using [CFMessagePortCreateRemote](<cfmessageportcreateremote(____).md>), specifying the name of the port.

To listen for messages, you need to create a run loop source with [CFMessagePortCreateRunLoopSource](<cfmessageportcreaterunloopsource(______).md>) and add it to a run loop with [CFRunLoopAddSource](<cfrunloopaddsource(______).md>).

> [!important] Important
> If you want to tear down the connection, you must invalidate the port (using [CFMessagePortInvalidate](<cfmessageportinvalidate(__).md>)) before releasing the runloop source and the message port object.

Your message port’s callback function will be called when a message arrives. To send data, you store the data in a CFData object and call [CFMessagePortSendRequest](<cfmessageportsendrequest(______________).md>). You can optionally have the function wait for a reply and return the reply in another CFData object.

Message ports only support communication on the local machine. For network communication, you have to use a [CFSocket](cfsocket.md) object.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a CFMessagePort Object

- [CFMessagePortCreateLocal](<cfmessageportcreatelocal(__________).md>) — Returns a local CFMessagePort object.
- [CFMessagePortCreateRemote](<cfmessageportcreateremote(____).md>) — Returns a CFMessagePort object connected to a remote port.

### Configuring a CFMessagePort Object

- [CFMessagePortCreateRunLoopSource](<cfmessageportcreaterunloopsource(______).md>) — Creates a CFRunLoopSource object for a CFMessagePort object.
- [CFMessagePortSetInvalidationCallBack](<cfmessageportsetinvalidationcallback(____).md>) — Sets the callback function invoked when a CFMessagePort object is invalidated.
- [CFMessagePortSetName](<cfmessageportsetname(____).md>) — Sets the name of a local CFMessagePort object.

### Using a Message Port

- [CFMessagePortInvalidate](<cfmessageportinvalidate(__).md>) — Invalidates a CFMessagePort object, stopping it from receiving or sending any more messages.
- [CFMessagePortSendRequest](<cfmessageportsendrequest(______________).md>) — Sends a message to a remote CFMessagePort object.
- [CFMessagePortSetDispatchQueue](<cfmessageportsetdispatchqueue(____).md>) — Schedules callbacks for the specified message port on the specified dispatch queue.

### Examining a Message Port

- [CFMessagePortGetContext](<cfmessageportgetcontext(____).md>) — Returns the context information for a CFMessagePort object.
- [CFMessagePortGetInvalidationCallBack](<cfmessageportgetinvalidationcallback(__).md>) — Returns the invalidation callback function for a CFMessagePort object.
- [CFMessagePortGetName](<cfmessageportgetname(__).md>) — Returns the name with which a CFMessagePort object is registered.
- [CFMessagePortIsRemote](<cfmessageportisremote(__).md>) — Returns a Boolean value that indicates whether a CFMessagePort object represents a remote port.
- [CFMessagePortIsValid](<cfmessageportisvalid(__).md>) — Returns a Boolean value that indicates whether a CFMessagePort object is valid and able to send or receive messages.

### Getting the CFMessagePort Type ID

- [CFMessagePortGetTypeID](<cfmessageportgettypeid().md>) — Returns the type identifier for the CFMessagePort opaque type.

### Callbacks

- [CFMessagePortCallBack](cfmessageportcallback.md) — Callback invoked to process a message received on a CFMessagePort object.
- [CFMessagePortInvalidationCallBack](cfmessageportinvalidationcallback.md) — Callback invoked when a CFMessagePort object is invalidated.

### Data Types

- [CFMessagePortContext](cfmessageportcontext.md) — A structure that contains program-defined data and callbacks with which you can configure a CFMessagePort object’s behavior.

### Constants

- [CFMessagePortSendRequest Error Codes](1561514-cfmessageportsendrequest-error-c.md) — Error codes for `CFMessagePortSendRequest`.

## See Also

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
