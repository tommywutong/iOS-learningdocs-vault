---
title: diskCapacity
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcache/diskcapacity
source_url: 'https://developer.apple.com/documentation/foundation/urlcache/diskcapacity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcache/diskcapacity.json'
content_hash: 'sha256:ffbc9cca25077551'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCache](../urlcache.md)

# diskCapacity

<sub>Instance Property</sub>

The capacity of the on-disk cache, in bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var diskCapacity: Int { get set }
```

## Discussion

When set, the on-disk cache will truncate its contents to the given size, if necessary.

## See Also

### Getting and setting on-disk cache properties

- [currentDiskUsage](currentdiskusage.md) — The current size of the on-disk cache, in bytes.
