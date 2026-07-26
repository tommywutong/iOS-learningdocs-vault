---
title: bytes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/filehandle/bytes
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/bytes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/bytes.json'
content_hash: 'sha256:45531f60309cbb94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# bytes

<sub>Instance Property</sub>

The file’s contents, as an asynchronous sequence of bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var bytes: FileHandle.AsyncBytes { get }
```

## Discussion

Use the `for`-`await`-`in` syntax to iterate over the bytes in this sequence. For text files, you can also use its [characters](../../swift/asyncsequence/characters.md), [unicodeScalars](../../swift/asyncsequence/unicodescalars.md), or [lines](../../swift/asyncsequence/lines.md) properties to retrieve the contents in a more convenient format. Since all of these properties conform to [AsyncSequence](../../swift/asyncsequence.md), as does [bytes](bytes.md) itself, you can use methods defined by [AsyncSequence](../../swift/asyncsequence.md) to perform powerful inline processing. For example, you can skip the first `n` bytes of the file with `myFileHandle.bytes.prefix(n)`.

> [!tip] Tip
> Rather than creating a [FileHandle](../filehandle.md) to read a file asynchronously, you can instead use a `file://` URL in combination with the [resourceBytes](../url/resourcebytes.md) property in [URL](../url.md).

## See Also

### Reading from a file handle asynchronously

- [AsyncBytes](asyncbytes.md) — An asynchronous sequence of bytes.
