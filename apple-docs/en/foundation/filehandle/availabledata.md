---
title: availableData
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filehandle/availabledata
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/availabledata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/availabledata.json'
content_hash: 'sha256:957b5f5ef0387c80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# availableData

<sub>Instance Property</sub>

The data currently available in the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var availableData: Data { get }
```

## Discussion

The data currently available through the receiver, up to the maximum size that can be represented by an [NSData](../nsdata.md) object.

If the receiver is a file, this method returns the data obtained by reading the file from the current file pointer to the end of the file. If the receiver is a communications channel, this method reads up to a buffer of data and returns it; if no data is available, the method blocks. Returns an empty data object if the end of file is reached. This method raises `NSFileHandleOperationException` if attempts to determine the file-handle type fail or if attempts to read from the file or channel fail.

## See Also

### Related Documentation

- [- readDataOfLength:](<readdata(oflength_).md>) — Reads data synchronously up to the specified number of bytes. _(deprecated)_
- [- readDataToEndOfFile](<readdatatoendoffile().md>) — Reads the available data synchronously up to the end of file or maximum number of bytes. _(deprecated)_

### Reading from a file handle synchronously

- [readToEnd()](<readtoend().md>) — Reads the available data synchronously up to the end of file or maximum number of bytes.
- [read(upToCount:)](<read(uptocount_).md>) — Reads data synchronously up to the specified number of bytes.
