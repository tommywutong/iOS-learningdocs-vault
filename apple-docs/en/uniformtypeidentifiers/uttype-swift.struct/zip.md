---
title: zip
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/zip
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/zip'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/zip.json'
content_hash: 'sha256:1f94c54fe6942cf0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# zip

<sub>Type Property</sub>

A type that represents a zip archive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var zip: UTType { get }
```

## Discussion

The identifier for this type is `public.zip-archive`.

This type conforms to [UTTypeData](../uttypedata.md) and [UTTypeArchive](../uttypearchive.md).

## See Also

### Compressed archives

- [archive](archive.md) — A base type that represents an archive of files and directories.
- [gzip](gzip.md) — A type that represents a GNU zip archive.
- [bz2](bz2.md) — A type that represents a bzip2 archive.
- [appleArchive](applearchive.md) — A type that represents an Apple archive of files and directories.
