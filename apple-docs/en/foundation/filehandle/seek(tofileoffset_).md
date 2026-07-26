---
title: 'seek(toFileOffset:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/filehandle/seek(tofileoffset:)'
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/seek(tofileoffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/seek%28tofileoffset%3A%29.json'
content_hash: 'sha256:cca3c497df7785b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# seek(toFileOffset:)

<sub>Instance Method</sub>

Moves the file pointer to the specified offset within the file represented by the receiver.

> [!warning] Deprecated
> Use [- seekToOffset:error:](<seek(tooffset_).md>) to handle errors when seeking to an offset in the file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func seek(toFileOffset offset: UInt64)
```

## Parameters

- `offset` — The offset to seek to.

## Discussion

Raises [NSFileHandleOperationException](../nsexceptionname/filehandleoperationexception.md) if called on a file handle representing a pipe or socket, if the file descriptor is closed, or if any other error occurs.

## See Also

### Deprecated

- [- readDataToEndOfFile](<readdatatoendoffile().md>) — Reads the available data synchronously up to the end of file or maximum number of bytes. _(deprecated)_
- [- readDataOfLength:](<readdata(oflength_).md>) — Reads data synchronously up to the specified number of bytes. _(deprecated)_
- [- writeData:](<write(__).md>) — Writes the specified data synchronously to the file handle. _(deprecated)_
- [offsetInFile](offsetinfile.md) — The position of the file pointer within the file represented by the file handle. _(deprecated)_
- [- seekToEndOfFile](<seektoendoffile().md>) — Places the file pointer at the end of the file referenced by the file handle and returns the new file offset. _(deprecated)_
- [- closeFile](<closefile().md>) — Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing. _(deprecated)_
- [- synchronizeFile](<synchronizefile().md>) — Causes all in-memory data and attributes of the file represented by the handle to write to permanent storage. _(deprecated)_
- [- truncateFileAtOffset:](<truncatefile(atoffset_).md>) — Truncates or extends the file represented by the file handle to a specified offset within the file and puts the file pointer at that position. _(deprecated)_
- [NSFileHandleNotificationMonitorModes](../nsfilehandlenotificationmonitormodes.md) — Currently unused. _(deprecated)_
