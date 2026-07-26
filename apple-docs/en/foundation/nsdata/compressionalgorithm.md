---
title: NSData.CompressionAlgorithm
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdata/compressionalgorithm
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/compressionalgorithm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/compressionalgorithm.json'
content_hash: 'sha256:64bf4ab7aeb7d8f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# NSData.CompressionAlgorithm

<sub>Enumeration</sub>

An algorithm that indicates how to compress or decompress data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CompressionAlgorithm
```

## Overview

Choose an algorithm that best suits the needs of your app:

- [NSDataCompressionAlgorithmLZFSE](compressionalgorithm/lzfse.md) — The algorithm offers faster speed and generally achieves better compression than   [NSDataCompressionAlgorithmZlib](compressionalgorithm/zlib.md). However, it is slower than [NSDataCompressionAlgorithmLZ4](compressionalgorithm/lz4.md) and doesn’t compress as well as [NSDataCompressionAlgorithmLZMA](compressionalgorithm/lzma.md).
- [NSDataCompressionAlgorithmZlib](compressionalgorithm/zlib.md) — Use this algorithm if your app requires interoperability with non-Apple devices. For example, if you are transferering data to another device where it needs to be compressed or decompressed.
- [NSDataCompressionAlgorithmLZ4](compressionalgorithm/lz4.md) — Use this algorithm if speed is critical, and you’re willing to sacrifice compression ratio to achieve it.
- [NSDataCompressionAlgorithmLZMA](compressionalgorithm/lzma.md) — Use this algorithm if compression ratio is critical, and you’re willing to sacrifice speed to achieve it. It is an order of magnitude slower for both compression and decompression than other choices.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Algorithms

- [NSDataCompressionAlgorithmLZ4](compressionalgorithm/lz4.md) — The LZ4 compression algorithm, recommended for fast compression.
- [NSDataCompressionAlgorithmLZFSE](compressionalgorithm/lzfse.md) — The LZFSE compression algorithm, recommended for use on Apple platforms.
- [NSDataCompressionAlgorithmLZMA](compressionalgorithm/lzma.md) — The LZMA compression algorithm, recommended for high-compression ratio.
- [NSDataCompressionAlgorithmZlib](compressionalgorithm/zlib.md) — The zlib compression algorithm, recommended for cross-platform compression.

### Initializers

- [init(rawValue:)](<compressionalgorithm/init(rawvalue_).md>)

## See Also

### Compressing and Decompressing Data

- [- compressedDataUsingAlgorithm:error:](<compressed(using_).md>) — Returns a new data object by compressing the data object’s bytes.
- [- decompressedDataUsingAlgorithm:error:](<decompressed(using_).md>) — Returns a new data object by decompressing data object’s bytes.
- [NSCompressionErrorMaximum](../nscompressionerrormaximum-swift.var.md) — The end of the range of error codes reserved for compression errors.
- [NSCompressionErrorMinimum](../nscompressionerrorminimum-swift.var.md) — The start of the range of error codes reserved for compression errors.
- [NSCompressionFailedError](../nscompressionfailederror-swift.var.md) — An error code value that indicates a failure to compress data using the provided algorithm.
- [NSDecompressionFailedError](../nsdecompressionfailederror-swift.var.md) — An error code value that indicates a failure to decompress data using the provided algorithm.
