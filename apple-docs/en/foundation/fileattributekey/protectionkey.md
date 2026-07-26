---
title: protectionKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/fileattributekey/protectionkey
source_url: 'https://developer.apple.com/documentation/foundation/fileattributekey/protectionkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/fileattributekey/protectionkey.json'
content_hash: 'sha256:6573e0eb2c86802f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileAttributeKey](../fileattributekey.md)

# protectionKey

<sub>Type Property</sub>

The key in a file attribute dictionary whose value identifies the protection level for this file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let protectionKey: FileAttributeKey
```

## Discussion

The corresponding value is an [NSString](../nsstring.md) value. For a list of possible values, see `File Protection Values`.

## See Also

### Accessing File Attributes

- [NSFileAppendOnly](appendonly.md) — The key in a file attribute dictionary whose value indicates whether the file is read-only.
- [NSFileBusy](busy.md) — The key in a file attribute dictionary whose value indicates whether the file is busy.
- [NSFileCreationDate](creationdate.md) — The key in a file attribute dictionary whose value indicates the file’s creation date.
- [NSFileDeviceIdentifier](deviceidentifier.md) — The key in a file attribute dictionary whose value indicates the identifier for the device on which the file resides.
- [NSFileExtensionHidden](extensionhidden.md) — The key in a file attribute dictionary whose value indicates whether the file’s extension is hidden.
- [NSFileGroupOwnerAccountID](groupowneraccountid.md) — The key in a file attribute dictionary whose value indicates the file’s group ID.
- [NSFileGroupOwnerAccountName](groupowneraccountname.md) — The key in a file attribute dictionary whose value indicates the group name of the file’s owner.
- [NSFileHFSCreatorCode](hfscreatorcode.md) — The key in a file attribute dictionary whose value indicates the file’s HFS creator code.
- [NSFileHFSTypeCode](hfstypecode.md) — The key in a file attribute dictionary whose value indicates the file’s HFS type code.
- [NSFileImmutable](immutable.md) — The key in a file attribute dictionary whose value indicates whether the file is mutable.
- [NSFileModificationDate](modificationdate.md) — The key in a file attribute dictionary whose value indicates the file’s last modified date.
- [NSFileOwnerAccountID](owneraccountid.md) — The key in a file attribute dictionary whose value indicates the file’s owner’s account ID.
- [NSFileOwnerAccountName](owneraccountname.md) — The key in a file attribute dictionary whose value indicates the name of the file’s owner.
- [NSFilePosixPermissions](posixpermissions.md) — The key in a file attribute dictionary whose value indicates the file’s Posix permissions.
- [NSFileReferenceCount](referencecount.md) — The key in a file attribute dictionary whose value indicates the file’s reference count.
