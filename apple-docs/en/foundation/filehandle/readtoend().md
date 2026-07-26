---
title: readToEnd()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 13.4+, visionOS 1.0+, watchOS 6.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/filehandle/readtoend()
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/readtoend()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/readtoend%28%29.json'
content_hash: 'sha256:d4abd03d543908c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# readToEnd()

<sub>Instance Method</sub>

Reads the available data synchronously up to the end of file or maximum number of bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func readToEnd() throws -> Data?
```

## Return Value

The data available through the file handle up to the maximum size that can be represented by an [NSData](../nsdata.md) object or, if a communications channel, until an end-of-file indicator is returned.

## Discussion

This method invokes [- readDataOfLength:](<readdata(oflength_).md>) as part of its implementation.

## See Also

### Reading from a file handle synchronously

- [availableData](availabledata.md) — The data currently available in the receiver.
- [read(upToCount:)](<read(uptocount_).md>) — Reads data synchronously up to the specified number of bytes.
