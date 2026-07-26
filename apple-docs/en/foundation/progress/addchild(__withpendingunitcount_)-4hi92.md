---
title: 'addChild(_:withPendingUnitCount:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/foundation/progress/addchild(_:withpendingunitcount:)-4hi92'
source_url: 'https://developer.apple.com/documentation/foundation/progress/addchild(_:withpendingunitcount:)-4hi92'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progress/addchild%28_%3Awithpendingunitcount%3A%29-4hi92.json'
content_hash: 'sha256:dbd1baea5f5c1f0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Progress](../progress.md)

# addChild(_:withPendingUnitCount:)

<sub>Instance Method</sub>

Adds a ProgressReporter as a child to a Progress, which constitutes a portion of Progress’s totalUnitCount.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addChild(_ reporter: ProgressReporter, withPendingUnitCount count: Int)
```

## Parameters

- `reporter` — A `ProgressReporter` instance.

- `count` — Number of units delegated from `self`’s `totalCount`.
