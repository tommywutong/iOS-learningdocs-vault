---
title: 'init(privateKey:ciphersuite:info:encapsulatedKey:authenticatedBy:presharedKey:presharedKeyIdentifier:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hpke/recipient/init(privatekey:ciphersuite:info:encapsulatedkey:authenticatedby:presharedkey:presharedkeyidentifier:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/hpke/recipient/init(privatekey:ciphersuite:info:encapsulatedkey:authenticatedby:presharedkey:presharedkeyidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpke/recipient/init%28privatekey%3Aciphersuite%3Ainfo%3Aencapsulatedkey%3Aauthenticatedby%3Apresharedkey%3Apresharedkeyidentifier%3A%29.json'
content_hash: 'sha256:fbc8b164346da9a7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [HPKE](../../hpke.md) · [Recipient](../recipient.md)

# init(privateKey:ciphersuite:info:encapsulatedKey:authenticatedBy:presharedKey:presharedKeyIdentifier:)

<sub>Initializer</sub>

Creates a recipient in authentication and preshared key mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<SK>(privateKey: SK, ciphersuite: HPKE.Ciphersuite, info: Data, encapsulatedKey: Data, authenticatedBy authenticationKey: SK.PublicKey, presharedKey psk: SymmetricKey, presharedKeyIdentifier pskID: Data) throws where SK : HPKEDiffieHellmanPrivateKey
```

## Parameters

- `privateKey` — The recipient’s private key for decrypting the incoming messages.

- `ciphersuite` — The cipher suite that defines the cryptographic algorithms to use.

- `info` — Data that the key derivation function uses to compute the symmetric key material. The sender and the recipient need to use the same `info` data.

- `encapsulatedKey` — The encapsulated symmetric key that the sender provides.

- `authenticationKey` — The sender’s public key for authenticating the messages.

- `psk` — A preshared key (PSK) that the sender and the recipient both hold.

- `pskID` — An identifier for the PSK.

## Discussion

The `Receiver` decrypts messages it receives in authentication and preshared key (`auth_psk`) mode using the encapsulated key with the key schedule information (`info` data), in addition to a symmetric encryption key that the sender and recipient both know in advance. Messages also include authentication data so that the recipient can verify the authenticity of the sender’s private key.

> [!note] Note
> The system throws errors from [Errors](../errors.md) when it encounters them.
