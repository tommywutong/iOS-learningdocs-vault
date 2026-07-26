---
title: requiresDNSSECValidation
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.1+, iPadOS 16.1+, Mac Catalyst 16.1+, macOS 13.0+, tvOS 16.1+, visionOS 1.0+, watchOS 9.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlrequest/requiresdnssecvalidation
source_url: 'https://developer.apple.com/documentation/foundation/urlrequest/requiresdnssecvalidation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlrequest/requiresdnssecvalidation.json'
content_hash: 'sha256:a859ceeed207cdb7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLRequest](../urlrequest.md)

# requiresDNSSECValidation

<sub>Instance Property</sub>

`true` if the request is required to do DNSSEC validation during DNS lookup. `false` otherwise. Defaults to `false`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var requiresDNSSECValidation: Bool { get set }
```

## See Also

### Controlling request behavior

- [timeoutInterval](timeoutinterval.md) — The timeout interval of the request.
- [httpShouldHandleCookies](httpshouldhandlecookies.md) — A Boolean value indicating whether cookies will be sent with and set for this request.
- [httpShouldUsePipelining](httpshouldusepipelining.md) — A Boolean value indicating whether the request should transmit before the previous response is received. _(deprecated)_
- [allowsCellularAccess](allowscellularaccess.md) — A Boolean value indicating whether the request is allowed to use the built-in cellular radios to satisfy the request.
- [allowsPersistentDNS](allowspersistentdns.md) — `true` if the request is allowed to store and use DNS answers, potentially beyond TTL expiry, in a persistent per-process cache, `false` otherwise. Defaults to `false`. This should only be set to `true` for hostnames whose resolutions are not expected to change across networks.
- [assumesHTTP3Capable](assumeshttp3capable.md) — `true` if server endpoint is known to support HTTP/3. Enables QUIC racing without HTTP/3 service discovery. Defaults to `false`. The default may be `true` in a future OS update.
- [cookiePartitionIdentifier](cookiepartitionidentifier.md)
