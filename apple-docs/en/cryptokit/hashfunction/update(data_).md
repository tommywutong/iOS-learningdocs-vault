---
title: 'update(data:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hashfunction/update(data:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/hashfunction/update(data:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hashfunction/update%28data%3A%29.json'
content_hash: 'sha256:03ccfc10774e9c3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HashFunction](../hashfunction.md)

# update(data:)

<sub>Instance Method</sub>

Incrementally updates the hash function with the given data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func update<D>(data: D) where D : DataProtocol
```

## Parameters

- `data` — The next block of data for the ongoing digest calculation. You can provide this as any type that conforms to [DataProtocol](../../foundation/dataprotocol.md), like [Data](../../foundation/data.md) or an array of [UInt8](../../swift/uint8.md) instances.

## Discussion

Call this method one or more times to provide data to the hash function in blocks. After providing the last block of data, call the [finalize()](<finalize().md>) method to get the computed digest. Don’t call the update method again after finalizing the hash function.

## See Also

### Computing a hash iteratively

- [init()](<init().md>) — Creates a hash function.
- [update(bufferPointer:)](<update(bufferpointer_).md>) — Incrementally updates the hash function with the contents of the buffer.
- [finalize()](<finalize().md>) — Finalizes the hash function and returns the computed digest.
