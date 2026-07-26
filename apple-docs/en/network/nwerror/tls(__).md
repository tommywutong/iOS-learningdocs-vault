---
title: 'NWError.tls(_:)'
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwerror/tls(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwerror/tls(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwerror/tls%28_%3A%29.json'
content_hash: 'sha256:71c6e0a3ab4fbd6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWError](../nwerror.md)

# NWError.tls(_:)

<sub>Case</sub>

A TLS error reported by a TLS connection or listener.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case tls(OSStatus)
```

## See Also

### Checking Error Types

- [NWError.posix(_:)](<posix(__).md>) — A POSIX error, which is used for most network protocol and routing errors.
- [NWError.dns(_:)](<dns(__).md>) — A DNS error encountered in resolving, browsing, or advertising.
