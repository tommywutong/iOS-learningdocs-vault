---
title: 'init(tag:tagClass:conformingTo:)'
framework: Uniform Type Identifiers
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uniformtypeidentifiers/uttypereference/init(tag:tagclass:conformingto:)'
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/init(tag:tagclass:conformingto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypereference/init%28tag%3Atagclass%3Aconformingto%3A%29.json'
content_hash: 'sha256:eb595fd8630db74a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTTypeReference](../uttypereference.md)

# init(tag:tagClass:conformingTo:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(tag: String, tagClass: String, conformingTo supertype: UTType?)
```

## Parameters

- `tag` — The tag, such as the path extension, for which a type is desired.

- `tagClass` — The class of the tag, such as \\c UTTagClassFilenameExtension.

- `supertype` — Another type that the resulting type must conform to. If \\c nil, no conformance is required.

## Return Value

A type. If no types are known to the system with the specified tag but the inputs were otherwise valid, a dynamic type may be provided. If the inputs were not valid, returns \\c nil.

## Discussion

Create a type given a type tag.
