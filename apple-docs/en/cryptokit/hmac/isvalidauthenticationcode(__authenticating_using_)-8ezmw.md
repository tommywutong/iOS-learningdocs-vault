---
title: 'isValidAuthenticationCode(_:authenticating:using:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hmac/isvalidauthenticationcode(_:authenticating:using:)-8ezmw'
source_url: 'https://developer.apple.com/documentation/cryptokit/hmac/isvalidauthenticationcode(_:authenticating:using:)-8ezmw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hmac/isvalidauthenticationcode%28_%3Aauthenticating%3Ausing%3A%29-8ezmw.json'
content_hash: 'sha256:f95e4e7c18638eb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HMAC](../hmac.md)

# isValidAuthenticationCode(_:authenticating:using:)

<sub>Type Method</sub>

Returns a Boolean value indicating whether the given message authentication code is valid for a block of data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func isValidAuthenticationCode<D>(_ authenticationCode: HMAC<H>.MAC, authenticating authenticatedData: D, using key: SymmetricKey) -> Bool where D : DataProtocol
```

## Parameters

- `authenticationCode` — The authentication code to compare.

- `authenticatedData` — The block of data to compare.

- `key` — The symmetric key for the authentication code.

## Return Value

A Boolean value that’s `true` if the message authentication code is valid for the specified block of data.

## See Also

### Checking an authentication code

- [isValidAuthenticationCode(_:authenticating:using:)](<isvalidauthenticationcode(__authenticating_using_)-5jbc8.md>) — Returns a Boolean value indicating whether the given message authentication code is valid for a block of data stored in a buffer.
- [isValidAuthenticationCode(_:authenticating:using:)](<isvalidauthenticationcode(__authenticating_using_)-5ilt9.md>) — Returns a Boolean value indicating whether the given message authentication code represented as contiguous bytes is valid for a block of data.
