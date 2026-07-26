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
doc_path: '/documentation/foundation/progressmanager/subprogress(assigningcount:)'
source_url: 'https://developer.apple.com/documentation/foundation/progressmanager/subprogress(assigningcount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressmanager/subprogress%28assigningcount%3A%29.json'
content_hash: 'sha256:61209a20d3200483'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProgressManager](../progressmanager.md)

# subprogress(assigningCount:)

<sub>Instance Method</sub>

Returns a `Subprogress` representing a portion of `self` which can be passed to any method that reports progress.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func subprogress(assigningCount portionOfParentTotal: Int) -> Subprogress
```

## Parameters

- `portionOfParentTotal` — The portion of `totalCount` to be delegated to the `Subprogress`.

## Return Value

A `Subprogress` instance.

## Discussion

If the `Subprogress` is not converted into a `ProgressManager` (for example, due to an error or early return), then the assigned count is marked as completed in the parent `ProgressManager`.
