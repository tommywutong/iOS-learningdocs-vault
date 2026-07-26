---
title: 'truncate(atOffset:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filehandle/truncate(atoffset:)'
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/truncate(atoffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/truncate%28atoffset%3A%29.json'
content_hash: 'sha256:fa74f5d14bd9727d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# truncate(atOffset:)

<sub>Instance Method</sub>

Truncates or extends the file represented by the file handle to a specified offset within the file and puts the file pointer at that position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func truncate(atOffset offset: UInt64) throws
```

## Parameters

- `offset` — The offset within the file that marks the new end of the file.

## Discussion

If the file is extended (if `offset` is beyond the current end of file), the added characters are null bytes.

## See Also

### Operating on a file

- [- closeAndReturnError:](<close().md>) — Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing.
- [- synchronizeAndReturnError:](<synchronize().md>) — Causes all in-memory data and attributes of the file represented by the file handle to write to permanent storage.
