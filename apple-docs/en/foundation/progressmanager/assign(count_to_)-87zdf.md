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
doc_path: '/documentation/foundation/progressmanager/assign(count:to:)-87zdf'
source_url: 'https://developer.apple.com/documentation/foundation/progressmanager/assign(count:to:)-87zdf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/progressmanager/assign%28count%3Ato%3A%29-87zdf.json'
content_hash: 'sha256:481c13e7c800854e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProgressManager](../progressmanager.md)

# assign(count:to:)

<sub>Instance Method</sub>

Adds a Foundation’s `Progress` instance as a child which constitutes a certain `count` of `self`’s `totalCount`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func assign(count: Int, to progress: Progress)
```

## Parameters

- `count` — Number of units delegated from `self`’s `totalCount`.

- `progress` — `Progress` which receives the delegated `count`.
