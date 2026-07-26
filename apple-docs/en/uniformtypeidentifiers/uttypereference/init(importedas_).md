---
title: 'init(importedAs:)'
framework: Uniform Type Identifiers
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uniformtypeidentifiers/uttypereference/init(importedas:)'
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/init(importedas:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypereference/init%28importedas%3A%29.json'
content_hash: 'sha256:9d2d4c99be405e99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTTypeReference](../uttypereference.md)

# init(importedAs:)

<sub>Initializer</sub>

Creates a type your app uses, but doesn’t own, based on an identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(importedAs identifier: String)
```

## Parameters

- `identifier` — The identifier of your type.

## See Also

### Creating a type

- [+ typeWithIdentifier:](<init(__).md>) — Creates a type based on an identifier.
- [+ typeWithMIMEType:](<init(mimetype_)-1txq0.md>) — Creates a type based on a MIME type.
- [+ typeWithMIMEType:conformingToType:](<init(mimetype_conformingto_).md>) — Creates a type based on a MIME type and a supertype that it conforms to.
- [+ typeWithFilenameExtension:](<init(filenameextension_).md>) — Creates a type that represents the specified filename extension.
- [+ typeWithFilenameExtension:conformingToType:](<init(filenameextension_conformingto_).md>) — Creates a type that represents the specified filename extension and conforms to an existing type.
- [init(tag:tagClass:conformingToType:)](<init(tag_tagclass_conformingtotype_).md>) — Creates a type that represents the specified tag and tag class and which conforms to an existing type.
- [+ exportedTypeWithIdentifier:](<init(exportedas_).md>) — Creates a type your app owns based on an identifier.
- [+ exportedTypeWithIdentifier:conformingToType:](<init(exportedas_conformingto_).md>) — Creates a type your app owns based on an identifier and a supertype that it conforms to.
- [+ importedTypeWithIdentifier:conformingToType:](<init(importedas_conformingto_).md>) — Creates a type your app uses, but doesn’t own, based on an identifier and a supertype that it conforms to.
