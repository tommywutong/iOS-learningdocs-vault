---
title: 'init(recipientKey:ciphersuite:info:authenticatedBy:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hpke/sender/init(recipientkey:ciphersuite:info:authenticatedby:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/hpke/sender/init(recipientkey:ciphersuite:info:authenticatedby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpke/sender/init%28recipientkey%3Aciphersuite%3Ainfo%3Aauthenticatedby%3A%29.json'
content_hash: 'sha256:0e08197f600b1dd5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [HPKE](../../hpke.md) · [Sender](../sender.md)

# init(recipientKey:ciphersuite:info:authenticatedBy:)

<sub>Initializer</sub>

Creates a sender in authentication mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<SK>(recipientKey: SK.PublicKey, ciphersuite: HPKE.Ciphersuite, info: Data, authenticatedBy authenticationKey: SK) throws where SK : HPKEDiffieHellmanPrivateKey
```

## Parameters

- `recipientKey` — The recipient’s public key for encrypting the messages.

- `ciphersuite` — The cipher suite that defines the cryptographic algorithms to use.

- `info` — Data that the key derivation function uses to compute the symmetric key material. The sender and the recipient need to use the same `info` data.

- `authenticationKey` — The sender’s private key for generating the HMAC.

## Discussion

The `Sender` encrypts messages in authentication mode with a symmetric encryption key. Messages also include authentication data so that the recipient can verify the authenticity of the sender’s private key.

> [!note] Note
> The system throws errors from [Errors](../errors.md) when it encounters them.
