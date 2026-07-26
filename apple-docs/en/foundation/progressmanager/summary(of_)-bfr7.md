---
title: 'summary(of:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/foundation/progressmanager/summary(of:)-bfr7'
source_url: 'https://developer.apple.com/documentation/foundation/progressmanager/summary(of:)-bfr7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressmanager/summary%28of%3A%29-bfr7.json'
content_hash: 'sha256:6de85a8b2d0d579b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProgressManager](../progressmanager.md)

# summary(of:)

<sub>Instance Method</sub>

Returns a summary for a custom string property across the progress subtree.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func summary<P>(of property: KeyPath<ProgressManager.Properties, P.Type>) -> P.Summary where P : ProgressManager.Property, P.Summary == [String?], P.Value == String?
```

## Parameters

- `property` — The type of the string property to summarize. Must be a property where both the value type is `String?` and the summary type is  `[String?]`.

## Return Value

A `[String?]` summary value for the specified property.

## Discussion

This method aggregates the values of a custom string property from this progress manager and all its children, returning a consolidated summary value.
