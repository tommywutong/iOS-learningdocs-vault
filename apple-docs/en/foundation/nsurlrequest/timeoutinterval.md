---
title: timeoutInterval
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlrequest/timeoutinterval
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/timeoutinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/timeoutinterval.json'
content_hash: 'sha256:ef3949e0fb21fb5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLRequest](../nsurlrequest.md)

# timeoutInterval

<sub>Instance Property</sub>

The request’s timeout interval, in seconds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timeoutInterval: TimeInterval { get }
```

## Discussion

If during a connection attempt the request remains idle for longer than the timeout interval, the request is considered to have timed out.

## See Also

### Related Documentation

- [timeoutInterval](../nsmutableurlrequest/timeoutinterval.md) — The request’s timeout interval, in seconds.

### Controlling request behavior

- [HTTPShouldHandleCookies](httpshouldhandlecookies.md) — A Boolean value that indicates whether the default cookie handling will be used for this request.
- [HTTPShouldUsePipelining](httpshouldusepipelining.md) — A Boolean value that indicates whether the request should continue transmitting data before receiving a response from an earlier transmission. _(deprecated)_
- [allowsCellularAccess](allowscellularaccess.md) — A Boolean value that indicates whether the request is allowed to use the cellular radio (if present).
