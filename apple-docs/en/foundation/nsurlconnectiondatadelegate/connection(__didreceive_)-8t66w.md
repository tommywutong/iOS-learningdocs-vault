---
title: 'connection(_:didReceive:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlconnectiondatadelegate/connection(_:didreceive:)-8t66w'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/connection(_:didreceive:)-8t66w'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnectiondatadelegate/connection%28_%3Adidreceive%3A%29-8t66w.json'
content_hash: 'sha256:508d3e34cf22dd1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnectionDataDelegate](../nsurlconnectiondatadelegate.md)

# connection(_:didReceive:)

<sub>Instance Method</sub>

Sent when the connection has received sufficient data to construct the URL response for its request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func connection(_ connection: NSURLConnection, didReceive response: URLResponse)
```

## Parameters

- `connection` — The connection sending the message.

- `response` — The URL response for the connection’s request. This object is immutable and will not be modified by the URL loading system once it is presented to the delegate.

## Discussion

In rare cases, for example in the case of an HTTP load where the content type of the load data is `multipart/x-mixed-replace`, the delegate will receive more than one `connection:didReceiveResponse:` message. When this happens, discard (or process) all data previously delivered by `connection:didReceiveData:`, and prepare to handle the next part (which could potentially have a different MIME type).

The only case where this message is not sent to the delegate is when the protocol implementation encounters an error before a response could be created.

## See Also

### Related Documentation

- [URL Loading System](../url-loading-system.md) — Interact with URLs and communicate with servers using standard Internet protocols.

### Handling Incoming Data

- [- connection:didReceiveData:](<connection(__didreceive_)-8p5vg.md>) — Sent as a connection loads data incrementally.
