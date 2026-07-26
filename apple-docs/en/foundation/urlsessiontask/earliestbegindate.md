---
title: earliestBeginDate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/earliestbegindate
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/earliestbegindate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/earliestbegindate.json'
content_hash: 'sha256:6d7325fe4a0de45f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTask](../urlsessiontask.md)

# earliestBeginDate

<sub>Instance Property</sub>

The earliest date at which the network load should begin.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var earliestBeginDate: Date? { get set }
```

## Discussion

For tasks created from background [URLSession](../urlsession.md) instances, this property indicates that the network load should not begin any earlier than this date. Setting this property does not guarantee that the load will begin at the specified date, but only that it will not begin sooner. If not specified, no start delay is used.

This property has no effect for tasks created from nonbackground sessions.

## See Also

### Scheduling tasks

- [countOfBytesClientExpectsToReceive](countofbytesclientexpectstoreceive.md) — A best-guess upper bound on the number of bytes the client expects to receive.
- [countOfBytesClientExpectsToSend](countofbytesclientexpectstosend.md) — A best-guess upper bound on the number of bytes the client expects to send.
- [NSURLSessionTransferSizeUnknown](../nsurlsessiontransfersizeunknown.md) — The total size of the transfer cannot be determined.
