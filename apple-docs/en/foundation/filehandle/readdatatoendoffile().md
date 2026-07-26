---
title: readDataToEndOfFile()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/filehandle/readdatatoendoffile()
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/readdatatoendoffile()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/readdatatoendoffile%28%29.json'
content_hash: 'sha256:cb49d56cd04b7d41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# readDataToEndOfFile()

<sub>Instance Method</sub>

Reads the available data synchronously up to the end of file or maximum number of bytes.

> [!warning] Deprecated
> To handle errors when reading data from the file handle, use [readToEnd()](<readtoend().md>) in Swift and [readDataToEndOfFileAndReturnError:](../nsfilehandle/readdatatoendoffileandreturnerror_.md) in Objective-C.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func readDataToEndOfFile() -> Data
```

## Return Value

The data available through the receiver up to maximum size that can be represented by an [NSData](../nsdata.md) object or, if a communications channel, until an end-of-file indicator is returned.

## Discussion

This method invokes [- readDataOfLength:](<readdata(oflength_).md>) as part of its implementation.

> [!important] Important
> This method raises [NSFileHandleOperationException](../nsexceptionname/filehandleoperationexception.md) if attempts to determine the file-handle type fail or if attempts to read from the file or channel fail.

## See Also

### Related Documentation

- [availableData](availabledata.md) — The data currently available in the receiver.

### Deprecated

- [- readDataOfLength:](<readdata(oflength_).md>) — Reads data synchronously up to the specified number of bytes. _(deprecated)_
- [- writeData:](<write(__).md>) — Writes the specified data synchronously to the file handle. _(deprecated)_
- [offsetInFile](offsetinfile.md) — The position of the file pointer within the file represented by the file handle. _(deprecated)_
- [- seekToEndOfFile](<seektoendoffile().md>) — Places the file pointer at the end of the file referenced by the file handle and returns the new file offset. _(deprecated)_
- [- seekToFileOffset:](<seek(tofileoffset_).md>) — Moves the file pointer to the specified offset within the file represented by the receiver. _(deprecated)_
- [- closeFile](<closefile().md>) — Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing. _(deprecated)_
- [- synchronizeFile](<synchronizefile().md>) — Causes all in-memory data and attributes of the file represented by the handle to write to permanent storage. _(deprecated)_
- [- truncateFileAtOffset:](<truncatefile(atoffset_).md>) — Truncates or extends the file represented by the file handle to a specified offset within the file and puts the file pointer at that position. _(deprecated)_
- [NSFileHandleNotificationMonitorModes](../nsfilehandlenotificationmonitormodes.md) — Currently unused. _(deprecated)_
