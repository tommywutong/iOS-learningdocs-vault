---
title: UTTypeDirectory
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypedirectory
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypedirectory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypedirectory.json'
content_hash: 'sha256:e05a75bd842a8c81'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeDirectory

<sub>Global Variable</sub>

A type that represents a file system directory, including packages and folders.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeDirectory;
```

## Discussion

The identifier for this type is `public.directory`.

This type conforms to [UTTypeItem](uttypeitem.md).

## See Also

### Apple file system objects

- [UTTypeSymbolicLink](uttypesymboliclink.md) — A type that represents a symbolic link.
- [UTTypeMountPoint](uttypemountpoint.md) — A type that represents a volume mount point.
- [UTTypeAliasFile](uttypealiasfile.md) — A type that represents an alias file.
- [UTTypeFolder](uttypefolder.md) — A type that represents a user-browsable directory.
- [UTTypeVolume](uttypevolume.md) — A type that represents the root folder of a volume or mount point.
- [UTTypeDiskImage](uttypediskimage.md) — A type that represents a data item that’s mountable as a volume.
