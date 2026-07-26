---
title: tags
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/tags
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/tags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/tags.json'
content_hash: 'sha256:aa82ea11e37b7aaf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# tags

<sub>Instance Property</sub>

The tag specification dictionary of the type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var tags: [UTTagClass : [String]] { get }
```

## Discussion

Uniform Type Identifiers don’t store tag information for nonstandard tag classes. Identifiers normalize string values into arrays that contain those strings. For example, a tag specification dictionary with values of:

```other
{
    "public.mime-type": "x/y",
    "nonstandard-tag-class": "abc",
}
```

Normalizes to:

```other
{
    "public.mime-type": ["x/y"]
}
```

Use the tag class [mimeType](../uttagclass/mimetype.md) or [filenameExtension](../uttagclass/filenameextension.md) to retrieve the list of supporting MIME types or filename extensions for your type. For example, the following example retrieves a list of the filename extensions for the [mpeg](mpeg.md) type:

```swift
let MPEGextensions = UTType.mpeg.tags[.filenameExtension]
```

Types that have no tags for the requested tag class return a nil, not an empty array.

To get the preferred filename extension or MIME type, use the tag class [preferredFilenameExtension](preferredfilenameextension.md) or [preferredMIMEType](preferredmimetype.md), respectively.

## See Also

### Obtaining tags

- [preferredFilenameExtension](preferredfilenameextension.md) — The preferred filename extension for the type.
- [preferredMIMEType](preferredmimetype.md) — The preferred MIME type for the type.
