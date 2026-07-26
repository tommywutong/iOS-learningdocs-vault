---
title: UTTypeZIP
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypezip
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypezip'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypezip.json'
content_hash: 'sha256:ab48baea5ab1528c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeZIP

<sub>Global Variable</sub>

A type that represents a zip archive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeZIP;
```

## Discussion

The identifier for this type is `public.zip-archive`.

This type conforms to [UTTypeData](uttypedata.md) and [UTTypeArchive](uttypearchive.md).

## See Also

### Compressed archives

- [UTTypeArchive](uttypearchive.md) — A base type that represents an archive of files and directories.
- [UTTypeGZIP](uttypegzip.md) — A type that represents a GNU zip archive.
- [UTTypeBZ2](uttypebz2.md) — A type that represents a bzip2 archive.
- [UTTypeAppleArchive](uttypeapplearchive.md) — A type that represents an Apple archive of files and directories.
