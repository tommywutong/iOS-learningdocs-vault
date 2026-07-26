---
title: UTTypeAppleArchive
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypeapplearchive
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypeapplearchive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypeapplearchive.json'
content_hash: 'sha256:aa5deadc26723681'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeAppleArchive

<sub>Global Variable</sub>

A type that represents an Apple archive of files and directories.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeAppleArchive;
```

## Discussion

The identifier for this type is `com.apple.archive`.

This type conforms to [UTTypeData](uttypedata.md) and [UTTypeArchive](uttypearchive.md).

## See Also

### Compressed archives

- [UTTypeArchive](uttypearchive.md) — A base type that represents an archive of files and directories.
- [UTTypeZIP](uttypezip.md) — A type that represents a zip archive.
- [UTTypeGZIP](uttypegzip.md) — A type that represents a GNU zip archive.
- [UTTypeBZ2](uttypebz2.md) — A type that represents a bzip2 archive.
