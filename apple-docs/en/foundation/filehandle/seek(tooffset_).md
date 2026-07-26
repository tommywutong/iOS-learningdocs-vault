---
title: 'seek(toOffset:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filehandle/seek(tooffset:)'
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/seek(tooffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/seek%28tooffset%3A%29.json'
content_hash: 'sha256:68cf74de0a9f771e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# seek(toOffset:)

<sub>Instance Method</sub>

Moves the file pointer to the specified offset within the file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func seek(toOffset offset: UInt64) throws
```

## Parameters

- `offset` — The offset to seek to.

## Discussion

> [!danger] Throws
> Throws an error if called on a file handle representing a pipe or socket, if the file descriptor is closed, or if any other error occurs while seeking.

## See Also

### Seeking within a file

- [offset()](<offset().md>) — Gets the position of the file pointer within the file.
- [seekToEnd()](<seektoend().md>) — Places the file pointer at the end of the file referenced by the file handle and returns the new file offset.
