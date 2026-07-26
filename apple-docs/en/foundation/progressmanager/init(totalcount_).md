---
title: 'init(totalCount:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/foundation/progressmanager/init(totalcount:)'
source_url: 'https://developer.apple.com/documentation/foundation/progressmanager/init(totalcount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressmanager/init%28totalcount%3A%29.json'
content_hash: 'sha256:bf399d41b3c3f98c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProgressManager](../progressmanager.md)

# init(totalCount:)

<sub>Initializer</sub>

Initializes `self` with `totalCount`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(totalCount: Int?)
```

## Parameters

- `totalCount` — Total units of work.

## Discussion

If `totalCount` is set to `nil`, `self` is indeterminate.
