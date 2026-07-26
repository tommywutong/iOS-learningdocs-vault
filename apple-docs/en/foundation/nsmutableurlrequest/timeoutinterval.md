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
doc_path: /documentation/foundation/nsmutableurlrequest/timeoutinterval
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableurlrequest/timeoutinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableurlrequest/timeoutinterval.json'
content_hash: 'sha256:891206e016c38c22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableURLRequest](../nsmutableurlrequest.md)

# timeoutInterval

<sub>Instance Property</sub>

The request’s timeout interval, in seconds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timeoutInterval: TimeInterval { get set }
```

## Discussion

If during a connection attempt the request remains idle for longer than the timeout interval, the request is considered to have timed out. The default timeout interval is 60 seconds.

As a general rule, you should not use short timeout intervals. Instead, you should provide an easy way for the user to cancel a long-running operation. For more information, read [Designing for Real-World Networks](https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/WhyNetworkingIsHard/WhyNetworkingIsHard.html#//apple_ref/doc/uid/TP40010220-CH13) in [Networking Overview](https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010220).

### Special considerations

In iOS versions prior to iOS 6, the minimum (and default) timeout interval for any request containing a request body was 240 seconds.

## See Also

### Controlling request behavior

- [HTTPShouldHandleCookies](httpshouldhandlecookies.md) — A Boolean value that indicates whether the request should use the default cookie handling for the request.
- [HTTPShouldUsePipelining](httpshouldusepipelining.md) — A Boolean value that indicates whether the request can continue transmitting data before receiving a response from an earlier transmission. _(deprecated)_
- [allowsCellularAccess](allowscellularaccess.md) — A Boolean value that indicates whether a connection can use the device’s cellular network (if present).
