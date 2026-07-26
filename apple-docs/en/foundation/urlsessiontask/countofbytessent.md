---
title: countOfBytesSent
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/countofbytessent
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/countofbytessent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/countofbytessent.json'
content_hash: 'sha256:dae47945cbcbb0b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTask](../urlsessiontask.md)

# countOfBytesSent

<sub>Instance Property</sub>

The number of bytes that the task has sent to the server in the request body.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var countOfBytesSent: Int64 { get }
```

## Discussion

This byte count includes _only_ the length of the request body itself, not the request headers.

To be notified when this value changes, implement the [- URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:](<../urlsessiontaskdelegate/urlsession(__task_didsendbodydata_totalbytessent_totalbytesexpectedtosend_).md>) delegate method.

## See Also

### Obtaining task progress

- [progress](progress.md) — A representation of the overall task progress.
- [countOfBytesExpectedToReceive](countofbytesexpectedtoreceive.md) — The number of bytes that the task expects to receive in the response body.
- [countOfBytesReceived](countofbytesreceived.md) — The number of bytes that the task has received from the server in the response body.
- [countOfBytesExpectedToSend](countofbytesexpectedtosend.md) — The number of bytes that the task expects to send in the request body.
- [NSURLSessionTransferSizeUnknown](../nsurlsessiontransfersizeunknown.md) — The total size of the transfer cannot be determined.
