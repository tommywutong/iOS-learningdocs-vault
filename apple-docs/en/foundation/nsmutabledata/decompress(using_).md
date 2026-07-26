---
title: 'decompress(using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledata/decompress(using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledata/decompress(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledata/decompress%28using%3A%29.json'
content_hash: 'sha256:834629e12ca2209c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableData](../nsmutabledata.md)

# decompress(using:)

<sub>Instance Method</sub>

Decompresses the data object’s bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decompress(using algorithm: NSData.CompressionAlgorithm) throws
```

## Parameters

- `algorithm` — The algorithm to use for decompressing the data. For a list of available algorithms, see [CompressionAlgorithm](../nsdata/compressionalgorithm.md).

## Discussion

Use this method to inflate in-memory data when you need uncompressed bytes. Specify the same algorithm used to compress the data to successfully decompress it.

The following example shows how to inflate an instance of [NSMutableData](../nsmutabledata.md) compressed with the [NSDataCompressionAlgorithmZlib](../nsdata/compressionalgorithm/zlib.md) algorithm:

```swift
do {
    data.decompress(using: .zlib)
} catch {
    print ("Decompression error: \(error)")
}
```

## See Also

### Compressing and Decompressing Data

- [- compressUsingAlgorithm:error:](<compress(using_).md>) — Compresses the data object’s bytes using an algorithm that you specify.
- [CompressionAlgorithm](../nsdata/compressionalgorithm.md) — An algorithm that indicates how to compress or decompress data.
- [NSCompressionErrorMaximum](../nscompressionerrormaximum-swift.var.md) — The end of the range of error codes reserved for compression errors.
- [NSCompressionErrorMinimum](../nscompressionerrorminimum-swift.var.md) — The start of the range of error codes reserved for compression errors.
- [NSCompressionFailedError](../nscompressionfailederror-swift.var.md) — An error code value that indicates a failure to compress data using the provided algorithm.
- [NSDecompressionFailedError](../nsdecompressionfailederror-swift.var.md) — An error code value that indicates a failure to decompress data using the provided algorithm.
