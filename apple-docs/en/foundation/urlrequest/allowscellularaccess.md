---
title: allowsCellularAccess
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlrequest/allowscellularaccess
source_url: 'https://developer.apple.com/documentation/foundation/urlrequest/allowscellularaccess'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlrequest/allowscellularaccess.json'
content_hash: 'sha256:fa25cc6e7d7a4ee5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLRequest](../urlrequest.md)

# allowsCellularAccess

<sub>Instance Property</sub>

A Boolean value indicating whether the request is allowed to use the built-in cellular radios to satisfy the request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allowsCellularAccess: Bool { get set }
```

## Discussion

Setting this property to `true` makes the request eligible to run over cellular, subject to other considerations (including, but not limited to, the [URLSessionConfiguration](../urlsessionconfiguration.md)’s [allowsCellularAccess](../urlsessionconfiguration/allowscellularaccess.md) property). Setting this value to `false` ensures that the request will never run over cellular.

## See Also

### Related Documentation

- [waitsForConnectivity](../urlsessionconfiguration/waitsforconnectivity.md) — A Boolean value that indicates whether the session should wait for connectivity to become available, or fail immediately.

### Controlling request behavior

- [timeoutInterval](timeoutinterval.md) — The timeout interval of the request.
- [httpShouldHandleCookies](httpshouldhandlecookies.md) — A Boolean value indicating whether cookies will be sent with and set for this request.
- [httpShouldUsePipelining](httpshouldusepipelining.md) — A Boolean value indicating whether the request should transmit before the previous response is received. _(deprecated)_
- [allowsPersistentDNS](allowspersistentdns.md) — `true` if the request is allowed to store and use DNS answers, potentially beyond TTL expiry, in a persistent per-process cache, `false` otherwise. Defaults to `false`. This should only be set to `true` for hostnames whose resolutions are not expected to change across networks.
- [assumesHTTP3Capable](assumeshttp3capable.md) — `true` if server endpoint is known to support HTTP/3. Enables QUIC racing without HTTP/3 service discovery. Defaults to `false`. The default may be `true` in a future OS update.
- [cookiePartitionIdentifier](cookiepartitionidentifier.md)
- [requiresDNSSECValidation](requiresdnssecvalidation.md) — `true` if the request is required to do DNSSEC validation during DNS lookup. `false` otherwise. Defaults to `false`.
