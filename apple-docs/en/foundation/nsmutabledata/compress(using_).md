---
title: 'compress(using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledata/compress(using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledata/compress(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledata/compress%28using%3A%29.json'
content_hash: 'sha256:e4ea5609c4f54d27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableData](../nsmutabledata.md)

# compress(using:)

<sub>Instance Method</sub>

Compresses the data object’s bytes using an algorithm that you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func compress(using algorithm: NSData.CompressionAlgorithm) throws
```

## Parameters

- `algorithm` — The algorithm to use to compress the data. For a list of available algorithms, see [CompressionAlgorithm](../nsdata/compressionalgorithm.md).

## Discussion

Use this method to compress in-memory data when you want to reduce memory usage and can afford the time to compress and decompress the data. If your data object is already in a compressed format, such as media formats like JPEG images or AAC audio, [- compressUsingAlgorithm:error:](<compress(using_).md>) may provide minimal or no benefit.

The following example shows how to compress data from a string and prints the sizes of the data instances to illustrate the amount of compression:

```swift
var string = "NSData and its mutable subclass NSMutableData provide data objects, or object-oriented wrappers for byte buffers. Data objects let simple allocated buffers (that is, data with no embedded pointers) take on the behavior of Foundation objects."
let data = NSMutableData(data: Data(string.utf8))
print ("original data size: \(data.length)")
do {
    try data.compress(using: .zlib)
    print("zlib compressed size: \(data.length)")
} catch {
    print ("Compression error: \(error)")
}
// Prints:
//  original data size: 241
//  zlib compressed size: 158
```

## See Also

### Compressing and Decompressing Data

- [- decompressUsingAlgorithm:error:](<decompress(using_).md>) — Decompresses the data object’s bytes.
- [CompressionAlgorithm](../nsdata/compressionalgorithm.md) — An algorithm that indicates how to compress or decompress data.
- [NSCompressionErrorMaximum](../nscompressionerrormaximum-swift.var.md) — The end of the range of error codes reserved for compression errors.
- [NSCompressionErrorMinimum](../nscompressionerrorminimum-swift.var.md) — The start of the range of error codes reserved for compression errors.
- [NSCompressionFailedError](../nscompressionfailederror-swift.var.md) — An error code value that indicates a failure to compress data using the provided algorithm.
- [NSDecompressionFailedError](../nsdecompressionfailederror-swift.var.md) — An error code value that indicates a failure to decompress data using the provided algorithm.
