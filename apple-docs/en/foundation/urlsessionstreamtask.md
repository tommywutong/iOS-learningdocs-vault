---
title: URLSessionStreamTask
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionstreamtask
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionstreamtask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionstreamtask.json'
content_hash: 'sha256:750055077347c571'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLSessionStreamTask

<sub>Class</sub>

A URL session task that is stream-based.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class URLSessionStreamTask
```

## Overview

[URLSessionStreamTask](urlsessionstreamtask.md) is a concrete subclass of [URLSessionTask](urlsessiontask.md). Many of the methods in the [URLSessionStreamTask](urlsessionstreamtask.md) class are documented in [URLSessionTask](urlsessiontask.md).

The [URLSessionStreamTask](urlsessionstreamtask.md) class provides an interface a TCP/IP connection created via [URLSession](urlsession.md). Tasks may be created from an [URLSession](urlsession.md) using the [- streamTaskWithHostName:port:](<urlsession/streamtask(withhostname_port_).md>) and [- streamTaskWithNetService:](<urlsession/streamtask(with_).md>) methods. They may also be created as a result of an [URLSessionDataTask](urlsessiondatatask.md) being upgraded via the HTTP `Upgrade:` response header and appropriate use of the [HTTPShouldUsePipelining](urlsessionconfiguration/httpshouldusepipelining.md) option of [URLSessionConfiguration](urlsessionconfiguration.md).

> [!note] Note
> See [RFC 2817](https://tools.ietf.org/html/rfc2817) and [RFC 6455](https://tools.ietf.org/html/rfc6455) for information about the `Upgrade:` header.

A [URLSessionStreamTask](urlsessionstreamtask.md) object performs asynchronous reads and writes, which are enqueued and executed serially, calling a handler upon completion being on the session delegate queue. If the task is canceled, all enqueued reads and writes will call their completion handlers with an appropriate error.

When working with APIs that accept [Stream](stream.md) objects, you can create [InputStream](inputstream.md) and [OutputStream](outputstream.md) objects from an [URLSessionStreamTask](urlsessionstreamtask.md) object by calling the [- captureStreams](<urlsessionstreamtask/capturestreams().md>) method.

> [!note] Note
> watchOS supports [URLSessionStreamTask](urlsessionstreamtask.md) for specific use cases. For more details, see [TN3135: Low-level networking on watchOS](../technotes/tn3135-low-level-networking-on-watchos.md).

## Relationships

- **Inherits From**: [URLSessionTask](urlsessiontask.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [ProgressReporting](progressreporting.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Reading and writing data

- [- readDataOfMinLength:maxLength:timeout:completionHandler:](<urlsessionstreamtask/readdata(ofminlength_maxlength_timeout_completionhandler_).md>) — Asynchronously reads a number of bytes from the stream, and calls a handler upon completion.
- [- writeData:timeout:completionHandler:](<urlsessionstreamtask/write(__timeout_completionhandler_).md>) — Asynchronously writes the specified data to the stream, and calls a handler upon completion.

### Capturing streams

- [- captureStreams](<urlsessionstreamtask/capturestreams().md>) — Completes any already enqueued reads and writes, and then invokes the [- URLSession:streamTask:didBecomeInputStream:outputStream:](<urlsessionstreamdelegate/urlsession(__streamtask_didbecome_outputstream_).md>) delegate message.

### Closing read and write sockets

- [- closeRead](<urlsessionstreamtask/closeread().md>) — Completes any enqueued reads and writes, and then closes the read side of the underlying socket.
- [- closeWrite](<urlsessionstreamtask/closewrite().md>) — Completes any enqueued reads and writes, and then closes the write side of the underlying socket.

### Starting and stopping secure connections

- [- startSecureConnection](<urlsessionstreamtask/startsecureconnection().md>) — Completes any enqueued reads and writes, and establishes a secure connection.
- [- stopSecureConnection](<urlsessionstreamtask/stopsecureconnection().md>) — Completes any enqueued reads and writes, and closes the secure connection. _(deprecated)_

### Initializers

- [- init](<urlsessionstreamtask/init().md>) _(deprecated)_

### Type Methods

- [+ new](<urlsessionstreamtask/new().md>) _(deprecated)_

## See Also

### Adding stream tasks to a session

- [- streamTaskWithHostName:port:](<urlsession/streamtask(withhostname_port_).md>) — Creates a task that establishes a bidirectional TCP/IP connection to a specified hostname and port.
- [- streamTaskWithNetService:](<urlsession/streamtask(with_).md>) — Creates a task that establishes a bidirectional TCP/IP connection using a specified network service. _(deprecated)_
- [URLSessionStreamDelegate](urlsessionstreamdelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to stream tasks.
