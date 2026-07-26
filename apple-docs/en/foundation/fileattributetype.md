---
title: FileAttributeType
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/fileattributetype
source_url: 'https://developer.apple.com/documentation/foundation/fileattributetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/fileattributetype.json'
content_hash: 'sha256:5a1380c10b2884dd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# FileAttributeType

<sub>Structure</sub>

Values representing a file’s type attribute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FileAttributeType
```

## Discussion

These strings are the possible values for the [NSFileType](fileattributekey/type.md) attribute key contained in the dictionary object returned by [- attributesOfItemAtPath:error:](<filemanager/attributesofitem(atpath_).md>).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a File Attribute Type

- [init(rawValue:)](<fileattributetype/init(rawvalue_).md>) — Creates a file attribute type value.

### Accessing File Type Attributes

- [NSFileTypeBlockSpecial](fileattributetype/typeblockspecial.md) — A block special file.
- [NSFileTypeCharacterSpecial](fileattributetype/typecharacterspecial.md) — A character special file.
- [NSFileTypeDirectory](fileattributetype/typedirectory.md) — A directory.
- [NSFileTypeRegular](fileattributetype/typeregular.md) — A regular file.
- [NSFileTypeSocket](fileattributetype/typesocket.md) — A socket.
- [NSFileTypeSymbolicLink](fileattributetype/typesymboliclink.md) — A symbolic link.
- [NSFileTypeUnknown](fileattributetype/typeunknown.md) — A file whose type is unknown.

## See Also

### Supporting Types

- [DirectoryEnumerationOptions](filemanager/directoryenumerationoptions.md) — Options for enumerating the contents of directories.
- [SearchPathDirectory](filemanager/searchpathdirectory.md) — The location of significant directories.
- [SearchPathDomainMask](filemanager/searchpathdomainmask.md) — Domain constants specifying base locations to use when you search for significant directories.
- [FileAttributeKey](fileattributekey.md) — Keys in dictionaries used to get and set file attributes.
- [FileProtectionType](fileprotectiontype.md) — Protection level values that can be associated with a file attribute key.
- [URLFileProtection](urlfileprotection.md) — Protection-level values for a URL resource key.
