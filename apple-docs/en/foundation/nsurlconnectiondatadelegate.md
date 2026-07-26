---
title: NSURLConnectionDataDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlconnectiondatadelegate
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnectiondatadelegate.json'
content_hash: 'sha256:2cb9c83b2b9eb032'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLConnectionDataDelegate

<sub>Protocol</sub>

A protocol that most delegates of a URL connection implement to receive data associated with the connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSURLConnectionDataDelegate : NSURLConnectionDelegate
```

## Overview

The `NSURLConnectionDataDelegate` protocol describes methods that should be implemented by the delegate for an instance of the [NSURLConnection](nsurlconnection.md) class. Many methods in this protocol existed as part of an informal protocol in previous versions of macOS and iOS.

In addition to the methods described in this protocol, an `NSURLConnection` delegate should also implement the methods described in the [NSURLConnectionDelegate](nsurlconnectiondelegate.md) protocol.

> [!note] Note
> If you are using `NSURLConnection` as part of Newsstand Kit on iOS, you should also implement the methods in the [NSURLConnectionDownloadDelegate](nsurlconnectiondownloaddelegate.md) protocol.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSURLConnectionDelegate](nsurlconnectiondelegate.md)

## Topics

### Handling Incoming Data

- [- connection:didReceiveResponse:](<nsurlconnectiondatadelegate/connection(__didreceive_)-8t66w.md>) — Sent when the connection has received sufficient data to construct the URL response for its request.
- [- connection:didReceiveData:](<nsurlconnectiondatadelegate/connection(__didreceive_)-8p5vg.md>) — Sent as a connection loads data incrementally.

### Receiving Connection Progress

- [- connection:didSendBodyData:totalBytesWritten:totalBytesExpectedToWrite:](<nsurlconnectiondatadelegate/connection(__didsendbodydata_totalbyteswritten_totalbytesexpectedtowrite_).md>) — Sent as the body (message data) of a request is transmitted (such as in an HTTP POST request).
- [- connectionDidFinishLoading:](<nsurlconnectiondatadelegate/connectiondidfinishloading(__).md>) — Sent when a connection has finished loading successfully.

### Handling Redirects

- [- connection:willSendRequest:redirectResponse:](<nsurlconnectiondatadelegate/connection(__willsend_redirectresponse_).md>) — Sent when the connection determines that it must change URLs in order to continue loading a request.
- [- connection:needNewBodyStream:](<nsurlconnectiondatadelegate/connection(__neednewbodystream_).md>) — Called when an `NSURLConnection` needs to retransmit a request that has a body stream to provide a new, unopened stream.

### Overriding Caching Behavior

- [- connection:willCacheResponse:](<nsurlconnectiondatadelegate/connection(__willcacheresponse_).md>) — Sent before the connection stores a cached response in the cache, to give the delegate an opportunity to alter it.

## See Also

### URL Connection

- [NSURLConnection](nsurlconnection.md) — An object that enables you to start and stop URL requests.
- [NSURLConnectionDelegate](nsurlconnectiondelegate.md) — A protocol that delegates of a URL connection implement to receive status about and provide feedback to the connection object.
- [NSURLConnectionDownloadDelegate](nsurlconnectiondownloaddelegate.md) — A protocol that delegates of a URL connection created with Newsstand Kit implement to receive data associated with a download.
