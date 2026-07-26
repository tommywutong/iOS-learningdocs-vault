---
title: countOfBytesExpectedToReceive
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/countofbytesexpectedtoreceive
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/countofbytesexpectedtoreceive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/countofbytesexpectedtoreceive.json'
content_hash: 'sha256:2a5c542fa32320e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTask](../urlsessiontask.md)

# countOfBytesExpectedToReceive

<sub>Instance Property</sub>

The number of bytes that the task expects to receive in the response body.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var countOfBytesExpectedToReceive: Int64 { get }
```

## Discussion

This value is determined based on the `Content-Length` header received from the server. If that header is absent, the value is [NSURLSessionTransferSizeUnknown](../nsurlsessiontransfersizeunknown.md).

## See Also

### Obtaining task progress

- [progress](progress.md) — A representation of the overall task progress.
- [countOfBytesReceived](countofbytesreceived.md) — The number of bytes that the task has received from the server in the response body.
- [countOfBytesExpectedToSend](countofbytesexpectedtosend.md) — The number of bytes that the task expects to send in the request body.
- [countOfBytesSent](countofbytessent.md) — The number of bytes that the task has sent to the server in the request body.
- [NSURLSessionTransferSizeUnknown](../nsurlsessiontransfersizeunknown.md) — The total size of the transfer cannot be determined.
