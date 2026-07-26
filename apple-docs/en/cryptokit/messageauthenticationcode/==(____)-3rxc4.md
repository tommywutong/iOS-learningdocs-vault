---
title: '==(_:_:)'
framework: Apple CryptoKit
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/messageauthenticationcode/==(_:_:)-3rxc4'
source_url: 'https://developer.apple.com/documentation/cryptokit/messageauthenticationcode/==(_:_:)-3rxc4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/messageauthenticationcode/%3D%3D%28_%3A_%3A%29-3rxc4.json'
content_hash: 'sha256:07683a1eb9a5cef3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [MessageAuthenticationCode](../messageauthenticationcode.md)

# ==(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether a message authentication code is equivalent to a collection of binary data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func == <D>(lhs: Self, rhs: D) -> Bool where D : DataProtocol
```

## Parameters

- `lhs` — A message authentication code to compare.

- `rhs` — A collection of binary data to compare.

## Return Value

A Boolean value that’s `true` if the message authentication code and the collection of binary data are equivalent.

## See Also

### Comparing codes

- [==(_:_:)](<==(____)-b90.md>) — Returns a Boolean value indicating whether two message authentication codes are equal.
