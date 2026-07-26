---
title: 'init(mimeType:conformingTo:)'
framework: Uniform Type Identifiers
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uniformtypeidentifiers/uttypereference/init(mimetype:conformingto:)'
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/init(mimetype:conformingto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypereference/init%28mimetype%3Aconformingto%3A%29.json'
content_hash: 'sha256:62d97916aed4b57b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTTypeReference](../uttypereference.md)

# init(mimeType:conformingTo:)

<sub>Initializer</sub>

Creates a type based on a MIME type and a supertype that it conforms to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(mimeType: String, conformingTo supertype: UTType)
```

## Parameters

- `mimeType` — A string that represents the MIME type.

- `supertype` — Another [UTType](../uttype-swift.struct.md) instance that the resulting type must conform to; for example, [UTTypeData](../uttypedata.md).

## Discussion

This initializer returns `nil` if the system doesn’t know the MIME type.

## See Also

### Creating a type

- [+ typeWithIdentifier:](<init(__).md>) — Creates a type based on an identifier.
- [+ typeWithMIMEType:](<init(mimetype_)-1txq0.md>) — Creates a type based on a MIME type.
- [+ typeWithFilenameExtension:](<init(filenameextension_).md>) — Creates a type that represents the specified filename extension.
- [+ typeWithFilenameExtension:conformingToType:](<init(filenameextension_conformingto_).md>) — Creates a type that represents the specified filename extension and conforms to an existing type.
- [init(tag:tagClass:conformingToType:)](<init(tag_tagclass_conformingtotype_).md>) — Creates a type that represents the specified tag and tag class and which conforms to an existing type.
- [+ exportedTypeWithIdentifier:](<init(exportedas_).md>) — Creates a type your app owns based on an identifier.
- [+ exportedTypeWithIdentifier:conformingToType:](<init(exportedas_conformingto_).md>) — Creates a type your app owns based on an identifier and a supertype that it conforms to.
- [+ importedTypeWithIdentifier:](<init(importedas_).md>) — Creates a type your app uses, but doesn’t own, based on an identifier.
- [+ importedTypeWithIdentifier:conformingToType:](<init(importedas_conformingto_).md>) — Creates a type your app uses, but doesn’t own, based on an identifier and a supertype that it conforms to.
