---
title: referenceURL
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypereference/referenceurl
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/referenceurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypereference/referenceurl.json'
content_hash: 'sha256:8c39c2ee48739c58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTTypeReference](../uttypereference.md)

# referenceURL

<sub>Instance Property</sub>

The reference URL for the type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var referenceURL: URL? { get }
```

## Discussion

A reference URL is a human-readable document that describes a type. Most types don’t specify reference URLs.

> [!warning] Warning
> The system doesn’t validate the URL, nor does it guarantee its scheme or structure.
