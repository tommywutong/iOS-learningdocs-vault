---
title: 'NWError.dns(_:)'
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwerror/dns(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwerror/dns(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwerror/dns%28_%3A%29.json'
content_hash: 'sha256:74c5edd2a69d599f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWError](../nwerror.md)

# NWError.dns(_:)

<sub>Case</sub>

A DNS error encountered in resolving, browsing, or advertising.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case dns(DNSServiceErrorType)
```

## See Also

### Checking Error Types

- [NWError.posix(_:)](<posix(__).md>) — A POSIX error, which is used for most network protocol and routing errors.
- [NWError.tls(_:)](<tls(__).md>) — A TLS error reported by a TLS connection or listener.
