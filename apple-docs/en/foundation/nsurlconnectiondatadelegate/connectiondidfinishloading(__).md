---
title: 'connectionDidFinishLoading(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlconnectiondatadelegate/connectiondidfinishloading(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/connectiondidfinishloading(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnectiondatadelegate/connectiondidfinishloading%28_%3A%29.json'
content_hash: 'sha256:6ea7aba8b9d7f03b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnectionDataDelegate](../nsurlconnectiondatadelegate.md)

# connectionDidFinishLoading(_:)

<sub>Instance Method</sub>

Sent when a connection has finished loading successfully.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func connectionDidFinishLoading(_ connection: NSURLConnection)
```

## Parameters

- `connection` — The connection sending the message.

## Discussion

The delegate will receive no further messages for `connection`.

## See Also

### Receiving Connection Progress

- [- connection:didSendBodyData:totalBytesWritten:totalBytesExpectedToWrite:](<connection(__didsendbodydata_totalbyteswritten_totalbytesexpectedtowrite_).md>) — Sent as the body (message data) of a request is transmitted (such as in an HTTP POST request).
