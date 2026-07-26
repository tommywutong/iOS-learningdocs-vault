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
doc_path: '/documentation/foundation/progressmanager/summary(of:)-7jb53'
source_url: 'https://developer.apple.com/documentation/foundation/progressmanager/summary(of:)-7jb53'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressmanager/summary%28of%3A%29-7jb53.json'
content_hash: 'sha256:e459d6f4a73408a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProgressManager](../progressmanager.md)

# summary(of:)

<sub>Instance Method</sub>

Returns a summary for a custom unsigned integer property across the progress subtree.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func summary<P>(of property: KeyPath<ProgressManager.Properties, P.Type>) -> P.Summary where P : ProgressManager.Property, P.Summary == [UInt64], P.Value == UInt64
```

## Parameters

- `property` — The type of the unsigned integer property to summarize. Must be a property where the value type is `UInt64` and the summary type is `[UInt64]`.

## Return Value

A `[UInt64]` summary value for the specified property.

## Discussion

This method aggregates the values of a custom unsigned integer property from this progress manager and all its children, returning a consolidated summary value as an array of UInt64 values.
