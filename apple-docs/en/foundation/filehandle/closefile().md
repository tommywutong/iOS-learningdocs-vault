---
title: closeFile()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/filehandle/closefile()
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/closefile()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/closefile%28%29.json'
content_hash: 'sha256:120a56f0d1ccfcd2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# closeFile()

<sub>Instance Method</sub>

Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing.

> [!warning] Deprecated
> Use [- closeAndReturnError:](<close().md>) to handle errors when closing a file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func closeFile()
```

## Discussion

If the file handle object owns its file descriptor, it automatically closes that descriptor when it is deallocated. If you initialized the file handle object using the [- initWithFileDescriptor:](<init(filedescriptor_).md>) method, or you initialized it using the [- initWithFileDescriptor:closeOnDealloc:](<init(filedescriptor_closeondealloc_).md>) and passed [false](../../swift/false.md) for the `flag` parameter, you can use this method to close the file descriptor; otherwise, you must close the file descriptor yourself.

After calling this method, you may still use the file handle object but must not attempt to read or write data or use the object to operate on the file descriptor. Attempts to read or write a closed file descriptor raise an exception.

## See Also

### Deprecated

- [- readDataToEndOfFile](<readdatatoendoffile().md>) — Reads the available data synchronously up to the end of file or maximum number of bytes. _(deprecated)_
- [- readDataOfLength:](<readdata(oflength_).md>) — Reads data synchronously up to the specified number of bytes. _(deprecated)_
- [- writeData:](<write(__).md>) — Writes the specified data synchronously to the file handle. _(deprecated)_
- [offsetInFile](offsetinfile.md) — The position of the file pointer within the file represented by the file handle. _(deprecated)_
- [- seekToEndOfFile](<seektoendoffile().md>) — Places the file pointer at the end of the file referenced by the file handle and returns the new file offset. _(deprecated)_
- [- seekToFileOffset:](<seek(tofileoffset_).md>) — Moves the file pointer to the specified offset within the file represented by the receiver. _(deprecated)_
- [- synchronizeFile](<synchronizefile().md>) — Causes all in-memory data and attributes of the file represented by the handle to write to permanent storage. _(deprecated)_
- [- truncateFileAtOffset:](<truncatefile(atoffset_).md>) — Truncates or extends the file represented by the file handle to a specified offset within the file and puts the file pointer at that position. _(deprecated)_
- [NSFileHandleNotificationMonitorModes](../nsfilehandlenotificationmonitormodes.md) — Currently unused. _(deprecated)_
