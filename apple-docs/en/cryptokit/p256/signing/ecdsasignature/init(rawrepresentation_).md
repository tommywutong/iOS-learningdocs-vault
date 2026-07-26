---
title: 'init(rawRepresentation:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/p256/signing/ecdsasignature/init(rawrepresentation:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/p256/signing/ecdsasignature/init(rawrepresentation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p256/signing/ecdsasignature/init%28rawrepresentation%3A%29.json'
content_hash: 'sha256:126f99b252d6642b'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [P256](../../../p256.md) · [Signing](../../signing.md) · [ECDSASignature](../ecdsasignature.md)

# init(rawRepresentation:)

<sub>Initializer</sub>

Creates a P-256 digital signature from a raw representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<D>(rawRepresentation: D) throws where D : DataProtocol
```

## Parameters

- `rawRepresentation` — A raw representation of the signature as a collection of contiguous bytes.

## See Also

### Creating a signature

- [init(derRepresentation:)](<init(derrepresentation_).md>) — Creates a P-256 digital signature from a Distinguished Encoding Rules (DER) encoded representation.
