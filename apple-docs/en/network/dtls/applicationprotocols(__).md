---
title: 'applicationProtocols(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/network/dtls/applicationprotocols(_:)'
source_url: 'https://developer.apple.com/documentation/network/dtls/applicationprotocols(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/dtls/applicationprotocols%28_%3A%29.json'
content_hash: 'sha256:4198f61bad62eb25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [DTLS](../dtls.md)

# applicationProtocols(_:)

<sub>Instance Method</sub>

Set application protocols supported by clients of this protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func applicationProtocols(_ protocols: [String]) -> DTLS
```

## Discussion

Application layer protocol negotiation (ALPN) tokens describe the application protocol in use above DTLS.
