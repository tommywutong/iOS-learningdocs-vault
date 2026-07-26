---
title: countOfBytesClientExpectsToReceive
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/countofbytesclientexpectstoreceive
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/countofbytesclientexpectstoreceive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/countofbytesclientexpectstoreceive.json'
content_hash: 'sha256:baf9a9d14572adc3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTask](../urlsessiontask.md)

# countOfBytesClientExpectsToReceive

<sub>Instance Property</sub>

A best-guess upper bound on the number of bytes the client expects to receive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var countOfBytesClientExpectsToReceive: Int64 { get set }
```

## Discussion

The value set for this property should account for the size of both HTTP response headers and the response body. If no value is specified, the system uses [NSURLSessionTransferSizeUnknown](../nsurlsessiontransfersizeunknown.md) instead. This property is used by the system to optimize the scheduling of URL session tasks. Developers are strongly encouraged to provide an approximate upper bound, or an exact byte count, if possible, rather than accept the default.

## See Also

### Scheduling tasks

- [countOfBytesClientExpectsToSend](countofbytesclientexpectstosend.md) — A best-guess upper bound on the number of bytes the client expects to send.
- [NSURLSessionTransferSizeUnknown](../nsurlsessiontransfersizeunknown.md) — The total size of the transfer cannot be determined.
- [earliestBeginDate](earliestbegindate.md) — The earliest date at which the network load should begin.
