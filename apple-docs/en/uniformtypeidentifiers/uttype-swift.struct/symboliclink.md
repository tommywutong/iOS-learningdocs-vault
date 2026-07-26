---
title: symbolicLink
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/symboliclink
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/symboliclink'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/symboliclink.json'
content_hash: 'sha256:915b2f8b0f5c710c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# symbolicLink

<sub>Type Property</sub>

A type that represents a symbolic link.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var symbolicLink: UTType { get }
```

## Discussion

The identifier for this type is `public.symlink`.

This type conforms to [UTTypeItem](../uttypeitem.md) and [UTTypeResolvable](../uttyperesolvable.md).

## See Also

### Apple file system objects

- [directory](directory.md) — A type that represents a file system directory, including packages and folders.
- [mountPoint](mountpoint.md) — A type that represents a volume mount point.
- [aliasFile](aliasfile.md) — A type that represents an alias file.
- [folder](folder.md) — A type that represents a user-browsable directory.
- [volume](volume.md) — A type that represents the root folder of a volume or mount point.
- [diskImage](diskimage.md) — A type that represents a data item that’s mountable as a volume.
