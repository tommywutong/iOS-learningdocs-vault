---
title: countOfBytesExpectedToSend
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/countofbytesexpectedtosend
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/countofbytesexpectedtosend'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/countofbytesexpectedtosend.json'
content_hash: 'sha256:c0f9159d43b1625f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTask](../urlsessiontask.md)

# countOfBytesExpectedToSend

<sub>Instance Property</sub>

The number of bytes that the task expects to send in the request body.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var countOfBytesExpectedToSend: Int64 { get }
```

## Discussion

The URL loading system can determine the length of the upload data in three ways:

- From the length of the data object provided as the upload body.
- From the length of the file on disk provided as the upload body of an upload task (_not_ a download task).
- From the `Content-Length` in the request object, if you explicitly set it.

Otherwise, the value is [NSURLSessionTransferSizeUnknown](../nsurlsessiontransfersizeunknown.md) (`-1`) if you provided a stream or body data object, or zero (`0`) if you did not.

## See Also

### Obtaining task progress

- [progress](progress.md) — A representation of the overall task progress.
- [countOfBytesExpectedToReceive](countofbytesexpectedtoreceive.md) — The number of bytes that the task expects to receive in the response body.
- [countOfBytesReceived](countofbytesreceived.md) — The number of bytes that the task has received from the server in the response body.
- [countOfBytesSent](countofbytessent.md) — The number of bytes that the task has sent to the server in the request body.
- [NSURLSessionTransferSizeUnknown](../nsurlsessiontransfersizeunknown.md) — The total size of the transfer cannot be determined.
