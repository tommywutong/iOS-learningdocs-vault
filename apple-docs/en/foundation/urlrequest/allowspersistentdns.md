---
title: allowsPersistentDNS
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlrequest/allowspersistentdns
source_url: 'https://developer.apple.com/documentation/foundation/urlrequest/allowspersistentdns'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlrequest/allowspersistentdns.json'
content_hash: 'sha256:cfc3eb9ca9f60b4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLRequest](../urlrequest.md)

# allowsPersistentDNS

<sub>Instance Property</sub>

`true` if the request is allowed to store and use DNS answers, potentially beyond TTL expiry, in a persistent per-process cache, `false` otherwise. Defaults to `false`. This should only be set to `true` for hostnames whose resolutions are not expected to change across networks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allowsPersistentDNS: Bool { get set }
```

## See Also

### Controlling request behavior

- [timeoutInterval](timeoutinterval.md) — The timeout interval of the request.
- [httpShouldHandleCookies](httpshouldhandlecookies.md) — A Boolean value indicating whether cookies will be sent with and set for this request.
- [httpShouldUsePipelining](httpshouldusepipelining.md) — A Boolean value indicating whether the request should transmit before the previous response is received. _(deprecated)_
- [allowsCellularAccess](allowscellularaccess.md) — A Boolean value indicating whether the request is allowed to use the built-in cellular radios to satisfy the request.
- [assumesHTTP3Capable](assumeshttp3capable.md) — `true` if server endpoint is known to support HTTP/3. Enables QUIC racing without HTTP/3 service discovery. Defaults to `false`. The default may be `true` in a future OS update.
- [cookiePartitionIdentifier](cookiepartitionidentifier.md)
- [requiresDNSSECValidation](requiresdnssecvalidation.md) — `true` if the request is required to do DNSSEC validation during DNS lookup. `false` otherwise. Defaults to `false`.
