---
title: synchronize()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filehandle/synchronize()
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/synchronize()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/synchronize%28%29.json'
content_hash: 'sha256:35acc466cba4a199'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# synchronize()

<sub>Instance Method</sub>

Causes all in-memory data and attributes of the file represented by the file handle to write to permanent storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func synchronize() throws
```

## Discussion

Programs that require the file to always be in a known state should call this method. An invocation of this method doesn’t return until memory is flushed.

## See Also

### Operating on a file

- [- closeAndReturnError:](<close().md>) — Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing.
- [- truncateAtOffset:error:](<truncate(atoffset_).md>) — Truncates or extends the file represented by the file handle to a specified offset within the file and puts the file pointer at that position.
