---
title: 'init(filenameExtension:conformingTo:)'
framework: Uniform Type Identifiers
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uniformtypeidentifiers/uttypereference/init(filenameextension:conformingto:)'
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/init(filenameextension:conformingto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypereference/init%28filenameextension%3Aconformingto%3A%29.json'
content_hash: 'sha256:bcd1983c148765d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTTypeReference](../uttypereference.md)

# init(filenameExtension:conformingTo:)

<sub>Initializer</sub>

Creates a type that represents the specified filename extension and conforms to an existing type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(filenameExtension: String, conformingTo supertype: UTType)
```

## Parameters

- `filenameExtension` — The filename extension.

- `supertype` — The type the resulting type must conform to, such as [data](../uttype-swift.struct/data.md) or [package](../uttype-swift.struct/package.md).

## Discussion

If the system recognizes the filename extension, the intializer returns the corresponding type; otherwise, the initializer returns a dynamic type whose [isDeclared](../uttype-swift.struct/isdeclared.md) and [isPublic](../uttype-swift.struct/ispublic.md) properties are both set to [false](../../swift/false.md).

## See Also

### Creating a type

- [+ typeWithIdentifier:](<init(__).md>) — Creates a type based on an identifier.
- [+ typeWithMIMEType:](<init(mimetype_)-1txq0.md>) — Creates a type based on a MIME type.
- [+ typeWithMIMEType:conformingToType:](<init(mimetype_conformingto_).md>) — Creates a type based on a MIME type and a supertype that it conforms to.
- [+ typeWithFilenameExtension:](<init(filenameextension_).md>) — Creates a type that represents the specified filename extension.
- [init(tag:tagClass:conformingToType:)](<init(tag_tagclass_conformingtotype_).md>) — Creates a type that represents the specified tag and tag class and which conforms to an existing type.
- [+ exportedTypeWithIdentifier:](<init(exportedas_).md>) — Creates a type your app owns based on an identifier.
- [+ exportedTypeWithIdentifier:conformingToType:](<init(exportedas_conformingto_).md>) — Creates a type your app owns based on an identifier and a supertype that it conforms to.
- [+ importedTypeWithIdentifier:](<init(importedas_).md>) — Creates a type your app uses, but doesn’t own, based on an identifier.
- [+ importedTypeWithIdentifier:conformingToType:](<init(importedas_conformingto_).md>) — Creates a type your app uses, but doesn’t own, based on an identifier and a supertype that it conforms to.
