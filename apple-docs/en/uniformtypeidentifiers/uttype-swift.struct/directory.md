---
title: directory
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/directory
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/directory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/directory.json'
content_hash: 'sha256:c5bab35770e0c5ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# directory

<sub>Type Property</sub>

A type that represents a file system directory, including packages and folders.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var directory: UTType { get }
```

## Discussion

The identifier for this type is `public.directory`.

This type conforms to [UTTypeItem](../uttypeitem.md).

## See Also

### Apple file system objects

- [symbolicLink](symboliclink.md) — A type that represents a symbolic link.
- [mountPoint](mountpoint.md) — A type that represents a volume mount point.
- [aliasFile](aliasfile.md) — A type that represents an alias file.
- [folder](folder.md) — A type that represents a user-browsable directory.
- [volume](volume.md) — A type that represents the root folder of a volume or mount point.
- [diskImage](diskimage.md) — A type that represents a data item that’s mountable as a volume.
