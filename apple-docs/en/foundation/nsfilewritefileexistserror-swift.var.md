---
title: NSFileWriteFileExistsError
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilewritefileexistserror-swift.var
source_url: 'https://developer.apple.com/documentation/foundation/nsfilewritefileexistserror-swift.var'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilewritefileexistserror-swift.var.json'
content_hash: 'sha256:e1e8ed756a8634cc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSFileWriteFileExistsError

<sub>Global Variable</sub>

Could not perform an operation because the destination file already exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSFileWriteFileExistsError: Int { get }
```

## Discussion

This error can be produced by the [FileManager](filemanager.md) class’s copy, move, and link methods

## See Also

### Error Codes

- [NSFileNoSuchFileError](nsfilenosuchfileerror-swift.var.md) — A filesystem operation was attempted on a non-existent file.
- [NSFileLockingError](nsfilelockingerror-swift.var.md) — The file could not be locked.
- [NSFileReadUnknownError](nsfilereadunknownerror-swift.var.md) — Could not read, for unknown reasons.
- [NSFileReadNoPermissionError](nsfilereadnopermissionerror-swift.var.md) — Could not read because of a permission problem.
- [NSFileReadInvalidFileNameError](nsfilereadinvalidfilenameerror-swift.var.md) — Could not read because of an invalid file name.
- [NSFileReadCorruptFileError](nsfilereadcorruptfileerror-swift.var.md) — Could not read because of a corrupted file, bad format, or similar reason.
- [NSFileReadNoSuchFileError](nsfilereadnosuchfileerror-swift.var.md) — Could not read because no such file was found.
- [NSFileReadInapplicableStringEncodingError](nsfilereadinapplicablestringencodingerror-swift.var.md) — Could not read because the string encoding wasn’t applicable.
- [NSFileReadUnsupportedSchemeError](nsfilereadunsupportedschemeerror-swift.var.md) — Could not read because the specified URL scheme is unsupported.
- [NSFileReadTooLargeError](nsfilereadtoolargeerror-swift.var.md) — Could not read because the specified file was too large.
- [NSFileReadUnknownStringEncodingError](nsfilereadunknownstringencodingerror-swift.var.md) — Could not read because the string coding of the file couldn’t be determined.
- [NSFileWriteUnknownError](nsfilewriteunknownerror-swift.var.md) — Could not write, for unknown reasons.
- [NSFileWriteNoPermissionError](nsfilewritenopermissionerror-swift.var.md) — Could not write because of a permission problem.
- [NSFileWriteInvalidFileNameError](nsfilewriteinvalidfilenameerror-swift.var.md) — Could not write because of an invalid file name.
- [NSFileWriteInapplicableStringEncodingError](nsfilewriteinapplicablestringencodingerror-swift.var.md) — Could not write because the string encoding was not applicable.
