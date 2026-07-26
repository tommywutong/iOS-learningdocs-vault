---
title: 'start(totalCount:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/foundation/subprogress/start(totalcount:)'
source_url: 'https://developer.apple.com/documentation/foundation/subprogress/start(totalcount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/subprogress/start%28totalcount%3A%29.json'
content_hash: 'sha256:07cbe68a0f8632d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Subprogress](../subprogress.md)

# start(totalCount:)

<sub>Instance Method</sub>

Instantiates a ProgressManager which is a child to the parent from which `self` is returned.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
consuming func start(totalCount: Int?) -> ProgressManager
```

## Parameters

- `totalCount` — Total count of returned child `ProgressManager` instance.

## Return Value

A `ProgressManager` instance.
