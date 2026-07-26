---
title: preferredFilenameExtension
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypereference/preferredfilenameextension
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/preferredfilenameextension'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypereference/preferredfilenameextension.json'
content_hash: 'sha256:467bf63ecd9431f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTTypeReference](../uttypereference.md)

# preferredFilenameExtension

<sub>Instance Property</sub>

The preferred filename extension for the type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var preferredFilenameExtension: String? { get }
```

## Discussion

If available, the preferred (first available) tag of class [filenameExtension](../uttagclass/filenameextension.md).

Many types require the generation of a filename; for example, when saving a file to disk. If not `nil`, the value of this property is the best available filename extension for this type.

The value of this property is equivalent to, but more efficient than:

```swift
type.tags[.filenameExtension]?.first
```
