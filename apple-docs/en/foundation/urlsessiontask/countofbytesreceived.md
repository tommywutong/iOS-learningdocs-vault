---
title: countOfBytesReceived
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/countofbytesreceived
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/countofbytesreceived'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/countofbytesreceived.json'
content_hash: 'sha256:e544faf939e448b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTask](../urlsessiontask.md)

# countOfBytesReceived

<sub>Instance Property</sub>

The number of bytes that the task has received from the server in the response body.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var countOfBytesReceived: Int64 { get }
```

## Discussion

To be notified when this value changes, implement the [- URLSession:dataTask:didReceiveData:](<../urlsessiondatadelegate/urlsession(__datatask_didreceive_).md>) delegate method (for data and upload tasks) or the [- URLSession:downloadTask:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:](<../urlsessiondownloaddelegate/urlsession(__downloadtask_didwritedata_totalbyteswritten_totalbytesexpectedtowrite_).md>) method (for download tasks).

## See Also

### Obtaining task progress

- [progress](progress.md) — A representation of the overall task progress.
- [countOfBytesExpectedToReceive](countofbytesexpectedtoreceive.md) — The number of bytes that the task expects to receive in the response body.
- [countOfBytesExpectedToSend](countofbytesexpectedtosend.md) — The number of bytes that the task expects to send in the request body.
- [countOfBytesSent](countofbytessent.md) — The number of bytes that the task has sent to the server in the request body.
- [NSURLSessionTransferSizeUnknown](../nsurlsessiontransfersizeunknown.md) — The total size of the transfer cannot be determined.
