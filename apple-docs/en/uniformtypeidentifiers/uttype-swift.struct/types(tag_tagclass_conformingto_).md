---
title: 'types(tag:tagClass:conformingTo:)'
framework: Uniform Type Identifiers
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uniformtypeidentifiers/uttype-swift.struct/types(tag:tagclass:conformingto:)'
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/types(tag:tagclass:conformingto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/types%28tag%3Atagclass%3Aconformingto%3A%29.json'
content_hash: 'sha256:18b0b67bbf899fdd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# types(tag:tagClass:conformingTo:)

<sub>Type Method</sub>

Returns an array of types from the provided tag and tag class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func types(tag: String, tagClass: UTTagClass, conformingTo supertype: UTType?) -> [UTType]
```

## Parameters

- `tag` — The tag, such as a filename extension.

- `tagClass` — The tag class, such as [filenameExtension](../uttagclass/filenameextension.md).

- `supertype` — Another type to which resulting types must conform. A value of `nil` indicates that conformance isn’t required.

## Discussion

If the system doesn’t find any types with the provided tag but the inputs were otherwise valid, it may provide a dynamic type. The initializer returns an empty array if the inputs aren’t valid.
