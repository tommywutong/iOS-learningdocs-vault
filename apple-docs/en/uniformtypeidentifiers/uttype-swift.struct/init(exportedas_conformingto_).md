---
title: 'init(exportedAs:conformingTo:)'
framework: Uniform Type Identifiers
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uniformtypeidentifiers/uttype-swift.struct/init(exportedas:conformingto:)'
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/init(exportedas:conformingto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/init%28exportedas%3Aconformingto%3A%29.json'
content_hash: 'sha256:b1aabef63b21309f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# init(exportedAs:conformingTo:)

<sub>Initializer</sub>

Creates a type your app owns based on an identifier and a supertype that it conforms to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(exportedAs identifier: String, conformingTo parentType: UTType? = nil)
```

## Parameters

- `identifier` — The identifier of your type.

- `parentType` — A type to extend for your own type.

## Discussion

Defining a type with this initializer asserts that you own the type definition. For example, you might define your file format in code to use it to save or open files in your app.

```swift
extension UTType {
    /// The type of my file format.
    public static let myFileFormat = UTType(exportedAs: "com.example.myfileformat")
}
```

## See Also

### Creating a type

- [init(_:)](<init(__).md>) — Creates a type based on an identifier.
- [init(mimeType:conformingTo:)](<init(mimetype_conformingto_).md>) — Creates a type based on a MIME type and a supertype that it conforms to.
- [init(filenameExtension:conformingTo:)](<init(filenameextension_conformingto_).md>) — Creates a type based on a filename extension and an existing supertype that it conforms to.
- [init(tag:tagClass:conformingTo:)](<init(tag_tagclass_conformingto_).md>) — Creates a type based on a tag, a tag class, and a supertype that it conforms to.
- [init(importedAs:conformingTo:)](<init(importedas_conformingto_).md>) — Creates a type your app uses, but doesn’t own, based on an identifier and a supertype that it conforms to.
