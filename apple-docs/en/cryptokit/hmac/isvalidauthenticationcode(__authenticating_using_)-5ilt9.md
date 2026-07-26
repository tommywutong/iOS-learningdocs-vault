---
title: 'isValidAuthenticationCode(_:authenticating:using:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.2+, iPadOS 13.2+, Mac Catalyst 13.2+, macOS 10.15+, tvOS 13.2+, visionOS 1.0+, watchOS 6.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hmac/isvalidauthenticationcode(_:authenticating:using:)-5ilt9'
source_url: 'https://developer.apple.com/documentation/cryptokit/hmac/isvalidauthenticationcode(_:authenticating:using:)-5ilt9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hmac/isvalidauthenticationcode%28_%3Aauthenticating%3Ausing%3A%29-5ilt9.json'
content_hash: 'sha256:c447a292fae6191c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HMAC](../hmac.md)

# isValidAuthenticationCode(_:authenticating:using:)

<sub>Type Method</sub>

Returns a Boolean value indicating whether the given message authentication code represented as contiguous bytes is valid for a block of data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func isValidAuthenticationCode<C, D>(_ authenticationCode: C, authenticating authenticatedData: D, using key: SymmetricKey) -> Bool where C : ContiguousBytes, D : DataProtocol
```

## Parameters

- `authenticationCode` — The authentication code to compare.

- `authenticatedData` — The block of data to compare.

- `key` — The symmetric key for the authentication code.

## Return Value

A Boolean value that’s `true` if the message authentication code is valid for the specified block of data.

## See Also

### Checking an authentication code

- [isValidAuthenticationCode(_:authenticating:using:)](<isvalidauthenticationcode(__authenticating_using_)-8ezmw.md>) — Returns a Boolean value indicating whether the given message authentication code is valid for a block of data.
- [isValidAuthenticationCode(_:authenticating:using:)](<isvalidauthenticationcode(__authenticating_using_)-5jbc8.md>) — Returns a Boolean value indicating whether the given message authentication code is valid for a block of data stored in a buffer.
