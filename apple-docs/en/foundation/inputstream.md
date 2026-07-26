---
title: InputStream
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/inputstream
source_url: 'https://developer.apple.com/documentation/foundation/inputstream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/inputstream.json'
content_hash: 'sha256:4594fd5ec2b31584'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# InputStream

<sub>Class</sub>

A stream that provides read-only stream functionality.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class InputStream
```

## Overview

[InputStream](inputstream.md) is “toll-free bridged” with its Core Foundation counterpart, [CFReadStream](../corefoundation/cfreadstream.md). For more information on toll-free bridging, see [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2).

### Subclassing Notes

`NSInputStream` is an abstract superclass of a _class cluster_ consisting of concrete subclasses of `NSStream` that provide standard read-only access to stream data. Although `NSInputStream` is probably sufficient for most situations requiring access to stream data, you can create a subclass of `NSInputStream` if you want more specialized behavior (for example, you want to record statistics on the data in a stream).

#### Methods to Override

To create a subclass of `NSInputStream` you may have to implement initializers for the type of stream data supported and suitably re-implement existing initializers. You must also provide complete implementations of the following methods:

- [- read:maxLength:](<inputstream/read(__maxlength_).md>)

From the current read index, take up to the number of bytes specified in the second parameter from the stream and place them in the client-supplied buffer (first parameter). The buffer must be of the size specified by the second parameter. Return the actual number of bytes placed in the buffer; if there is nothing left in the stream, return `0`. Reset the index into the stream for the next read operation.

- [- getBuffer:length:](<inputstream/getbuffer(__length_).md>)

Return in 0(1) a pointer to the subclass-allocated buffer (first parameter). Return by reference in the second parameter the number of bytes actually put into the buffer. The buffer’s contents are valid only until the next stream operation. Return [false](../swift/false.md) if you cannot access data in the buffer; otherwise, return [true](../swift/true.md). If this method is not appropriate for your type of stream, you may return [false](../swift/false.md).

- [hasBytesAvailable](inputstream/hasbytesavailable.md)

Return [true](../swift/true.md) if there is more data to read in the stream, [false](../swift/false.md) if there is not. If you want to be semantically compatible with `NSInputStream`, return [true](../swift/true.md) if a read must be attempted to determine if bytes are available.

## Relationships

- **Inherits From**: [Stream](stream.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating Streams

- [- initWithData:](<inputstream/init(data_).md>) — Initializes and returns an `NSInputStream` object for reading from a given `NSData` object.
- [- initWithFileAtPath:](<inputstream/init(fileatpath_).md>) — Initializes and returns an `NSInputStream` object that reads data from the file at a given path.
- [- initWithURL:](<inputstream/init(url_)-1lfmj.md>) — Initializes and returns an `NSInputStream` object that reads data from the file at a given URL.

### Using Streams

- [- read:maxLength:](<inputstream/read(__maxlength_).md>) — Reads up to a given number of bytes into a given buffer.
- [- getBuffer:length:](<inputstream/getbuffer(__length_).md>) — Returns by reference a pointer to a read buffer and, by reference, the number of bytes available, and returns a Boolean value that indicates whether the buffer is available.
- [hasBytesAvailable](inputstream/hasbytesavailable.md) — A Boolean value that indicates whether the receiver has bytes available to read.

### Initializers

- [init(URL:)](<inputstream/init(url_)-3lbto.md>)

### Default Implementations

- [NSInputStream Implementations](inputstream/nsinputstream-implementations.md)

## See Also

### Streams

- [Stream](stream.md) — An abstract class representing a stream.
- [OutputStream](outputstream.md) — A stream that provides write-only stream functionality.
- [StreamDelegate](streamdelegate.md) — An interface that delegates of a stream instance use to handle events on the stream.
