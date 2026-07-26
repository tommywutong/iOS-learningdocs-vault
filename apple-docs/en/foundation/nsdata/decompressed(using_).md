---
title: 'decompressed(using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/decompressed(using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/decompressed(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/decompressed%28using%3A%29.json'
content_hash: 'sha256:31fbe3c3b5aaff7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# decompressed(using:)

<sub>Instance Method</sub>

Returns a new data object by decompressing data object’s bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decompressed(using algorithm: NSData.CompressionAlgorithm) throws -> Self
```

## Parameters

- `algorithm` — An algorithm used to decompress the data. For a list of available algorithms, see [CompressionAlgorithm](compressionalgorithm.md).

## Return Value

An [NSData](../nsdata.md) instance that contains the decompressed buffer data.

## Discussion

Use this method to inflate in-memory data when you need uncompressed bytes. Specify the same algorithm used to compress the data to successfully decompress it.

The following example shows how to create a new [NSData](../nsdata.md) instance from data compressed with the [NSDataCompressionAlgorithmZlib](compressionalgorithm/zlib.md) algorithm:

```swift
do {
    let uncompressedData = try compressedData.decompressed(using: .zlib)
} catch {
    print ("Decompression error: \(error)")
}
```

## See Also

### Compressing and Decompressing Data

- [- compressedDataUsingAlgorithm:error:](<compressed(using_).md>) — Returns a new data object by compressing the data object’s bytes.
- [CompressionAlgorithm](compressionalgorithm.md) — An algorithm that indicates how to compress or decompress data.
- [NSCompressionErrorMaximum](../nscompressionerrormaximum-swift.var.md) — The end of the range of error codes reserved for compression errors.
- [NSCompressionErrorMinimum](../nscompressionerrorminimum-swift.var.md) — The start of the range of error codes reserved for compression errors.
- [NSCompressionFailedError](../nscompressionfailederror-swift.var.md) — An error code value that indicates a failure to compress data using the provided algorithm.
- [NSDecompressionFailedError](../nsdecompressionfailederror-swift.var.md) — An error code value that indicates a failure to decompress data using the provided algorithm.
