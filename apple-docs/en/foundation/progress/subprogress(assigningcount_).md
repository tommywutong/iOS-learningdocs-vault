---
title: 'subprogress(assigningCount:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/foundation/progress/subprogress(assigningcount:)'
source_url: 'https://developer.apple.com/documentation/foundation/progress/subprogress(assigningcount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/subprogress%28assigningcount%3A%29.json'
content_hash: 'sha256:0b08697a661082f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# subprogress(assigningCount:)

<sub>Instance Method</sub>

Returns a Subprogress which can be passed to any method that reports progress It can be then used to create a child `ProgressManager` reporting to this `Progress`

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func subprogress(assigningCount count: Int) -> Subprogress
```

## Parameters

- `count` — Number of units delegated to a child instance of `ProgressManager` which may be instantiated by `Subprogress` later when `reporter(totalCount:)` is called.

## Return Value

A `Subprogress` instance.

## Discussion

Delegates a portion of totalUnitCount to a future child `ProgressManager` instance.
