---
title: localizedDescription
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypereference/localizeddescription
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/localizeddescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypereference/localizeddescription.json'
content_hash: 'sha256:c0cfdbc24a773550'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTTypeReference](../uttypereference.md)

# localizedDescription

<sub>Instance Property</sub>

A localized description of the type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var localizedDescription: String? { get }
```

## Discussion

If the type doesn’t provide a description, the system searches its supertypes. A dynamic type doesn’t have localized description, even if its supertypes do.
