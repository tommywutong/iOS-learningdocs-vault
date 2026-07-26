---
title: fileCreationDate()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdictionary/filecreationdate()
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/filecreationdate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/filecreationdate%28%29.json'
content_hash: 'sha256:f409b22f2c05c053'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# fileCreationDate()

<sub>Instance Method</sub>

Returns the file’s creation date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fileCreationDate() -> Date?
```

## Return Value

The value associated with the [NSFileCreationDate](../fileattributekey/creationdate.md) file attributes key, or `nil` if the file attributes dictionary has no entry for the key.

## See Also

### Accessing File Attributes

- [- fileSize](<filesize().md>) — Returns the file’s size, in bytes.
- [- fileType](<filetype().md>) — Returns the file type.
- [- fileModificationDate](<filemodificationdate().md>) — Returns file’s modification date.
- [- filePosixPermissions](<fileposixpermissions().md>) — Returns the file’s POSIX permissions.
- [- fileOwnerAccountID](<fileowneraccountid().md>) — Returns the file’s owner account ID.
- [- fileOwnerAccountName](<fileowneraccountname().md>) — Returns the file’s owner account name.
- [- fileGroupOwnerAccountID](<filegroupowneraccountid().md>) — Returns file’s group owner account ID.
- [- fileGroupOwnerAccountName](<filegroupowneraccountname().md>) — Returns the file’s group owner account name.
- [- fileExtensionHidden](<fileextensionhidden().md>) — Returns a Boolean value indicating whether the file hides its extension.
- [- fileIsImmutable](<fileisimmutable().md>) — Returns a Boolean value indicating whether the file is immutable.
- [- fileIsAppendOnly](<fileisappendonly().md>) — Returns a Boolean value indicating whether the file is append only.
- [- fileSystemFileNumber](<filesystemfilenumber().md>) — Returns the filesystem file number.
- [- fileSystemNumber](<filesystemnumber().md>) — Returns the filesystem number.
- [- fileHFSTypeCode](<filehfstypecode().md>) — Returns file’s HFS type code.
- [- fileHFSCreatorCode](<filehfscreatorcode().md>) — Returns the file’s HFS creator code.
