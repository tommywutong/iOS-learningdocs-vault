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
doc_path: '/documentation/foundation/nsurlconnectiondatadelegate/connection(_:didreceive:)-8p5vg'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/connection(_:didreceive:)-8p5vg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnectiondatadelegate/connection%28_%3Adidreceive%3A%29-8p5vg.json'
content_hash: 'sha256:430868e3dfc6fc95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnectionDataDelegate](../nsurlconnectiondatadelegate.md)

# connection(_:didReceive:)

<sub>Instance Method</sub>

Sent as a connection loads data incrementally.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func connection(_ connection: NSURLConnection, didReceive data: Data)
```

## Parameters

- `connection` — The connection sending the message.

- `data` — The newly available data. The delegate should concatenate the contents of each `data` object delivered to build up the complete data for a URL load.

## Discussion

This method provides the only way for an asynchronous delegate to retrieve the loaded data. It is the responsibility of the delegate to retain or copy this data as it is delivered.

## See Also

### Handling Incoming Data

- [- connection:didReceiveResponse:](<connection(__didreceive_)-8t66w.md>) — Sent when the connection has received sufficient data to construct the URL response for its request.
