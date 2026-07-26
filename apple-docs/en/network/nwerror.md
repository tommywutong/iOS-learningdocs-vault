---
title: NWError
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwerror
source_url: 'https://developer.apple.com/documentation/network/nwerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwerror.json'
content_hash: 'sha256:51513eb960dd65d9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NWError

<sub>Enumeration</sub>

The errors returned by objects in the Network framework.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NWError
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomNSError](../foundation/customnserror.md), [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Checking Error Types

- [NWError.posix(_:)](<nwerror/posix(__).md>) — A POSIX error, which is used for most network protocol and routing errors.
- [NWError.dns(_:)](<nwerror/dns(__).md>) — A DNS error encountered in resolving, browsing, or advertising.
- [NWError.tls(_:)](<nwerror/tls(__).md>) — A TLS error reported by a TLS connection or listener.

### Enumeration Cases

- [NWError.wifiAware(_:)](<nwerror/wifiaware(__).md>) — The error code will be a Wi-Fi Aware error as defined in \<WifiAware/errors.swift\>

### Instance Properties

- [wifiAware](nwerror/wifiaware.md) — The underlying error that occurred, if applicable.
