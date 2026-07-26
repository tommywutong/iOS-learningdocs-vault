---
title: mimeType
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttagclass/mimetype
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttagclass/mimetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttagclass/mimetype.json'
content_hash: 'sha256:51ff65d4386949a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTTagClass](../uttagclass.md)

# mimeType

<sub>Type Property</sub>

A type property that returns the tag class used to map a type to a MIME type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var mimeType: UTTagClass { get }
```

## Discussion

The tag class for MIME types such as `text/plain`. The raw value of this tag class is `public.mime-type`.

## See Also

### Getting a declared types mapping

- [filenameExtension](filenameextension.md) — A type property that returns the tag class used to map a type to a filename extension.
