---
title: 'assign(count:to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/foundation/progressmanager/assign(count:to:)-98a77'
source_url: 'https://developer.apple.com/documentation/foundation/progressmanager/assign(count:to:)-98a77'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressmanager/assign%28count%3Ato%3A%29-98a77.json'
content_hash: 'sha256:0a6b38005bb09178'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProgressManager](../progressmanager.md)

# assign(count:to:)

<sub>Instance Method</sub>

Adds a `ProgressReporter` as a child, with its progress representing a portion of `self`’s progress.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func assign(count: Int, to reporter: ProgressReporter)
```

## Parameters

- `count` — Units, which is a portion of `totalCount`delegated to an instance of `Subprogress`.

- `reporter` — A `ProgressReporter` instance.

## Discussion

If a cycle is detected, this will cause a crash at runtime.
