---
title: preferredMIMEType
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/preferredmimetype
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/preferredmimetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/preferredmimetype.json'
content_hash: 'sha256:230197bfe6dd8c31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# preferredMIMEType

<sub>Instance Property</sub>

The preferred MIME type for the type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var preferredMIMEType: String? { get }
```

## Discussion

If available, the preferred (first available) tag of class [mimeType](../uttagclass/mimetype.md). If not `nil`, the value of this property is the best available MIME type value for this type.

The value of this property is equivalent to, but more efficient than:

```swift
type.tags[.mimeType]?.first
```

## See Also

### Obtaining tags

- [preferredFilenameExtension](preferredfilenameextension.md) — The preferred filename extension for the type.
- [tags](tags.md) — The tag specification dictionary of the type.
