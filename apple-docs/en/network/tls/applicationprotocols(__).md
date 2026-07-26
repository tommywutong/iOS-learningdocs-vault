---
title: 'applicationProtocols(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/tls/applicationprotocols(_:)'
source_url: 'https://developer.apple.com/documentation/network/tls/applicationprotocols(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tls/applicationprotocols%28_%3A%29.json'
content_hash: 'sha256:6010fe7f77438cbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [TLS](../tls.md)

# applicationProtocols(_:)

<sub>Instance Method</sub>

Set application protocols supported by clients of this protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func applicationProtocols(_ protocols: [String]) -> TLS
```

## Discussion

Application layer protocol negotiation (ALPN) tokens describe the application protocol in use above TLS.
