---
title: FileAttributeKey
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/fileattributekey
source_url: 'https://developer.apple.com/documentation/foundation/fileattributekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/fileattributekey.json'
content_hash: 'sha256:f0feb04fe383a8f4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# FileAttributeKey

<sub>Structure</sub>

Keys in dictionaries used to get and set file attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FileAttributeKey
```

## Discussion

These keys are used with the methods listed in the Getting and Setting Attributes topic of [FileManager](filemanager.md).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a File Attribute Key

- [init(_:)](<fileattributekey/init(__).md>) — Creates a file attribute key from a string.
- [init(rawValue:)](<fileattributekey/init(rawvalue_).md>) — Creates a file attribute key from a raw value string.

### Accessing File Attributes

- [NSFileAppendOnly](fileattributekey/appendonly.md) — The key in a file attribute dictionary whose value indicates whether the file is read-only.
- [NSFileBusy](fileattributekey/busy.md) — The key in a file attribute dictionary whose value indicates whether the file is busy.
- [NSFileCreationDate](fileattributekey/creationdate.md) — The key in a file attribute dictionary whose value indicates the file’s creation date.
- [NSFileDeviceIdentifier](fileattributekey/deviceidentifier.md) — The key in a file attribute dictionary whose value indicates the identifier for the device on which the file resides.
- [NSFileExtensionHidden](fileattributekey/extensionhidden.md) — The key in a file attribute dictionary whose value indicates whether the file’s extension is hidden.
- [NSFileGroupOwnerAccountID](fileattributekey/groupowneraccountid.md) — The key in a file attribute dictionary whose value indicates the file’s group ID.
- [NSFileGroupOwnerAccountName](fileattributekey/groupowneraccountname.md) — The key in a file attribute dictionary whose value indicates the group name of the file’s owner.
- [NSFileHFSCreatorCode](fileattributekey/hfscreatorcode.md) — The key in a file attribute dictionary whose value indicates the file’s HFS creator code.
- [NSFileHFSTypeCode](fileattributekey/hfstypecode.md) — The key in a file attribute dictionary whose value indicates the file’s HFS type code.
- [NSFileImmutable](fileattributekey/immutable.md) — The key in a file attribute dictionary whose value indicates whether the file is mutable.
- [NSFileModificationDate](fileattributekey/modificationdate.md) — The key in a file attribute dictionary whose value indicates the file’s last modified date.
- [NSFileOwnerAccountID](fileattributekey/owneraccountid.md) — The key in a file attribute dictionary whose value indicates the file’s owner’s account ID.
- [NSFileOwnerAccountName](fileattributekey/owneraccountname.md) — The key in a file attribute dictionary whose value indicates the name of the file’s owner.
- [NSFilePosixPermissions](fileattributekey/posixpermissions.md) — The key in a file attribute dictionary whose value indicates the file’s Posix permissions.
- [NSFileProtectionKey](fileattributekey/protectionkey.md) — The key in a file attribute dictionary whose value identifies the protection level for this file.
- [NSFileReferenceCount](fileattributekey/referencecount.md) — The key in a file attribute dictionary whose value indicates the file’s reference count.
- [NSFileSize](fileattributekey/size.md) — The key in a file attribute dictionary whose value indicates the file’s size in bytes.
- [NSFileSystemFileNumber](fileattributekey/systemfilenumber.md) — The key in a file attribute dictionary whose value indicates the file’s filesystem file number.
- [NSFileSystemFreeNodes](fileattributekey/systemfreenodes.md) — The key in a file system attribute dictionary whose value indicates the number of free nodes in the file system.
- [NSFileSystemFreeSize](fileattributekey/systemfreesize.md) — The key in a file system attribute dictionary whose value indicates the amount of free space on the file system.
- [NSFileSystemNodes](fileattributekey/systemnodes.md) — The key in a file system attribute dictionary whose value indicates the number of nodes in the file system.
- [NSFileSystemNumber](fileattributekey/systemnumber.md) — The key in a file system attribute dictionary whose value indicates the filesystem number of the file system.
- [NSFileSystemSize](fileattributekey/systemsize.md) — The key in a file system attribute dictionary whose value indicates the size of the file system.
- [NSFileType](fileattributekey/type.md) — The key in a file attribute dictionary whose value indicates the file’s type.

## See Also

### Supporting Types

- [DirectoryEnumerationOptions](filemanager/directoryenumerationoptions.md) — Options for enumerating the contents of directories.
- [SearchPathDirectory](filemanager/searchpathdirectory.md) — The location of significant directories.
- [SearchPathDomainMask](filemanager/searchpathdomainmask.md) — Domain constants specifying base locations to use when you search for significant directories.
- [FileAttributeType](fileattributetype.md) — Values representing a file’s type attribute.
- [FileProtectionType](fileprotectiontype.md) — Protection level values that can be associated with a file attribute key.
- [URLFileProtection](urlfileprotection.md) — Protection-level values for a URL resource key.
