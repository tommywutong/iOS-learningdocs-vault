---
title: uncached
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdata/readingoptions/uncached
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/readingoptions/uncached'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/readingoptions/uncached.json'
content_hash: 'sha256:fbe07dd8cd689c97'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSData](../../nsdata.md) · [ReadingOptions](../readingoptions.md)

# uncached

<sub>Type Property</sub>

A hint indicating the file should not be stored in the file-system caches.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var uncached: NSData.ReadingOptions { get }
```

## Discussion

For data being read once and discarded, this option can improve performance.

## See Also

### Constants

- [NSDataReadingMappedIfSafe](mappedifsafe.md) — A hint indicating the file should be mapped into virtual memory, if possible and safe.
- [NSDataReadingMappedAlways](alwaysmapped.md) — Hint to map the file in if possible.
