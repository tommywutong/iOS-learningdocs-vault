---
title: UTTypeRTFD
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypertfd
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypertfd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypertfd.json'
content_hash: 'sha256:28e711a46b1814c6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeRTFD

<sub>Global Variable</sub>

A type that represents Rich Text Format Directory documents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeRTFD;
```

## Discussion

RTFD is RTF with content embedded in its on-disk format.

The identifier for this type is `com.apple.rtfd`.

This type conforms to [UTTypePackage](uttypepackage.md) and [UTTypeCompositeContent](uttypecompositecontent.md).

## See Also

### Application files

- [UTTypePDF](uttypepdf.md) — A type that represents Adobe Portable Document Format (PDF) documents.
- [UTTypeFlatRTFD](uttypeflatrtfd.md) — A type that represents flattened Rich Text Format Directory documents.
- [UTTypeEPUB](uttypeepub.md) — A type that represents data in the electronic publication (EPUB) format.
