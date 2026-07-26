---
title: 'update(bufferPointer:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hashfunction/update(bufferpointer:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/hashfunction/update(bufferpointer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hashfunction/update%28bufferpointer%3A%29.json'
content_hash: 'sha256:8448fc862918514b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HashFunction](../hashfunction.md)

# update(bufferPointer:)

<sub>Instance Method</sub>

Incrementally updates the hash function with the contents of the buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func update(bufferPointer: UnsafeRawBufferPointer)
```

## Parameters

- `bufferPointer` — A pointer to the next block of data for the ongoing digest calculation.

## Discussion

Call this method one or more times to provide data to the hash function in blocks. After providing the last block of data, call the [finalize()](<finalize().md>) method to get the computed digest. Don’t call the update method again after finalizing the hash function.

> [!note] Note
> Typically, it’s safer to use an instance of [Data](../../foundation/data.md), or some other type that conforms to the [DataProtocol](../../foundation/dataprotocol.md), to hold your data. When possible, use the [update(data:)](<update(data_).md>) method instead.

## See Also

### Computing a hash iteratively

- [init()](<init().md>) — Creates a hash function.
- [update(data:)](<update(data_).md>) — Incrementally updates the hash function with the given data.
- [finalize()](<finalize().md>) — Finalizes the hash function and returns the computed digest.
