---
title: progress
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/progress
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/progress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/progress.json'
content_hash: 'sha256:bd1fd1e9bf6096f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTask](../urlsessiontask.md)

# progress

<sub>Instance Property</sub>

A representation of the overall task progress.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var progress: Progress { get }
```

## See Also

### Obtaining task progress

- [countOfBytesExpectedToReceive](countofbytesexpectedtoreceive.md) — The number of bytes that the task expects to receive in the response body.
- [countOfBytesReceived](countofbytesreceived.md) — The number of bytes that the task has received from the server in the response body.
- [countOfBytesExpectedToSend](countofbytesexpectedtosend.md) — The number of bytes that the task expects to send in the request body.
- [countOfBytesSent](countofbytessent.md) — The number of bytes that the task has sent to the server in the request body.
- [NSURLSessionTransferSizeUnknown](../nsurlsessiontransfersizeunknown.md) — The total size of the transfer cannot be determined.
