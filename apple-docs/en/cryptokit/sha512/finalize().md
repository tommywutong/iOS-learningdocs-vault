---
title: finalize()
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/sha512/finalize()
source_url: 'https://developer.apple.com/documentation/cryptokit/sha512/finalize()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/sha512/finalize%28%29.json'
content_hash: 'sha256:00466ce0674d6b70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [SHA512](../sha512.md)

# finalize()

<sub>Instance Method</sub>

Finalizes the hash function and returns the computed digest.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func finalize() -> SHA512.Digest
```

## Return Value

The computed digest of the data.

## Discussion

Call this method after you provide the hash function with all the data to hash by making one or more calls to the `update(data:)` or [update(bufferPointer:)](<update(bufferpointer_).md>) method. After finalizing the hash function, discard it. To compute a new digest, create a new hash function with a call to the [init()](<init().md>) method.

## See Also

### Computing a hash iteratively

- [init()](<init().md>) — Creates a SHA512 hash function.
- [update(bufferPointer:)](<update(bufferpointer_).md>) — Incrementally updates the hash function with the contents of the buffer.
