---
title: init()
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/sha3_512/init()
source_url: 'https://developer.apple.com/documentation/cryptokit/sha3_512/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/sha3_512/init%28%29.json'
content_hash: 'sha256:c4c9988987a9928e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [SHA3_512](../sha3_512.md)

# init()

<sub>Initializer</sub>

Creates a SHA3-512 hash function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## Discussion

Initialize a new hash function by calling this method if you want to hash data iteratively, such as when you don’t have a buffer large enough to hold all the data at once. Provide data blocks to the hash function using the `update(data:)` or [update(bufferPointer:)](<update(bufferpointer_).md>) method. After providing all the data, call [finalize()](<finalize().md>) to get the digest.

If your data fits into a single buffer, you can use the `hash(data:)` method instead, to compute the digest in a single call.
