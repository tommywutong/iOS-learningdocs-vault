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
doc_path: '/documentation/foundation/progressreporter/summary(of:)-5klzp'
source_url: 'https://developer.apple.com/documentation/foundation/progressreporter/summary(of:)-5klzp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressreporter/summary%28of%3A%29-5klzp.json'
content_hash: 'sha256:3c8645640090a3ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProgressReporter](../progressreporter.md)

# summary(of:)

<sub>Instance Method</sub>

Returns a summary for the specified string property across the progress subtree.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func summary<P>(of property: KeyPath<ProgressManager.Properties, P.Type>) -> [String?] where P : ProgressManager.Property, P.Summary == [String?], P.Value == String?
```

## Parameters

- `property` — The type of the string property to summarize. Must be a property where both the value and summary types are `String`.

## Return Value

The aggregated summary value for the specified property across the entire subtree.

## Discussion

This method aggregates the values of a custom string property from the underlying progress manager and all its children, returning a consolidated summary value.
