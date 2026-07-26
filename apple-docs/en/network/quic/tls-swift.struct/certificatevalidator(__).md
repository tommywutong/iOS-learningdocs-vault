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
doc_path: '/documentation/network/quic/tls-swift.struct/certificatevalidator(_:)'
source_url: 'https://developer.apple.com/documentation/network/quic/tls-swift.struct/certificatevalidator(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/quic/tls-swift.struct/certificatevalidator%28_%3A%29.json'
content_hash: 'sha256:19bf729d9233e0a4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [QUIC](../../quic.md) · [TLS](../tls-swift.struct.md)

# certificateValidator(_:)

<sub>Instance Method</sub>

Set a block to provide custom verification of the peer’s credentials during the TLS handshake.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func certificateValidator(_ handler: @escaping @isolated(any) @Sendable (sec_protocol_metadata_t, sec_trust_t) async -> Bool) -> QUIC
```

## Discussion

This block may be called multiple times for each connection. It should return `true` if the credentials should be trusted and the handshake should proceed, `false` otherwise.

> [!warning] Warning
> Most apps should not override the default system handling, as doing so can result in insecure network connections and major security vulnerabilities.
