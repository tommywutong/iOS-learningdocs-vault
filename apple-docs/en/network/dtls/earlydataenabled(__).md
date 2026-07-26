---
title: 'earlyDataEnabled(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/network/dtls/earlydataenabled(_:)'
source_url: 'https://developer.apple.com/documentation/network/dtls/earlydataenabled(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/dtls/earlydataenabled%28_%3A%29.json'
content_hash: 'sha256:acf80056ac71242f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [DTLS](../dtls.md)

# earlyDataEnabled(_:)

<sub>Instance Method</sub>

Enable early data (0-RTT) for DTLS.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func earlyDataEnabled(_ enabled: Bool) -> DTLS
```

## Parameters

- `enabled` — True to enable early data, false otherwise.

## Discussion

> [!warning] Warning
> This may have security implications for application data. In particular, DTLS early data is replayable by a network attacker. You must account for this when sending data before the handshake is confirmed. See RFC 8446 for more information. You MUST NOT enable fast open without a specific application profile that defines its use.
