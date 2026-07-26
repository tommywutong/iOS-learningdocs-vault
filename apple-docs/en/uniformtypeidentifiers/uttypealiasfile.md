---
title: UTTypeAliasFile
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypealiasfile
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypealiasfile'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypealiasfile.json'
content_hash: 'sha256:e0dc214e8bcacc96'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeAliasFile

<sub>Global Variable</sub>

A type that represents an alias file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeAliasFile;
```

## Discussion

This type conforms to both [UTTypeData](uttypedata.md) and [UTTypeResolvable](uttyperesolvable.md), and its identifier is `com.apple.alias-file`.

## See Also

### Apple file system objects

- [UTTypeDirectory](uttypedirectory.md) — A type that represents a file system directory, including packages and folders.
- [UTTypeSymbolicLink](uttypesymboliclink.md) — A type that represents a symbolic link.
- [UTTypeMountPoint](uttypemountpoint.md) — A type that represents a volume mount point.
- [UTTypeFolder](uttypefolder.md) — A type that represents a user-browsable directory.
- [UTTypeVolume](uttypevolume.md) — A type that represents the root folder of a volume or mount point.
- [UTTypeDiskImage](uttypediskimage.md) — A type that represents a data item that’s mountable as a volume.
