---
title: 'connection(_:didSendBodyData:totalBytesWritten:totalBytesExpectedToWrite:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlconnectiondatadelegate/connection(_:didsendbodydata:totalbyteswritten:totalbytesexpectedtowrite:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/connection(_:didsendbodydata:totalbyteswritten:totalbytesexpectedtowrite:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnectiondatadelegate/connection%28_%3Adidsendbodydata%3Atotalbyteswritten%3Atotalbytesexpectedtowrite%3A%29.json'
content_hash: 'sha256:dee9f7820feaa235'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnectionDataDelegate](../nsurlconnectiondatadelegate.md)

# connection(_:didSendBodyData:totalBytesWritten:totalBytesExpectedToWrite:)

<sub>Instance Method</sub>

Sent as the body (message data) of a request is transmitted (such as in an HTTP POST request).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func connection(_ connection: NSURLConnection, didSendBodyData bytesWritten: Int, totalBytesWritten: Int, totalBytesExpectedToWrite: Int)
```

## Parameters

- `connection` — The connection sending the message.

- `bytesWritten` — The number of bytes written in the latest write.

- `totalBytesWritten` — The total number of bytes written for this connection.

- `totalBytesExpectedToWrite` — The number of bytes the connection expects to write.

## Discussion

This method provides an estimate of the progress of a URL upload.

The value of `totalBytesExpectedToWrite` may change during the upload if the request needs to be retransmitted due to a lost connection or an authentication challenge from the server.

## See Also

### Receiving Connection Progress

- [- connectionDidFinishLoading:](<connectiondidfinishloading(__).md>) — Sent when a connection has finished loading successfully.
