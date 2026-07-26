---
title: NSFileHandleNotificationMonitorModes
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+（5.0 起废弃）, iPadOS 2.0+（5.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsfilehandlenotificationmonitormodes
source_url: 'https://developer.apple.com/documentation/foundation/nsfilehandlenotificationmonitormodes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilehandlenotificationmonitormodes.json'
content_hash: 'sha256:507b9da3b1b86277'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSFileHandleNotificationMonitorModes

<sub>Global Variable</sub>

Currently unused.

> [!warning] Deprecated
> Not supported

<sub>tvOS, visionOS, watchOS</sub>

```swift
let NSFileHandleNotificationMonitorModes: String
```

## See Also

### Deprecated

- [- readDataToEndOfFile](<filehandle/readdatatoendoffile().md>) — Reads the available data synchronously up to the end of file or maximum number of bytes. _(deprecated)_
- [- readDataOfLength:](<filehandle/readdata(oflength_).md>) — Reads data synchronously up to the specified number of bytes. _(deprecated)_
- [- writeData:](<filehandle/write(__).md>) — Writes the specified data synchronously to the file handle. _(deprecated)_
- [offsetInFile](filehandle/offsetinfile.md) — The position of the file pointer within the file represented by the file handle. _(deprecated)_
- [- seekToEndOfFile](<filehandle/seektoendoffile().md>) — Places the file pointer at the end of the file referenced by the file handle and returns the new file offset. _(deprecated)_
- [- seekToFileOffset:](<filehandle/seek(tofileoffset_).md>) — Moves the file pointer to the specified offset within the file represented by the receiver. _(deprecated)_
- [- closeFile](<filehandle/closefile().md>) — Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing. _(deprecated)_
- [- synchronizeFile](<filehandle/synchronizefile().md>) — Causes all in-memory data and attributes of the file represented by the handle to write to permanent storage. _(deprecated)_
- [- truncateFileAtOffset:](<filehandle/truncatefile(atoffset_).md>) — Truncates or extends the file represented by the file handle to a specified offset within the file and puts the file pointer at that position. _(deprecated)_
