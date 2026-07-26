---
title: 'init(mimeType:conformingTo:)'
framework: Uniform Type Identifiers
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uniformtypeidentifiers/uttype-swift.struct/init(mimetype:conformingto:)'
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/init(mimetype:conformingto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/init%28mimetype%3Aconformingto%3A%29.json'
content_hash: 'sha256:782ef8ce41bc298e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# init(mimeType:conformingTo:)

<sub>Initializer</sub>

Creates a type based on a MIME type and a supertype that it conforms to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(mimeType: String, conformingTo supertype: UTType = .data)
```

## Parameters

- `mimeType` — A string that represents the MIME type.

- `supertype` — Another [UTType](../uttype-swift.struct.md) instance that the resulting type must conform to; for example, [UTTypeData](../uttypedata.md).

## Discussion

This initializer is equivalent to calling:

```swift
UTType(tag: mimeType,
       tagClass: .mimeType,
       conformingTo: supertype)
```

The initializer may provide a dynamic type if the parameters are valid, but the system doesn’t find any types with the MIME type and conformance. The initializer returns `nil` if the parameters aren’t valid.

## See Also

### Creating a type

- [init(_:)](<init(__).md>) — Creates a type based on an identifier.
- [init(filenameExtension:conformingTo:)](<init(filenameextension_conformingto_).md>) — Creates a type based on a filename extension and an existing supertype that it conforms to.
- [init(tag:tagClass:conformingTo:)](<init(tag_tagclass_conformingto_).md>) — Creates a type based on a tag, a tag class, and a supertype that it conforms to.
- [init(exportedAs:conformingTo:)](<init(exportedas_conformingto_).md>) — Creates a type your app owns based on an identifier and a supertype that it conforms to.
- [init(importedAs:conformingTo:)](<init(importedas_conformingto_).md>) — Creates a type your app uses, but doesn’t own, based on an identifier and a supertype that it conforms to.
