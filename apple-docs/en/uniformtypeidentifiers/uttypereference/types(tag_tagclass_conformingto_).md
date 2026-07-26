---
title: 'types(tag:tagClass:conformingTo:)'
framework: Uniform Type Identifiers
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uniformtypeidentifiers/uttypereference/types(tag:tagclass:conformingto:)'
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/types(tag:tagclass:conformingto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypereference/types%28tag%3Atagclass%3Aconformingto%3A%29.json'
content_hash: 'sha256:4efdc7e0c4ded022'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTTypeReference](../uttypereference.md)

# types(tag:tagClass:conformingTo:)

<sub>Type Method</sub>

Returns an array of types from the provided tag and tag class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func types(tag: String, tagClass: String, conformingTo supertype: UTType?) -> [UTType]
```

## Parameters

- `tag` — The desired tag, such as a filename extension.

- `tagClass` — The tag class, such as [UTTagClassFilenameExtension](../uttagclassfilenameextension.md).

- `supertype` — Another type that the resulting type must conform to; for example, [UTTypeData](../uttypedata.md).
