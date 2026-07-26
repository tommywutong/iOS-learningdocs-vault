---
title: 'init(derRepresentation:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/p521/signing/ecdsasignature/init(derrepresentation:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/p521/signing/ecdsasignature/init(derrepresentation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p521/signing/ecdsasignature/init%28derrepresentation%3A%29.json'
content_hash: 'sha256:c37c969ac8ca5f6a'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [P521](../../../p521.md) · [Signing](../../signing.md) · [ECDSASignature](../ecdsasignature.md)

# init(derRepresentation:)

<sub>Initializer</sub>

Creates a P-521 digital signature from a Distinguished Encoding Rules (DER) encoded representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<D>(derRepresentation: D) throws where D : DataProtocol
```

## Parameters

- `derRepresentation` — The DER-encoded representation of the signature.

## See Also

### Creating a signature

- [init(rawRepresentation:)](<init(rawrepresentation_).md>) — Creates a P-521 digital signature from a raw representation.
