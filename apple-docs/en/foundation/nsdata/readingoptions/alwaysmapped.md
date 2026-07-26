---
title: alwaysMapped
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdata/readingoptions/alwaysmapped
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/readingoptions/alwaysmapped'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/readingoptions/alwaysmapped.json'
content_hash: 'sha256:aebcda1fde52fe58'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSData](../../nsdata.md) · [ReadingOptions](../readingoptions.md)

# alwaysMapped

<sub>Type Property</sub>

Hint to map the file in if possible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var alwaysMapped: NSData.ReadingOptions { get }
```

## Discussion

This takes precedence over [NSDataReadingMappedIfSafe](mappedifsafe.md) if both are given.

## See Also

### Constants

- [NSDataReadingMappedIfSafe](mappedifsafe.md) — A hint indicating the file should be mapped into virtual memory, if possible and safe.
- [NSDataReadingUncached](uncached.md) — A hint indicating the file should not be stored in the file-system caches.
