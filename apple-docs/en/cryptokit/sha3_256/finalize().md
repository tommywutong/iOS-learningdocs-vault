---
title: finalize()
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/sha3_256/finalize()
source_url: 'https://developer.apple.com/documentation/cryptokit/sha3_256/finalize()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/sha3_256/finalize%28%29.json'
content_hash: 'sha256:182ffda696df6423'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [SHA3_256](../sha3_256.md)

# finalize()

<sub>Instance Method</sub>

Finalizes the hash function and returns the computed digest.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func finalize() -> SHA3_256.Digest
```

## Return Value

The computed digest of the data.

## Discussion

Call this method after you provide the hash function with all the data to hash by making one or more calls to the `update(data:)` or [update(bufferPointer:)](<update(bufferpointer_).md>) method. After finalizing the hash function, discard it. To compute a new digest, create a new hash function with a call to the [init()](<init().md>) method.
