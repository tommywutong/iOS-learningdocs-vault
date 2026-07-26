---
title: NSURLConnectionDownloadDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlconnectiondownloaddelegate
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnectiondownloaddelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnectiondownloaddelegate.json'
content_hash: 'sha256:e06555eea221de6f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLConnectionDownloadDelegate

<sub>Protocol</sub>

A protocol that delegates of a URL connection created with Newsstand Kit implement to receive data associated with a download.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSURLConnectionDownloadDelegate : NSURLConnectionDelegate
```

## Overview

The `NSURLConnectionDownloadDelegate` protocol describes methods that should be implemented by the delegate of instances of `NSURLConnection` created using Newsstand Kit’s `download(with:)` method. The methods in this protocol provide progress information about the download of a URL asset and, when downloading concludes, provide a file URL where the downloaded file can be accessed.

In addition to the methods described in this protocol, an `NSURLConnection` delegate should also implement the methods described in the [NSURLConnectionDelegate](nsurlconnectiondelegate.md) protocol.

> [!note] Note
> If you are using `NSURLConnection` directly, your delegate class should instead implement the methods defined in the [NSURLConnectionDataDelegate](nsurlconnectiondatadelegate.md) protocol.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSURLConnectionDelegate](nsurlconnectiondelegate.md)

## Topics

### Managing Downloads of URL Assets

- [- connection:didWriteData:totalBytesWritten:expectedTotalBytes:](<nsurlconnectiondownloaddelegate/connection(__didwritedata_totalbyteswritten_expectedtotalbytes_).md>) — Sent to the delegate to deliver progress information for a download of a URL asset to a destination file.
- [- connectionDidResumeDownloading:totalBytesWritten:expectedTotalBytes:](<nsurlconnectiondownloaddelegate/connectiondidresumedownloading(__totalbyteswritten_expectedtotalbytes_).md>) — Sent to the delegate when an URL connection resumes downloading a URL asset that was earlier suspended.
- [- connectionDidFinishDownloading:destinationURL:](<nsurlconnectiondownloaddelegate/connectiondidfinishdownloading(__destinationurl_).md>) — Sent to the delegate when the URL connection has successfully downloaded the URL asset to a destination file.

## See Also

### URL Connection

- [NSURLConnection](nsurlconnection.md) — An object that enables you to start and stop URL requests.
- [NSURLConnectionDelegate](nsurlconnectiondelegate.md) — A protocol that delegates of a URL connection implement to receive status about and provide feedback to the connection object.
- [NSURLConnectionDataDelegate](nsurlconnectiondatadelegate.md) — A protocol that most delegates of a URL connection implement to receive data associated with the connection.
