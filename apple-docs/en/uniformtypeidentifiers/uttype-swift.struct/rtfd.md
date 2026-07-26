---
title: rtfd
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/rtfd
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/rtfd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/rtfd.json'
content_hash: 'sha256:d2a56b365855979e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# rtfd

<sub>Type Property</sub>

A type that represents Rich Text Format Directory documents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var rtfd: UTType { get }
```

## Discussion

RTFD is RTF with content embedded in its on-disk format.

The identifier for this type is `com.apple.rtfd`.

This type conforms to [UTTypePackage](../uttypepackage.md) and [UTTypeCompositeContent](../uttypecompositecontent.md).

## See Also

### Application files

- [pdf](pdf.md) — A type that represents Adobe Portable Document Format (PDF) documents.
- [flatRTFD](flatrtfd.md) — A type that represents flattened Rich Text Format Directory documents.
- [epub](epub.md) — A type that represents data in the electronic publication (EPUB) format.
