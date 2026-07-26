---
title: Stream
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stream
source_url: 'https://developer.apple.com/documentation/foundation/stream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stream.json'
content_hash: 'sha256:f8929ad53be2f13c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Stream

<sub>Class</sub>

An abstract class representing a stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Stream
```

## Overview

This class’s interface is common to all Cocoa stream classes, including its concrete subclasses [InputStream](inputstream.md) and [OutputStream](outputstream.md).

[Stream](stream.md) objects provide an easy way to read and write data to and from a variety of media in a device-independent way. You can create stream objects for data located in memory, in a file, or on a network (using sockets), and you can use stream objects without loading all of the data into memory at once.

By default, [Stream](stream.md) instances that aren’t file-based are non-seekable, one-way streams (although custom seekable subclasses are possible). After you provide or consume data, you can’t retrieve the data from the stream.

### Subclassing Notes

[Stream](stream.md) is an abstract class, incapable of instantiation and intended for you to subclass it. It publishes a programmatic interface that all subclasses must adopt and provide implementations for. The two Apple-provided concrete subclasses of [Stream](stream.md), [InputStream](inputstream.md) and [OutputStream](outputstream.md), are suitable for most purposes. However, there might be situations when you want a peer subclass to [InputStream](inputstream.md) and [OutputStream](outputstream.md). For example, you might want a class that implements a full-duplex (two-way) stream, or a class whose instances are capable of seeking through a stream.

#### Methods to Override

All subclasses must fully implement the following methods:

- [- open](<stream/open().md>) and [- close](<stream/close().md>)

Implement [- open](<stream/open().md>) to open the stream for reading or writing and make the stream available to the client directly or, if the stream object is scheduled on a run loop, to the delegate. Implement [- close](<stream/close().md>) to close the stream and remove the stream object from the run loop, if necessary. A closed stream should still be able to accept new properties and report its current properties. Once you close a stream, you can’t reopen it.

- [delegate](stream/delegate.md)

Return and set the delegate. By a default, a stream object must be its own delegate; so a [delegate](stream/delegate.md) message with an argument of `nil` should restore this delegate. Don’t retain the delegate to prevent retain cycles.

To learn about delegates and delegation, read “Delegation” in Cocoa Fundamentals Guide.

- [- scheduleInRunLoop:forMode:](<stream/schedule(in_formode_).md>) and [- removeFromRunLoop:forMode:](<stream/remove(from_formode_).md>)

Implement [- scheduleInRunLoop:forMode:](<stream/schedule(in_formode_).md>) to schedule the stream object on the specified run loop for the specified mode. Implement [- removeFromRunLoop:forMode:](<stream/remove(from_formode_).md>) to remove the object from the run loop. See the documentation of the [RunLoop](runloop.md) class for details. Once the stream object for an open stream is scheduled on a run loop, it is the responsibility of the subclass as it processes stream data to send [- stream:handleEvent:](<streamdelegate/stream(__handle_).md>) messages to its delegate.

- [- propertyForKey:](<stream/property(forkey_).md>) and [- setProperty:forKey:](<stream/setproperty(__forkey_).md>)

Implement these methods to return and set, respectively, the property value for the specified key. You may add custom properties, but be sure to handle all properties defined by [Stream](stream.md) as well.

- [streamStatus](stream/streamstatus.md) and [streamError](stream/streamerror.md)

Implement [streamStatus](stream/streamstatus.md) to return the current status of the stream as a [Status](stream/status.md) constant; you may define new [Status](stream/status.md) constants, but be sure to handle the system defined constants properly. Implement [streamError](stream/streamerror.md) to return an [NSError](nserror.md) object representing the current error. You might decide to return a custom [NSError](nserror.md) object that can provide complete and localized information about the error.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [InputStream](inputstream.md), [OutputStream](outputstream.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating Streams

- [+ getStreamsToHost:port:inputStream:outputStream:](<stream/getstreamsto(__port_inputstream_outputstream_).md>) — Creates and returns by reference an `NSInputStream` object and `NSOutputStream` object for a socket connection with a given host on a given port. _(deprecated)_

### Configuring Streams

- [- propertyForKey:](<stream/property(forkey_).md>) — Returns the receiver’s property for a given key.
- [- setProperty:forKey:](<stream/setproperty(__forkey_).md>) — Attempts to set the value of a given property of the receiver and returns a Boolean value that indicates whether the value is accepted by the receiver.
- [delegate](stream/delegate.md) — Sets the receiver’s delegate.

### Using Streams

- [- open](<stream/open().md>) — Opens the receiving stream.
- [- close](<stream/close().md>) — Closes the receiver.

### Managing Run Loops

- [- scheduleInRunLoop:forMode:](<stream/schedule(in_formode_).md>) — Schedules the receiver on a given run loop in a given mode.
- [- removeFromRunLoop:forMode:](<stream/remove(from_formode_).md>) — Removes the receiver from a given run loop running in a given mode.

### Getting Stream Information

- [streamStatus](stream/streamstatus.md) — Returns the receiver’s status.
- [streamError](stream/streamerror.md) — Returns an `NSError` object representing the stream error.

### Constants

- [Status](stream/status.md) — The type declared for the constants listed in doc:stream/stream_status_constants.
- [Stream Status Constants](stream_status_constants.md) — These constants indicate the current status of a stream. They are returned by [streamStatus](stream/streamstatus.md).
- [Event](stream/event.md) — Describes the constants that may be sent to the delegate as a bit field in the second parameter of [- stream:handleEvent:](<streamdelegate/stream(__handle_).md>) to specify the kind of stream event.
- [StreamNetworkServiceTypeValue](streamnetworkservicetypevalue.md) — `NSStream` defines these string constants for specifying the service type of a stream.
- [StreamSOCKSProxyConfiguration](streamsocksproxyconfiguration.md)
- [StreamSOCKSProxyVersion](streamsocksproxyversion.md)
- [StreamSocketSecurityLevel](streamsocketsecuritylevel.md) — `NSStream` defines these string constants for specifying the secure-socket layer (SSL) security level.
- [PropertyKey](stream/propertykey.md) — `NSStream` defines these string constants as keys for accessing stream properties using [- propertyForKey:](<stream/property(forkey_).md>) and setting properties with [- setProperty:forKey:](<stream/setproperty(__forkey_).md>):
- [NSStreamSocketSSLErrorDomain](nsstreamsocketsslerrordomain.md) — The error domain used by `NSError` when reporting SSL errors.
- [NSStreamSOCKSErrorDomain](nsstreamsockserrordomain.md) — The error domain used by `NSError` when reporting SOCKS errors.

### Type Methods

- [+ getBoundStreamsWithBufferSize:inputStream:outputStream:](<stream/getboundstreams(withbuffersize_inputstream_outputstream_).md>) — Creates and returns by reference a bound pair of input and output streams.
- [+ getStreamsToHostWithName:port:inputStream:outputStream:](<stream/getstreamstohost(withname_port_inputstream_outputstream_).md>) — Creates and returns by reference an `NSInputStream` object and `NSOutputStream` object for a socket connection with a given host on a given port. _(deprecated)_

## See Also

### Streams

- [InputStream](inputstream.md) — A stream that provides read-only stream functionality.
- [OutputStream](outputstream.md) — A stream that provides write-only stream functionality.
- [StreamDelegate](streamdelegate.md) — An interface that delegates of a stream instance use to handle events on the stream.
