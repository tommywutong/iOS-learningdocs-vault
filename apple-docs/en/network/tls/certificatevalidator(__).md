---
title: 'certificateValidator(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/tls/certificatevalidator(_:)'
source_url: 'https://developer.apple.com/documentation/network/tls/certificatevalidator(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tls/certificatevalidator%28_%3A%29.json'
content_hash: 'sha256:621e15ff356ea1ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [TLS](../tls.md)

# certificateValidator(_:)

<sub>Instance Method</sub>

Set a closure to provide custom verification of the peer’s credentials during the TLS handshake.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func certificateValidator(_ handler: @escaping @isolated(any) @Sendable (sec_protocol_metadata_t, sec_trust_t) async -> Bool) -> TLS
```

## Discussion

This closure may be called multiple times for each connection. It should return `true` if the credentials should be trusted and the handshake should proceed, `false` otherwise.

> [!warning] Warning
> Most apps should not override the default system handling, as doing so can result in insecure network connections and major security vulnerabilities.
