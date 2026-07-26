---
title: OutputStream
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/outputstream
source_url: 'https://developer.apple.com/documentation/foundation/outputstream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/outputstream.json'
content_hash: 'sha256:a5238f020d0061e7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# OutputStream

<sub>Class</sub>

A stream that provides write-only stream functionality.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class OutputStream
```

## Overview

[OutputStream](outputstream.md) is “toll-free bridged” with its Core Foundation counterpart, [CFWriteStream](../corefoundation/cfwritestream.md). For more information on toll-free bridging, see [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2).

### Subclassing Notes

`NSOutputStream` is a concrete subclass of `NSStream` that lets you write data to a stream. Although `NSOutputStream` is probably sufficient for most situations requiring this capability, you can create a subclass of `NSOutputStream` if you want more specialized behavior (for example, you want to record statistics on the data in a stream).

#### Methods to Override

To create a subclass of `NSOutputStream` you may have to implement initializers for the type of stream data supported and suitably reimplement existing initializers. You must also provide complete implementations of the following methods:

- [- write:maxLength:](<outputstream/write(__maxlength_).md>)

From the current write pointer, take up to the number of bytes specified in the `maxLength:` parameter from the client-supplied buffer (first parameter) and put them onto the stream. The buffer must be of the size specified by the second parameter. To prepare for the next operation, offset the write pointer by the number of bytes written. Return a signed integer based on the outcome of the current operation:

- If the write operation is successful, return the actual number of bytes put onto the stream.
- If the stream is of a fixed length and has reached its capacity, return `0`.
- If there was an error writing to the stream, return `-1`.
- [hasSpaceAvailable](outputstream/hasspaceavailable.md)

Return [true](../swift/true.md) if the stream can currently accept more data, [false](../swift/false.md) if it cannot. If you want to be semantically compatible with `NSOutputStream`, return [true](../swift/true.md) if a write must be attempted to determine if space is available.

## Relationships

- **Inherits From**: [Stream](stream.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating Streams

- [+ outputStreamToMemory](<outputstream/tomemory().md>) — Creates and returns an initialized output stream that will write stream data to memory.
- [- initToMemory](<outputstream/init(tomemory_).md>) — Returns an initialized output stream that will write to memory.
- [- initToBuffer:capacity:](<outputstream/init(tobuffer_capacity_).md>) — Returns an initialized output stream that can write to a provided buffer.
- [- initToFileAtPath:append:](<outputstream/init(tofileatpath_append_).md>) — Returns an initialized output stream for writing to a specified file.
- [- initWithURL:append:](<outputstream/init(url_append_)-5soau.md>) — Returns an initialized output stream for writing to a specified URL.

### Using Streams

- [hasSpaceAvailable](outputstream/hasspaceavailable.md) — A boolean value that indicates whether the receiver can be written to.
- [- write:maxLength:](<outputstream/write(__maxlength_).md>) — Writes the contents of a provided data buffer to the receiver.

### Initializers

- [init(URL:append:)](<outputstream/init(url_append_)-4dpt1.md>)

### Default Implementations

- [NSOutputStream Implementations](outputstream/nsoutputstream-implementations.md)

## See Also

### Streams

- [Stream](stream.md) — An abstract class representing a stream.
- [InputStream](inputstream.md) — A stream that provides read-only stream functionality.
- [StreamDelegate](streamdelegate.md) — An interface that delegates of a stream instance use to handle events on the stream.
