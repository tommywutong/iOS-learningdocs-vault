---
title: URLSessionStreamDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionstreamdelegate
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionstreamdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionstreamdelegate.json'
content_hash: 'sha256:79f82c2bdb9a49b7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLSessionStreamDelegate

<sub>Protocol</sub>

A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to stream tasks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol URLSessionStreamDelegate : URLSessionTaskDelegate
```

## Overview

In addition to these methods, be sure to implement the methods in the [URLSessionTaskDelegate](urlsessiontaskdelegate.md) and [URLSessionDelegate](urlsessiondelegate.md) protocols to handle events common to all task types and session-level events, respectively.

> [!note] Note
> A [URLSession](urlsession.md) object need not have a delegate. If no delegate is assigned, a system-provided delegate is used, and you must provide a completion callback to obtain the data.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [URLSessionDelegate](urlsessiondelegate.md), [URLSessionTaskDelegate](urlsessiontaskdelegate.md)

## Topics

### Handling rerouting

- [- URLSession:betterRouteDiscoveredForStreamTask:](<urlsessionstreamdelegate/urlsession(__betterroutediscoveredfor_).md>) — Tells the delegate that a better route to the host has been detected for the stream.

### Completing stream capture

- [- URLSession:streamTask:didBecomeInputStream:outputStream:](<urlsessionstreamdelegate/urlsession(__streamtask_didbecome_outputstream_).md>) — Tells the delegate that the stream task has been completed as a result of the stream task calling the [- captureStreams](<urlsessionstreamtask/capturestreams().md>) method.

### Handling closing events

- [- URLSession:readClosedForStreamTask:](<urlsessionstreamdelegate/urlsession(__readclosedfor_).md>) — Tells the delegate that the read side of the underlying socket has been closed.
- [- URLSession:writeClosedForStreamTask:](<urlsessionstreamdelegate/urlsession(__writeclosedfor_).md>) — Tells the delegate that the write side of the underlying socket has been closed.

## See Also

### Adding stream tasks to a session

- [- streamTaskWithHostName:port:](<urlsession/streamtask(withhostname_port_).md>) — Creates a task that establishes a bidirectional TCP/IP connection to a specified hostname and port.
- [- streamTaskWithNetService:](<urlsession/streamtask(with_).md>) — Creates a task that establishes a bidirectional TCP/IP connection using a specified network service. _(deprecated)_
- [URLSessionStreamTask](urlsessionstreamtask.md) — A URL session task that is stream-based.
