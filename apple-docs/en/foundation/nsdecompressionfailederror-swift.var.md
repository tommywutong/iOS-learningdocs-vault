---
title: NSDecompressionFailedError
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdecompressionfailederror-swift.var
source_url: 'https://developer.apple.com/documentation/foundation/nsdecompressionfailederror-swift.var'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecompressionfailederror-swift.var.json'
content_hash: 'sha256:71382ebe51b67ddd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDecompressionFailedError

<sub>Global Variable</sub>

An error code value that indicates a failure to decompress data using the provided algorithm.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSDecompressionFailedError: Int { get }
```

## See Also

### Compressing and Decompressing Data

- [- compressedDataUsingAlgorithm:error:](<nsdata/compressed(using_).md>) — Returns a new data object by compressing the data object’s bytes.
- [- decompressedDataUsingAlgorithm:error:](<nsdata/decompressed(using_).md>) — Returns a new data object by decompressing data object’s bytes.
- [CompressionAlgorithm](nsdata/compressionalgorithm.md) — An algorithm that indicates how to compress or decompress data.
- [NSCompressionErrorMaximum](nscompressionerrormaximum-swift.var.md) — The end of the range of error codes reserved for compression errors.
- [NSCompressionErrorMinimum](nscompressionerrorminimum-swift.var.md) — The start of the range of error codes reserved for compression errors.
- [NSCompressionFailedError](nscompressionfailederror-swift.var.md) — An error code value that indicates a failure to compress data using the provided algorithm.
