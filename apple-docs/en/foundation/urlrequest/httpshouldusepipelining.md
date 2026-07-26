---
title: httpShouldUsePipelining
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（18.4 起废弃）, iPadOS 8.0+（18.4 起废弃）, Mac Catalyst 8.0+（18.4 起废弃）, macOS 10.10+（15.4 起废弃）, tvOS 9.0+（18.4 起废弃）, visionOS 1.0+（2.4 起废弃）, watchOS 2.0+（11.4 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/urlrequest/httpshouldusepipelining
source_url: 'https://developer.apple.com/documentation/foundation/urlrequest/httpshouldusepipelining'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlrequest/httpshouldusepipelining.json'
content_hash: 'sha256:a3dd5768b3240d12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLRequest](../urlrequest.md)

# httpShouldUsePipelining

<sub>Instance Property</sub>

A Boolean value indicating whether the request should transmit before the previous response is received.

> [!warning] Deprecated
> Only supported in the classic loading mode, please adopt HTTP/2 and HTTP/3 instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var httpShouldUsePipelining: Bool { get set }
```

## See Also

### Controlling request behavior

- [timeoutInterval](timeoutinterval.md) — The timeout interval of the request.
- [httpShouldHandleCookies](httpshouldhandlecookies.md) — A Boolean value indicating whether cookies will be sent with and set for this request.
- [allowsCellularAccess](allowscellularaccess.md) — A Boolean value indicating whether the request is allowed to use the built-in cellular radios to satisfy the request.
- [allowsPersistentDNS](allowspersistentdns.md) — `true` if the request is allowed to store and use DNS answers, potentially beyond TTL expiry, in a persistent per-process cache, `false` otherwise. Defaults to `false`. This should only be set to `true` for hostnames whose resolutions are not expected to change across networks.
- [assumesHTTP3Capable](assumeshttp3capable.md) — `true` if server endpoint is known to support HTTP/3. Enables QUIC racing without HTTP/3 service discovery. Defaults to `false`. The default may be `true` in a future OS update.
- [cookiePartitionIdentifier](cookiepartitionidentifier.md)
- [requiresDNSSECValidation](requiresdnssecvalidation.md) — `true` if the request is required to do DNSSEC validation during DNS lookup. `false` otherwise. Defaults to `false`.
