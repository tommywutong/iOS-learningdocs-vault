---
title: 'exportSecret(context:outputByteCount:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hpke/sender/exportsecret(context:outputbytecount:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/hpke/sender/exportsecret(context:outputbytecount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpke/sender/exportsecret%28context%3Aoutputbytecount%3A%29.json'
content_hash: 'sha256:b2000eb32abf8eb7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [HPKE](../../hpke.md) · [Sender](../sender.md)

# exportSecret(context:outputByteCount:)

<sub>Instance Method</sub>

Exports a secret given domain-separation context and the desired output length.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func exportSecret<Context>(context: Context, outputByteCount: Int) throws -> SymmetricKey where Context : DataProtocol
```

## Parameters

- `context` — Application-specific information providing context on the use of this key.

- `outputByteCount` — The desired length of the exported secret.

## Return Value

The exported secret.
