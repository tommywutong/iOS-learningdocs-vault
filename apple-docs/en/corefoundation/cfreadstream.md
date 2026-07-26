---
title: CFReadStream
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfreadstream
source_url: 'https://developer.apple.com/documentation/corefoundation/cfreadstream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfreadstream.json'
content_hash: 'sha256:894072ae3f5b86cd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFReadStream

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFReadStream
```

## Overview

`CFReadStream` provides an interface for reading a byte stream either synchronously or asynchronously. You can create streams that read bytes from a block of memory, a file, or a generic socket. All streams need to be opened, using [CFReadStreamOpen](<cfreadstreamopen(__).md>), before reading.

Use [CFWriteStream](cfwritestream.md) for writing byte streams. The CFNetwork framework defines an additional type of stream for reading responses to HTTP requests.

CFReadStream is “toll-free bridged” with its Cocoa Foundation counterpart, [InputStream](../foundation/inputstream.md). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSInputStream *` parameter, you can pass in a CFReadStreamRef, and in a function where you see a CFReadStreamRef parameter, you can pass in an `NSInputStream` instance. Note, however, that you may have either a delegate or callbacks but not both. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a Read Stream

- [CFReadStreamCreateWithBytesNoCopy](<cfreadstreamcreatewithbytesnocopy(________).md>) — Creates a readable stream for a block of memory.
- [CFReadStreamCreateWithFile](<cfreadstreamcreatewithfile(____).md>) — Creates a readable stream for a file.

### Opening and Closing a Read Stream

- [CFReadStreamClose](<cfreadstreamclose(__).md>) — Closes a readable stream.
- [CFReadStreamOpen](<cfreadstreamopen(__).md>) — Opens a stream for reading.

### Reading from a Stream

- [CFReadStreamRead](<cfreadstreamread(______).md>) — Reads data from a readable stream.

### Scheduling a Read Stream

- [CFReadStreamScheduleWithRunLoop](<cfreadstreamschedulewithrunloop(______).md>) — Schedules a stream into a run loop.
- [CFReadStreamUnscheduleFromRunLoop](<cfreadstreamunschedulefromrunloop(______).md>) — Removes a read stream from a given run loop.

### Examining Stream Properties

- [CFReadStreamCopyProperty](<cfreadstreamcopyproperty(____).md>) — Returns the value of a property for a stream.
- [CFReadStreamGetBuffer](<cfreadstreamgetbuffer(______).md>) — Returns a pointer to a stream’s internal buffer of unread data, if possible.
- [CFReadStreamCopyError](<cfreadstreamcopyerror(__).md>) — Returns the error associated with a stream.
- [CFReadStreamGetError](<cfreadstreamgeterror(__).md>) — Returns the error status of a stream. _(deprecated)_
- [CFReadStreamGetStatus](<cfreadstreamgetstatus(__).md>) — Returns the current state of a stream.
- [CFReadStreamHasBytesAvailable](<cfreadstreamhasbytesavailable(__).md>) — Returns a Boolean value that indicates whether a readable stream has data that can be read without blocking.

### Setting Stream Properties

- [CFReadStreamSetClient](<cfreadstreamsetclient(________).md>) — Assigns a client to a stream, which receives callbacks when certain events occur.
- [CFReadStreamSetProperty](<cfreadstreamsetproperty(______).md>) — Sets the value of a property for a stream.

### Getting the CFReadStream Type ID

- [CFReadStreamGetTypeID](<cfreadstreamgettypeid().md>) — Returns the type identifier the `CFReadStream` opaque type.

### Callbacks

- [CFReadStreamClientCallBack](cfreadstreamclientcallback.md) — Callback invoked when certain types of activity takes place on a readable stream.

### Data Types

- [CFStreamClientContext](cfstreamclientcontext.md) — A structure that contains program-defined data and callbacks with which you can configure a stream’s client behavior.

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
