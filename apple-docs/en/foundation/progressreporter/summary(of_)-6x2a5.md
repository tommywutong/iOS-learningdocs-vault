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
doc_path: '/documentation/foundation/progressreporter/summary(of:)-6x2a5'
source_url: 'https://developer.apple.com/documentation/foundation/progressreporter/summary(of:)-6x2a5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressreporter/summary%28of%3A%29-6x2a5.json'
content_hash: 'sha256:effb58315cb3bb6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProgressReporter](../progressreporter.md)

# summary(of:)

<sub>Instance Method</sub>

Returns a summary for the specified URL property across the progress subtree.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func summary<P>(of property: KeyPath<ProgressManager.Properties, P.Type>) -> [URL?] where P : ProgressManager.Property, P.Summary == [URL?], P.Value == URL?
```

## Parameters

- `property` — The type of the URL property to summarize. Must be a property where both the value and summary types are `URL?` and `[URL?]` respectively.

## Return Value

The aggregated summary value for the specified property across the entire subtree.

## Discussion

This method aggregates the values of a custom URL property from the underlying progress manager and all its children, returning a consolidated summary value.
