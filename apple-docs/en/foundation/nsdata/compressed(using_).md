---
title: 'compressed(using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/compressed(using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/compressed(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/compressed%28using%3A%29.json'
content_hash: 'sha256:d856a218c7b14175'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# compressed(using:)

<sub>Instance Method</sub>

Returns a new data object by compressing the data object’s bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func compressed(using algorithm: NSData.CompressionAlgorithm) throws -> Self
```

## Parameters

- `algorithm` — An algorithm used to compress the data. For a list of available algorithms, see [CompressionAlgorithm](compressionalgorithm.md).

## Return Value

An [NSData](../nsdata.md) instance that contains the compressed buffer data.

## Discussion

Use this method to compress in-memory data when you want to reduce memory usage and can afford the time to compress and decompress it. If your data object is already in a compressed format, such as media formats like JPEG images or AAC audio, additional compression may provide minimal or no reduction in memory usage.

To restore this data, use [- decompressedDataUsingAlgorithm:error:](<decompressed(using_).md>), and specify the algorithm originally used to compress the data.

The following example shows how to compress the data from a string and prints the sizes of the data instances to illustrate the amount of compression:

```swift
var string = "NSData and its mutable subclass NSMutableData provide data objects, or object-oriented wrappers for byte buffers. Data objects let simple allocated buffers (that is, data with no embedded pointers) take on the behavior of Foundation objects."
let data = Data(string.utf8) as NSData
print ("original data size: \(data.count) bytes")
do {
    let compressedData = try data.compressed(using: .zlib)
    print("zlib compressed size: \(compressedData.count) bytes")
} catch {
    print ("Compression error: \(error)")
}
// Prints:
//  original data size: 241 bytes
//  zlib compressed size: 158 bytes
```

## See Also

### Compressing and Decompressing Data

- [- decompressedDataUsingAlgorithm:error:](<decompressed(using_).md>) — Returns a new data object by decompressing data object’s bytes.
- [CompressionAlgorithm](compressionalgorithm.md) — An algorithm that indicates how to compress or decompress data.
- [NSCompressionErrorMaximum](../nscompressionerrormaximum-swift.var.md) — The end of the range of error codes reserved for compression errors.
- [NSCompressionErrorMinimum](../nscompressionerrorminimum-swift.var.md) — The start of the range of error codes reserved for compression errors.
- [NSCompressionFailedError](../nscompressionfailederror-swift.var.md) — An error code value that indicates a failure to compress data using the provided algorithm.
- [NSDecompressionFailedError](../nsdecompressionfailederror-swift.var.md) — An error code value that indicates a failure to decompress data using the provided algorithm.
