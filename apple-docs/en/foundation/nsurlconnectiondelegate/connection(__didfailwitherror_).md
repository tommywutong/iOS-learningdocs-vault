---
title: 'connection(_:didFailWithError:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlconnectiondelegate/connection(_:didfailwitherror:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/connection(_:didfailwitherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnectiondelegate/connection%28_%3Adidfailwitherror%3A%29.json'
content_hash: 'sha256:ad5630929e176699'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnectionDelegate](../nsurlconnectiondelegate.md)

# connection(_:didFailWithError:)

<sub>Instance Method</sub>

Sent when a connection fails to load its request successfully.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func connection(_ connection: NSURLConnection, didFailWithError error: any Error)
```

## Parameters

- `connection` — The connection sending the message.

- `error` — An error object containing details of why the connection failed to load the request successfully.

## Discussion

Once the delegate receives this message, it will receive no further messages for `connection`.
