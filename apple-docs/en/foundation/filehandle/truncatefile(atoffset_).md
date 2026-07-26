---
title: 'truncateFile(atOffset:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/filehandle/truncatefile(atoffset:)'
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/truncatefile(atoffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/truncatefile%28atoffset%3A%29.json'
content_hash: 'sha256:33cc5ad2203230b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# truncateFile(atOffset:)

<sub>Instance Method</sub>

Truncates or extends the file represented by the file handle to a specified offset within the file and puts the file pointer at that position.

> [!warning] Deprecated
> Use [- truncateAtOffset:error:](<truncate(atoffset_).md>) to handle errors when truncating or extending the file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func truncateFile(atOffset offset: UInt64)
```

## Parameters

- `offset` — The offset within the file that marks the new end of the file.

## Discussion

If the file is extended (if `offset` is beyond the current end of file), the added characters are null bytes.

> [!important] Important
> This method raises [NSFileHandleOperationException](../nsexceptionname/filehandleoperationexception.md) if called on a file handle representing a pipe or socket, if the file descriptor is closed, or if the operation failed.

## See Also

### Deprecated

- [- readDataToEndOfFile](<readdatatoendoffile().md>) — Reads the available data synchronously up to the end of file or maximum number of bytes. _(deprecated)_
- [- readDataOfLength:](<readdata(oflength_).md>) — Reads data synchronously up to the specified number of bytes. _(deprecated)_
- [- writeData:](<write(__).md>) — Writes the specified data synchronously to the file handle. _(deprecated)_
- [offsetInFile](offsetinfile.md) — The position of the file pointer within the file represented by the file handle. _(deprecated)_
- [- seekToEndOfFile](<seektoendoffile().md>) — Places the file pointer at the end of the file referenced by the file handle and returns the new file offset. _(deprecated)_
- [- seekToFileOffset:](<seek(tofileoffset_).md>) — Moves the file pointer to the specified offset within the file represented by the receiver. _(deprecated)_
- [- closeFile](<closefile().md>) — Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing. _(deprecated)_
- [- synchronizeFile](<synchronizefile().md>) — Causes all in-memory data and attributes of the file represented by the handle to write to permanent storage. _(deprecated)_
- [NSFileHandleNotificationMonitorModes](../nsfilehandlenotificationmonitormodes.md) — Currently unused. _(deprecated)_
