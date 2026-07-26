---
title: filenameExtension
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttagclass/filenameextension
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttagclass/filenameextension'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttagclass/filenameextension.json'
content_hash: 'sha256:b6e898ed1399fe9c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTTagClass](../uttagclass.md)

# filenameExtension

<sub>Type Property</sub>

A type property that returns the tag class used to map a type to a filename extension.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var filenameExtension: UTTagClass { get }
```

## Discussion

The tag class for filename extensions such as `txt`.

Don’t include the leading period (`.`) character in the tag; it isn’t part of the filename extension.

The raw value of this tag class is `public.filename-extension`.

## See Also

### Getting a declared types mapping

- [mimeType](mimetype.md) — A type property that returns the tag class used to map a type to a MIME type.
