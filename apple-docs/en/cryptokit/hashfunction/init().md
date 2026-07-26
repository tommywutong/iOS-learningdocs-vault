---
title: init()
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/hashfunction/init()
source_url: 'https://developer.apple.com/documentation/cryptokit/hashfunction/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hashfunction/init%28%29.json'
content_hash: 'sha256:f19b727e0c92aac1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HashFunction](../hashfunction.md)

# init()

<sub>Initializer</sub>

Creates a hash function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## Discussion

Initialize a new hash function by calling this method if you want to hash the data iteratively, such as when you don’t have a buffer large enough to hold all the data at once. Provide data blocks to the hash function using the [update(data:)](<update(data_).md>) or [update(bufferPointer:)](<update(bufferpointer_).md>) method. After providing all the data, call [finalize()](<finalize().md>) to get the digest.

If your data fits into a single buffer, you can use the [hash(data:)](<hash(data_).md>) method instead to compute the digest in a single call.

## See Also

### Computing a hash iteratively

- [update(data:)](<update(data_).md>) — Incrementally updates the hash function with the given data.
- [update(bufferPointer:)](<update(bufferpointer_).md>) — Incrementally updates the hash function with the contents of the buffer.
- [finalize()](<finalize().md>) — Finalizes the hash function and returns the computed digest.
