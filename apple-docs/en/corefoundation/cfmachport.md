---
title: CFMachPort
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfmachport
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmachport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmachport.json'
content_hash: 'sha256:5371ee914dbf3104'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMachPort

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFMachPort
```

## Overview

A CFMachPort object is a wrapper for a native Mach port (`mach_port_t`). Mach ports are the native communication channel for the macOS kernel.

CFMachPort does not provide a function to send messages, so you primarily use a CFMachPort object if you need to listen to a Mach port that you obtained by other means. You can get a callback when a message arrives on the port or when the port becomes invalid, such as when the native port dies.

To listen for messages you need to create a run loop source with [CFMachPortCreateRunLoopSource](<cfmachportcreaterunloopsource(______).md>) and add it to a run loop with [CFRunLoopAddSource](<cfrunloopaddsource(______).md>).

> [!important] Important
> If you want to tear down the connection, you must invalidate the port (using [CFMachPortInvalidate](<cfmachportinvalidate(__).md>)) before releasing the runloop source and the Mach port object.

To send data, you must use the Mach APIs with the native Mach port, which is not described here. Alternatively, you can use a [CFMessagePort](cfmessageport.md) object, which can send arbitrary data.

Mach ports only support communication on the local machine. For network communication, you have to use a [CFSocket](cfsocket.md) object.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a CFMachPort Object

- [CFMachPortCreate](<cfmachportcreate(________).md>) — Creates a CFMachPort object with a new Mach port.
- [CFMachPortCreateWithPort](<cfmachportcreatewithport(__________).md>) — Creates a CFMachPort object for a pre-existing native Mach port.

### Configuring a CFMachPort Object

- [CFMachPortInvalidate](<cfmachportinvalidate(__).md>) — Invalidates a CFMachPort object, stopping it from receiving any more messages.
- [CFMachPortCreateRunLoopSource](<cfmachportcreaterunloopsource(______).md>) — Creates a CFRunLoopSource object for a CFMachPort object.
- [CFMachPortSetInvalidationCallBack](<cfmachportsetinvalidationcallback(____).md>) — Sets the callback function invoked when a CFMachPort object is invalidated.

### Examining a CFMachPort Object

- [CFMachPortGetContext](<cfmachportgetcontext(____).md>) — Returns the context information for a CFMachPort object.
- [CFMachPortGetInvalidationCallBack](<cfmachportgetinvalidationcallback(__).md>) — Returns the invalidation callback function for a CFMachPort object.
- [CFMachPortGetPort](<cfmachportgetport(__).md>) — Returns the native Mach port represented by a CFMachPort object.
- [CFMachPortIsValid](<cfmachportisvalid(__).md>) — Returns a Boolean value that indicates whether a CFMachPort object is valid and able to receive messages.

### Getting the CFMachPort Type ID

- [CFMachPortGetTypeID](<cfmachportgettypeid().md>) — Returns the type identifier for the CFMachPort opaque type.

### Callbacks

- [CFMachPortCallBack](cfmachportcallback.md) — Callback invoked to process a message received on a CFMachPort object.
- [CFMachPortInvalidationCallBack](cfmachportinvalidationcallback.md) — Callback invoked when a CFMachPort object is invalidated.

### Data Types

- [CFMachPortContext](cfmachportcontext.md) — A structure that contains program-defined data and callbacks with which you can configure a CFMachPort object’s behavior.

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
