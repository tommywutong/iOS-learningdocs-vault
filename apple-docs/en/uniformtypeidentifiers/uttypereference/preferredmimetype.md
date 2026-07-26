---
title: preferredMIMEType
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypereference/preferredmimetype
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/preferredmimetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypereference/preferredmimetype.json'
content_hash: 'sha256:f3ee806436b39588'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTTypeReference](../uttypereference.md)

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
