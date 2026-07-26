---
title: 'earlyDataEnabled(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/tls/earlydataenabled(_:)'
source_url: 'https://developer.apple.com/documentation/network/tls/earlydataenabled(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tls/earlydataenabled%28_%3A%29.json'
content_hash: 'sha256:063bfb1c7835f82a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [TLS](../tls.md)

# earlyDataEnabled(_:)

<sub>Instance Method</sub>

Enable early data (0-RTT) for TLS.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func earlyDataEnabled(_ enabled: Bool) -> TLS
```

## Parameters

- `enabled` — True to enable early data, false otherwise.

## Discussion

> [!warning] Warning
> This may have security implications for application data. In particular, TLS early data is replayable by a network attacker. You must account for this when sending data before the handshake is confirmed. See RFC 8446 for more information. You MUST NOT enable fast open without a specific application profile that defines its use.
