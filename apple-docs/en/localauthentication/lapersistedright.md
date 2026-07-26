---
title: LAPersistedRight
framework: Local Authentication
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/localauthentication/lapersistedright
source_url: 'https://developer.apple.com/documentation/localauthentication/lapersistedright'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/localauthentication/lapersistedright.json'
content_hash: 'sha256:03b6dc4721f35568'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Local Authentication](../localauthentication.md)

# LAPersistedRight

<sub>Class</sub>

A right that gates access to a key and a secret.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class LAPersistedRight
```

## Overview

An [LAPersistedRight](lapersistedright.md) is a right that’s backed by a unique key in the Secure Enclave with an access control list that matches the authorization requirements of the right. You can access the key that backs a right to perform cryptographic operations like encryption, decryption, signing, and verification.

You can use the key that backs an [LAPersistedRight](lapersistedright.md) to perform both public key and private key operations, but private key operations — like decryption, signing, and key exchange — are only available after you authorize the right. Public key operations like encryption and verification are always available.

The following generates a right with the default authorization requirements, stores it in the [sharedStore](larightstore/shared.md) [LARightStore](larightstore.md), and exports the public key so that you can use it to verify signatures that the corresponding private key produces:

```swift
func generateClientKeys() async throws -> Data {
    let right = LARight()
    let persistedRight = try await LARightStore.shared.saveRight(right, identifier: "server-access")
    return try await persistedRight.key.publicKey.bytes
}
```

The following uses the private key associated with the right from the previous example to sign a challenge issued by a server:

```swift
func signServerChallenge(nonce: Data) async throws -> Data {
    let persistedRight = try await LARightStore.shared.right(forIdentifier: "server-access")
    try await persistedRight.authorize(localizedReason: "Access the sandcastle competition server")

    guard persistedRight.key.canSign(using: .ecdsaSignatureMessageX962SHA256) else {
        throw NSError(domain: "ExampleErrorDomain", code: -1, userInfo: [:])
    }
    
    return try await persistedRight.key.sign(nonce, algorithm: .ecdsaSignatureMessageX962SHA256)
}
```

The signature operation occurs after verifying that the user has the proper authorization and confirming that the private key supports the given signing algorithm.

## Relationships

- **Inherits From**: [LARight](laright.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing persistent data

- [key](lapersistedright/key.md) — The private key that’s persisted by the right.
- [secret](lapersistedright/secret.md) — The data kept secret by the right.

## See Also

### Persistence

- [LARightStore](larightstore.md) — A container for data protected by a right.
- [LASecret](lasecret.md) — Data that’s protected by a persisted right.
