---
title: UTTypeFolder
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypefolder
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypefolder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypefolder.json'
content_hash: 'sha256:b52046ddec25c7f9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeFolder

<sub>Global Variable</sub>

A type that represents a user-browsable directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeFolder;
```

## Discussion

The identifier for this type is `public.folder`.

This type conforms to [UTTypeDirectory](uttypedirectory.md).

## See Also

### Apple file system objects

- [UTTypeDirectory](uttypedirectory.md) — A type that represents a file system directory, including packages and folders.
- [UTTypeSymbolicLink](uttypesymboliclink.md) — A type that represents a symbolic link.
- [UTTypeMountPoint](uttypemountpoint.md) — A type that represents a volume mount point.
- [UTTypeAliasFile](uttypealiasfile.md) — A type that represents an alias file.
- [UTTypeVolume](uttypevolume.md) — A type that represents the root folder of a volume or mount point.
- [UTTypeDiskImage](uttypediskimage.md) — A type that represents a data item that’s mountable as a volume.
