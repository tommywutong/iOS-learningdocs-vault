---
title: 'readData(ofLength:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/filehandle/readdata(oflength:)'
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/readdata(oflength:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/readdata%28oflength%3A%29.json'
content_hash: 'sha256:08cdece18d1c26ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# readData(ofLength:)

<sub>Instance Method</sub>

Reads data synchronously up to the specified number of bytes.

> [!warning] Deprecated
> To handle errors when reading data from the file handle, use [read(upToCount:)](<read(uptocount_).md>) in Swift and [readDataUpToLength:error:](../nsfilehandle/readdatauptolength_error_.md) in Objective-C.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func readData(ofLength length: Int) -> Data
```

## Parameters

- `length` — The number of bytes to read from the file handle.

## Return Value

The data available through the receiver up to a maximum of `length` bytes, or the maximum size that can be represented by an [NSData](../nsdata.md) object, whichever is the smaller.

## Discussion

If the handle represents a file, this method returns the data obtained by reading `length` bytes starting at the current file pointer. If `length` bytes aren’t available, this method returns the data from the current file pointer to the end of the file. If the handle represents a communications channel, the method reads up to `length` bytes from the channel. Returns an empty `NSData` object if the handle is at the file’s end or if the communications channel returns an end-of-file indicator.

> [!important] Important
> This method raises [NSFileHandleOperationException](../nsexceptionname/filehandleoperationexception.md) if attempts to determine the file-handle type fail or if attempts to read from the file or channel fail.

## See Also

### Related Documentation

- [availableData](availabledata.md) — The data currently available in the receiver.

### Deprecated

- [- readDataToEndOfFile](<readdatatoendoffile().md>) — Reads the available data synchronously up to the end of file or maximum number of bytes. _(deprecated)_
- [- writeData:](<write(__).md>) — Writes the specified data synchronously to the file handle. _(deprecated)_
- [offsetInFile](offsetinfile.md) — The position of the file pointer within the file represented by the file handle. _(deprecated)_
- [- seekToEndOfFile](<seektoendoffile().md>) — Places the file pointer at the end of the file referenced by the file handle and returns the new file offset. _(deprecated)_
- [- seekToFileOffset:](<seek(tofileoffset_).md>) — Moves the file pointer to the specified offset within the file represented by the receiver. _(deprecated)_
- [- closeFile](<closefile().md>) — Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing. _(deprecated)_
- [- synchronizeFile](<synchronizefile().md>) — Causes all in-memory data and attributes of the file represented by the handle to write to permanent storage. _(deprecated)_
- [- truncateFileAtOffset:](<truncatefile(atoffset_).md>) — Truncates or extends the file represented by the file handle to a specified offset within the file and puts the file pointer at that position. _(deprecated)_
- [NSFileHandleNotificationMonitorModes](../nsfilehandlenotificationmonitormodes.md) — Currently unused. _(deprecated)_
