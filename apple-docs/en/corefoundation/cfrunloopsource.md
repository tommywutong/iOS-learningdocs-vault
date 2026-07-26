---
title: CFRunLoopSource
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunloopsource
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopsource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopsource.json'
content_hash: 'sha256:0862f5592e6b1840'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopSource

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFRunLoopSource
```

## Overview

A CFRunLoopSource object is an abstraction of an input source that can be put into a run loop. Input sources typically generate asynchronous events, such as messages arriving on a network port or actions performed by the user.

An input source type normally defines an API for creating and operating on objects of the type, as if it were a separate entity from the run loop, then provides a function to create a CFRunLoopSource for an object. The run loop source can then be registered with the run loop and act as an intermediary between the run loop and the actual input source type object. Examples of input sources include [CFMachPort](cfmachport.md), [CFMessagePort](cfmessageport.md), and [CFSocket](cfsocket.md).

There are two categories of sources. Version 0 sources, so named because the `version` field of their context structure is 0, are managed manually by the application. When a source is ready to fire, some part of the application, perhaps code on a separate thread waiting for an event, must call [CFRunLoopSourceSignal](<cfrunloopsourcesignal(__).md>) to tell the run loop that the source is ready to fire. The run loop source for CFSocket is currently implemented as a version 0 source.

Version 1 sources are managed by the run loop and kernel. These sources use Mach ports to signal when the sources are ready to fire. A source is automatically signaled by the kernel when a message arrives on the source’s Mach port. The contents of the message are given to the source to process when the source is fired. The run loop sources for CFMachPort and CFMessagePort are currently implemented as version 1 sources.

When creating your own custom run loop source, you can choose which version works best for you.

A run loop source can be registered in multiple run loops and run loop modes at the same time. When the source is signaled, whichever run loop that happens to detect the signal first will fire the source. Adding a source to multiple threads’ run loops can be used to manage a pool of “worker” threads that is processing discrete sets of data, such as client-server messages over a network or entries in a job queue filled by a “manager” thread. As messages arrive or jobs get added to the queue, the source gets signaled and a random thread receives and processes the request.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### CFRunLoopSource Miscellaneous Functions

- [CFRunLoopSourceCreate](<cfrunloopsourcecreate(______).md>) — Creates a CFRunLoopSource object.
- [CFRunLoopSourceGetContext](<cfrunloopsourcegetcontext(____).md>) — Returns the context information for a CFRunLoopSource object.
- [CFRunLoopSourceGetOrder](<cfrunloopsourcegetorder(__).md>) — Returns the ordering parameter for a CFRunLoopSource object.
- [CFRunLoopSourceGetTypeID](<cfrunloopsourcegettypeid().md>) — Returns the type identifier of the CFRunLoopSource opaque type.
- [CFRunLoopSourceInvalidate](<cfrunloopsourceinvalidate(__).md>) — Invalidates a CFRunLoopSource object, stopping it from ever firing again.
- [CFRunLoopSourceIsValid](<cfrunloopsourceisvalid(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopSource object is valid and able to fire.
- [CFRunLoopSourceSignal](<cfrunloopsourcesignal(__).md>) — Signals a CFRunLoopSource object, marking it as ready to fire.

### Callbacks

- [cancel](cfrunloopsourcecontext/cancel.md)
- [equal](cfrunloopsourcecontext/equal.md) — An equality test callback for your program-defined `info` pointer. Can be `NULL`.
- [hash](cfrunloopsourcecontext/hash.md) — A hash calculation callback for your program-defined `info` pointer. Can be `NULL`.
- [perform](cfrunloopsourcecontext/perform.md) — A perform callback for the run loop source. This callback is called when the source has fired.
- [schedule](cfrunloopsourcecontext/schedule.md) — A scheduling callback for the run loop source. This callback is called when the source is added to a run loop mode. Can be `NULL`.

### Data Types

- [CFRunLoopSourceContext](cfrunloopsourcecontext.md) — A structure that contains program-defined data and callbacks with which you can configure a version 0 CFRunLoopSource’s behavior.
- [CFRunLoopSourceContext1](cfrunloopsourcecontext1.md) — A structure that contains program-defined data and callbacks with which you can configure a version 1 CFRunLoopSource’s behavior.

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
