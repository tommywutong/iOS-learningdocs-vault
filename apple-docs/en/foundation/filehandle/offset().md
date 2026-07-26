---
title: offset()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 13.4+, visionOS 1.0+, watchOS 6.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/filehandle/offset()
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/offset()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/offset%28%29.json'
content_hash: 'sha256:3b4c4796c38011d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# offset()

<sub>Instance Method</sub>

Gets the position of the file pointer within the file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func offset() throws -> UInt64
```

## Return Value

The position of the file pointer within the file.

## Discussion

Throws an error if called on a file handle representing a pipe or socket, or if the file descriptor is closed.

## See Also

### Seeking within a file

- [seekToEnd()](<seektoend().md>) — Places the file pointer at the end of the file referenced by the file handle and returns the new file offset.
- [- seekToOffset:error:](<seek(tooffset_).md>) — Moves the file pointer to the specified offset within the file.
