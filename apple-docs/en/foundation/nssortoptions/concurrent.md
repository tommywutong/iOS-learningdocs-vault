---
title: concurrent
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nssortoptions/concurrent
source_url: 'https://developer.apple.com/documentation/foundation/nssortoptions/concurrent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssortoptions/concurrent.json'
content_hash: 'sha256:2de8d05b8d04a009'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSortOptions](../nssortoptions.md)

# concurrent

<sub>Type Property</sub>

Specifies that the Block sort operation should be concurrent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var concurrent: NSSortOptions { get }
```

## Discussion

This option is a hint and may be ignored by the implementation under some circumstances; the code of the Block must be safe against concurrent invocation.

## See Also

### Constants

- [NSSortStable](stable.md) — Specifies that the sorted results should return compared items having equal value in the order they occurred originally.
