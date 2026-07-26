---
title: 'init(importedAs:conformingTo:)'
framework: Uniform Type Identifiers
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uniformtypeidentifiers/uttype-swift.struct/init(importedas:conformingto:)'
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/init(importedas:conformingto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/init%28importedas%3Aconformingto%3A%29.json'
content_hash: 'sha256:d14331ffc72c299a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# init(importedAs:conformingTo:)

<sub>Initializer</sub>

Creates a type your app uses, but doesn’t own, based on an identifier and a supertype that it conforms to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(importedAs identifier: String, conformingTo parentType: UTType? = nil)
```

## Parameters

- `identifier` — The identifier of your type.

- `parentType` — A type to extend with this type.

## Discussion

Define a type with this initializer when you’re supporting a type that another app owns. For example, the following code uses another app’s type information to open or save files in its app:

```swift
extension UTType {
    /// The type of a supported file format.
    public static var anotherFormat: UTType {
        UTType(importedAs: "com.example.anotherformat")
    }
}
```

## See Also

### Creating a type

- [init(_:)](<init(__).md>) — Creates a type based on an identifier.
- [init(mimeType:conformingTo:)](<init(mimetype_conformingto_).md>) — Creates a type based on a MIME type and a supertype that it conforms to.
- [init(filenameExtension:conformingTo:)](<init(filenameextension_conformingto_).md>) — Creates a type based on a filename extension and an existing supertype that it conforms to.
- [init(tag:tagClass:conformingTo:)](<init(tag_tagclass_conformingto_).md>) — Creates a type based on a tag, a tag class, and a supertype that it conforms to.
- [init(exportedAs:conformingTo:)](<init(exportedas_conformingto_).md>) — Creates a type your app owns based on an identifier and a supertype that it conforms to.
