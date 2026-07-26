---
title: 'init(privateKey:ciphersuite:info:encapsulatedKey:authenticatedBy:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hpke/recipient/init(privatekey:ciphersuite:info:encapsulatedkey:authenticatedby:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/hpke/recipient/init(privatekey:ciphersuite:info:encapsulatedkey:authenticatedby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpke/recipient/init%28privatekey%3Aciphersuite%3Ainfo%3Aencapsulatedkey%3Aauthenticatedby%3A%29.json'
content_hash: 'sha256:69bc4d4493cd8bf0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [HPKE](../../hpke.md) · [Recipient](../recipient.md)

# init(privateKey:ciphersuite:info:encapsulatedKey:authenticatedBy:)

<sub>Initializer</sub>

Creates a recipient in authentication mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<SK>(privateKey: SK, ciphersuite: HPKE.Ciphersuite, info: Data, encapsulatedKey: Data, authenticatedBy authenticationKey: SK.PublicKey) throws where SK : HPKEDiffieHellmanPrivateKey
```

## Parameters

- `privateKey` — The recipient’s private key for decrypting the incoming messages.

- `ciphersuite` — The cipher suite that defines the cryptographic algorithms to use.

- `info` — Data that the key derivation function uses to compute the symmetric key material. The sender and the recipient need to use the same `info` data.

- `encapsulatedKey` — The encapsulated symmetric key that the sender provides.

- `authenticationKey` — The sender’s public key for authenticating the messages.

## Discussion

The `Receiver` decrypts messages in authentication mode using the encapsulated key with the key schedule information (`info` data). Messages also include authentication data so that the recipient can verify the authenticity of the sender’s private key.

> [!note] Note
> The system throws errors from [Errors](../errors.md) when it encounters them.
