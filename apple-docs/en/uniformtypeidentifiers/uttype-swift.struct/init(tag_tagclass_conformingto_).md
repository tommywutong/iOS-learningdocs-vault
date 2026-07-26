---
title: 'init(tag:tagClass:conformingTo:)'
framework: Uniform Type Identifiers
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uniformtypeidentifiers/uttype-swift.struct/init(tag:tagclass:conformingto:)'
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/init(tag:tagclass:conformingto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/init%28tag%3Atagclass%3Aconformingto%3A%29.json'
content_hash: 'sha256:f3b593284db13eef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# init(tag:tagClass:conformingTo:)

<sub>Initializer</sub>

Creates a type based on a tag, a tag class, and a supertype that it conforms to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(tag: String, tagClass: UTTagClass, conformingTo supertype: UTType?)
```

## Parameters

- `tag` — The tag, such as a filename extension.

- `tagClass` — The tag class, such as [UTTagClassFilenameExtension](../uttagclassfilenameextension.md).

- `supertype` — Another type that the resulting type must conform to; for example, [UTTypeData](../uttypedata.md).

## Discussion

This initializer returns `nil` if the system doesn’t know the tag.

## See Also

### Creating a type

- [init(_:)](<init(__).md>) — Creates a type based on an identifier.
- [init(mimeType:conformingTo:)](<init(mimetype_conformingto_).md>) — Creates a type based on a MIME type and a supertype that it conforms to.
- [init(filenameExtension:conformingTo:)](<init(filenameextension_conformingto_).md>) — Creates a type based on a filename extension and an existing supertype that it conforms to.
- [init(exportedAs:conformingTo:)](<init(exportedas_conformingto_).md>) — Creates a type your app owns based on an identifier and a supertype that it conforms to.
- [init(importedAs:conformingTo:)](<init(importedas_conformingto_).md>) — Creates a type your app uses, but doesn’t own, based on an identifier and a supertype that it conforms to.
