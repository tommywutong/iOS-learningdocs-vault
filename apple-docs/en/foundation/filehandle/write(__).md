---
title: 'write(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/filehandle/write(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/write(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/write%28_%3A%29.json'
content_hash: 'sha256:583a488c8168aa35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# write(_:)

<sub>Instance Method</sub>

Writes the specified data synchronously to the file handle.

> [!warning] Deprecated
> To handle errors when writing data to the file handle, use [write(contentsOf:)](<write(contentsof_).md>) in Swift and [writeData:error:](../nsfilehandle/writedata_error_.md) in Objective-C.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func write(_ data: Data)
```

## Parameters

- `data` — The data to write to the file handle.

## Discussion

If the handle represents a file, writing takes place at the file pointer’s current position. After it writes the data, the method advances the file pointer by the number of bytes written.

> [!important] Important
> This method raises [NSFileHandleOperationException](../nsexceptionname/filehandleoperationexception.md) if the file descriptor is closed or isn’t valid, if the handle represents an unconnected pipe or socket endpoint, if there isn’t any free space on the file system, or if any other writing error occurs.

## See Also

### Related Documentation

- [availableData](availabledata.md) — The data currently available in the receiver.

### Deprecated

- [- readDataToEndOfFile](<readdatatoendoffile().md>) — Reads the available data synchronously up to the end of file or maximum number of bytes. _(deprecated)_
- [- readDataOfLength:](<readdata(oflength_).md>) — Reads data synchronously up to the specified number of bytes. _(deprecated)_
- [offsetInFile](offsetinfile.md) — The position of the file pointer within the file represented by the file handle. _(deprecated)_
- [- seekToEndOfFile](<seektoendoffile().md>) — Places the file pointer at the end of the file referenced by the file handle and returns the new file offset. _(deprecated)_
- [- seekToFileOffset:](<seek(tofileoffset_).md>) — Moves the file pointer to the specified offset within the file represented by the receiver. _(deprecated)_
- [- closeFile](<closefile().md>) — Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing. _(deprecated)_
- [- synchronizeFile](<synchronizefile().md>) — Causes all in-memory data and attributes of the file represented by the handle to write to permanent storage. _(deprecated)_
- [- truncateFileAtOffset:](<truncatefile(atoffset_).md>) — Truncates or extends the file represented by the file handle to a specified offset within the file and puts the file pointer at that position. _(deprecated)_
- [NSFileHandleNotificationMonitorModes](../nsfilehandlenotificationmonitormodes.md) — Currently unused. _(deprecated)_
