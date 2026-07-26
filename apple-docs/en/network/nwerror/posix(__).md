---
title: 'NWError.posix(_:)'
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwerror/posix(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwerror/posix(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwerror/posix%28_%3A%29.json'
content_hash: 'sha256:f9ff2188cacd04eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWError](../nwerror.md)

# NWError.posix(_:)

<sub>Case</sub>

A POSIX error, which is used for most network protocol and routing errors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case posix(POSIXErrorCode)
```

## See Also

### Checking Error Types

- [NWError.dns(_:)](<dns(__).md>) — A DNS error encountered in resolving, browsing, or advertising.
- [NWError.tls(_:)](<tls(__).md>) — A TLS error reported by a TLS connection or listener.
