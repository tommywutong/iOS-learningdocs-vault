---
title: stable
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nssortoptions/stable
source_url: 'https://developer.apple.com/documentation/foundation/nssortoptions/stable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssortoptions/stable.json'
content_hash: 'sha256:5049bdc17f9d4a17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSortOptions](../nssortoptions.md)

# stable

<sub>Type Property</sub>

Specifies that the sorted results should return compared items having equal value in the order they occurred originally.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var stable: NSSortOptions { get }
```

## Discussion

If this option is unspecified, equal objects may, or may not be returned in their original order.

## See Also

### Constants

- [NSSortConcurrent](concurrent.md) — Specifies that the Block sort operation should be concurrent.
