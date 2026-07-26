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
doc_path: /documentation/cryptokit/insecure/sha1/finalize()
source_url: 'https://developer.apple.com/documentation/cryptokit/insecure/sha1/finalize()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/insecure/sha1/finalize%28%29.json'
content_hash: 'sha256:9910f14e750bb36f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [Insecure](../../insecure.md) · [SHA1](../sha1.md)

# finalize()

<sub>Instance Method</sub>

Finalizes the hash function and returns the computed digest.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func finalize() -> Insecure.SHA1.Digest
```

## Return Value

The computed digest of the data.

## Discussion

Call this method after you provide the hash function with all the data to hash by making one or more calls to the `update(data:)` or [update(bufferPointer:)](<update(bufferpointer_).md>) method. After finalizing the hash function, discard it. To compute a new digest, create a new hash function with a call to the [init()](<init().md>) method.

## See Also

### Computing a hash iteratively

- [init()](<init().md>) — Creates a SHA1 hash function.
- [update(bufferPointer:)](<update(bufferpointer_).md>) — Incrementally updates the hash function with the contents of the buffer.
