---
title: 'certificateValidator(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/network/dtls/certificatevalidator(_:)'
source_url: 'https://developer.apple.com/documentation/network/dtls/certificatevalidator(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/dtls/certificatevalidator%28_%3A%29.json'
content_hash: 'sha256:8bc4a803a2f0e92c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [DTLS](../dtls.md)

# certificateValidator(_:)

<sub>Instance Method</sub>

Set a closure to provide custom verification of the peer’s credentials during the DTLS handshake.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func certificateValidator(_ handler: @escaping @isolated(any) @Sendable (sec_protocol_metadata_t, sec_trust_t) async -> Bool) -> DTLS
```

## Discussion

This closure may be called multiple times for each connection. It should return `true` if the credentials should be trusted and the handshake should proceed, `false` otherwise.

> [!warning] Warning
> Most apps should not override the default system handling, as doing so can result in insecure network connections and major security vulnerabilities.
