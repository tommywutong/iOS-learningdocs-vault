---
title: 'write(contentsOf:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 13.4+, visionOS 1.0+, watchOS 6.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filehandle/write(contentsof:)'
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/write(contentsof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/write%28contentsof%3A%29.json'
content_hash: 'sha256:e33010850e6bba50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# write(contentsOf:)

<sub>Instance Method</sub>

Writes the specified data synchronously to the file handle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func write<T>(contentsOf data: T) throws where T : DataProtocol
```

## Parameters

- `data` — The data to write to the file handle.

## Discussion

If the handle represents a file, writing takes place at the file pointer’s current position. After it writes the data, the method advances the file pointer by the number of bytes written. This method throws an error if the file descriptor is closed or isn’t valid, if the handle represents an unconnected pipe or socket endpoint, if there isn’t any free space on the file system, or if any other writing error occurs.

## See Also

### Related Documentation

- [availableData](availabledata.md) — The data currently available in the receiver.
- [read(upToCount:)](<read(uptocount_).md>) — Reads data synchronously up to the specified number of bytes.
- [readToEnd()](<readtoend().md>) — Reads the available data synchronously up to the end of file or maximum number of bytes.
