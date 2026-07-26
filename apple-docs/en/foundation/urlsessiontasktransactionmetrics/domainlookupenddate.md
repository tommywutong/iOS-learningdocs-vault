---
title: domainLookupEndDate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontasktransactionmetrics/domainlookupenddate
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/domainlookupenddate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontasktransactionmetrics/domainlookupenddate.json'
content_hash: 'sha256:3af77d6e92a1504e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTaskTransactionMetrics](../urlsessiontasktransactionmetrics.md)

# domainLookupEndDate

<sub>Instance Property</sub>

The time after the name lookup was completed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var domainLookupEndDate: Date? { get }
```

## Discussion

This value will be `nil` if a persistent connection was used, or if the resource was retrieved from local resources.

## See Also

### Accessing temporal metrics

- [fetchStartDate](fetchstartdate.md) — The time when the task started fetching the resource, from the server or locally.
- [domainLookupStartDate](domainlookupstartdate.md) — The time immediately before the task started the name lookup for the resource.
- [connectStartDate](connectstartdate.md) — The time immediately before the task started establishing a TCP connection to the server.
- [secureConnectionStartDate](secureconnectionstartdate.md) — The time immediately before the task started the TLS security handshake to secure the current connection.
- [secureConnectionEndDate](secureconnectionenddate.md) — The time immediately after the security handshake completed.
- [connectEndDate](connectenddate.md) — The time immediately after the task finished establishing the connection to the server.
- [requestStartDate](requeststartdate.md) — The time immediately before the task started requesting the resource, regardless of whether it is retrieved from the server or local resources.
- [requestEndDate](requestenddate.md) — The time immediately after the task finished requesting the resource, regardless of whether it was retrieved from the server or local resources.
- [responseStartDate](responsestartdate.md) — The time immediately after the task received the first byte of the response from the server or from local resources.
- [responseEndDate](responseenddate.md) — The time immediately after the task received the last byte of the resource.
