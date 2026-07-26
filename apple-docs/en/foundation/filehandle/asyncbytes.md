---
title: FileHandle.AsyncBytes
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/filehandle/asyncbytes
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/asyncbytes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/asyncbytes.json'
content_hash: 'sha256:2a9b443541c812e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# FileHandle.AsyncBytes

<sub>Structure</sub>

An asynchronous sequence of bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AsyncBytes
```

## Overview

Use the `for`-`await`-`in` syntax to iterate over the bytes in this sequence. For text files, you can also use its [characters](../../swift/asyncsequence/characters.md), [unicodeScalars](../../swift/asyncsequence/unicodescalars.md), or [lines](../../swift/asyncsequence/lines.md) properties to retrieve the contents in a more convenient format. Since all of these properties conform to [AsyncSequence](../../swift/asyncsequence.md), as does the [FileHandle](../filehandle.md) property [bytes](bytes.md), you can use methods defined by [AsyncSequence](../../swift/asyncsequence.md) to perform powerful inline processing. For example, you can skip the first `n` bytes of the file with `myFileHandle.bytes.prefix(n)`.

## Relationships

- **Conforms To**: [AsyncSequence](../../swift/asyncsequence.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Adapting Textual Sequences

- [AsyncCharacterSequence](../asynccharactersequence.md) — An asynchronous sequence of characters.
- [AsyncUnicodeScalarSequence](../asyncunicodescalarsequence.md) — An asychronous sequence of Unicode scalar values.
- [AsyncLineSequence](../asynclinesequence.md) — An asynchronous sequence of lines of text.

### Creating an Iterator

- [makeAsyncIterator()](<asyncbytes/makeasynciterator().md>) — Creates the asynchronous iterator that produces elements of this asynchronous sequence.

### Structures

- [Iterator](asyncbytes/iterator.md) — An iterator that produces the bytes of a file handle.

## See Also

### Reading from a file handle asynchronously

- [bytes](bytes.md) — The file’s contents, as an asynchronous sequence of bytes.
