---
title: 'init(filenameExtension:conformingTo:)'
framework: Uniform Type Identifiers
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uniformtypeidentifiers/uttype-swift.struct/init(filenameextension:conformingto:)'
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/init(filenameextension:conformingto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/init%28filenameextension%3Aconformingto%3A%29.json'
content_hash: 'sha256:4147fb3de2747af0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# init(filenameExtension:conformingTo:)

<sub>Initializer</sub>

Creates a type based on a filename extension and an existing supertype that it conforms to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(filenameExtension: String, conformingTo supertype: UTType = .data)
```

## Parameters

- `filenameExtension` — The filename extension.

- `supertype` — Another type that the resulting type must conform to; for example, [UTTypeData](../uttypedata.md) or [UTTypePackage](../uttypepackage.md).

## Discussion

If the system finds no types with the provided filename extension and conformance, but the inputs are otherwise valid, it may provide a dynamic type. The initializer returns `nil` if the parameters aren’t valid.

This initializer is equivalent to calling:

```swift
UTType(tag: filenameExtension,
       tagClass: .filenameExtension,
       conformingTo: supertype)
```

To get the type of a file on disk, use [contentType](../../foundation/urlresourcevalues/contenttype.md).

> [!important] Important
> You can’t always derive the type of a file system item based solely on its filename extension.

A type depends on other attributes in addition to the filename extension, including whether the item is a directory.

## See Also

### Creating a type

- [init(_:)](<init(__).md>) — Creates a type based on an identifier.
- [init(mimeType:conformingTo:)](<init(mimetype_conformingto_).md>) — Creates a type based on a MIME type and a supertype that it conforms to.
- [init(tag:tagClass:conformingTo:)](<init(tag_tagclass_conformingto_).md>) — Creates a type based on a tag, a tag class, and a supertype that it conforms to.
- [init(exportedAs:conformingTo:)](<init(exportedas_conformingto_).md>) — Creates a type your app owns based on an identifier and a supertype that it conforms to.
- [init(importedAs:conformingTo:)](<init(importedas_conformingto_).md>) — Creates a type your app uses, but doesn’t own, based on an identifier and a supertype that it conforms to.
