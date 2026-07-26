---
title: CFWriteStream
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfwritestream
source_url: 'https://developer.apple.com/documentation/corefoundation/cfwritestream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfwritestream.json'
content_hash: 'sha256:c566fa12f9f18f1b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFWriteStream

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFWriteStream
```

## Overview

`CFWriteStream` provides an interface for writing a byte stream either synchronously or asynchronously. You can create streams that write bytes to a block of memory, a file, or a generic socket. All streams need to be opened, using [CFWriteStreamOpen](<cfwritestreamopen(__).md>), before writing.

Use [CFReadStream](cfreadstream.md) for reading byte streams, and for the functions, such as [CFStreamCreatePairWithSocketToHost](<cfstreamcreatepairwithsockettohost(__________).md>), that create socket streams).

`CFWriteStream` is “toll-free bridged” with its Cocoa Foundation counterpart, [OutputStream](../foundation/outputstream.md). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSOutputStream *` parameter, you can pass in a `CFWriteStreamRef`, and in a function where you see a `CFWriteStreamRef` parameter, you can pass in an `NSOutputStream` instance. Note, however, that you may have either a delegate or callbacks but not both. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a Write Stream

- [CFWriteStreamCreateWithAllocatedBuffers](<cfwritestreamcreatewithallocatedbuffers(____).md>) — Creates a writable stream for a growable block of memory.
- [CFWriteStreamCreateWithBuffer](<cfwritestreamcreatewithbuffer(______).md>) — Creates a writable stream for a fixed-size block of memory.
- [CFWriteStreamCreateWithFile](<cfwritestreamcreatewithfile(____).md>) — Creates a writable stream for a file.

### Opening and Closing a Stream

- [CFWriteStreamClose](<cfwritestreamclose(__).md>) — Closes a writable stream.
- [CFWriteStreamOpen](<cfwritestreamopen(__).md>) — Opens a stream for writing.

### Writing to a Stream

- [CFWriteStreamWrite](<cfwritestreamwrite(______).md>) — Writes data to a writable stream.

### Scheduling a Write Stream

- [CFWriteStreamScheduleWithRunLoop](<cfwritestreamschedulewithrunloop(______).md>) — Schedules a stream into a run loop.
- [CFWriteStreamUnscheduleFromRunLoop](<cfwritestreamunschedulefromrunloop(______).md>) — Removes a stream from a particular run loop.

### Examining Stream Properties

- [CFWriteStreamCanAcceptBytes](<cfwritestreamcanacceptbytes(__).md>) — Returns whether a writable stream can accept new data without blocking.
- [CFWriteStreamCopyProperty](<cfwritestreamcopyproperty(____).md>) — Returns the value of a property for a stream.
- [CFWriteStreamCopyError](<cfwritestreamcopyerror(__).md>) — Returns the error associated with a stream.
- [CFWriteStreamGetError](<cfwritestreamgeterror(__).md>) — Returns the error status of a stream. _(deprecated)_
- [CFWriteStreamGetStatus](<cfwritestreamgetstatus(__).md>) — Returns the current state of a stream.

### Setting Stream Properties

- [CFWriteStreamSetClient](<cfwritestreamsetclient(________).md>) — Assigns a client to a stream, which receives callbacks when certain events occur.
- [CFWriteStreamSetProperty](<cfwritestreamsetproperty(______).md>) — Sets the value of a property for a stream.

### Getting the CFWriteStream Type ID

- [CFWriteStreamGetTypeID](<cfwritestreamgettypeid().md>) — Returns the type identifier of all CFWriteStream objects.

### Callbacks

- [CFWriteStreamClientCallBack](cfwritestreamclientcallback.md) — Callback invoked when certain types of activity takes place on a writable stream.

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
