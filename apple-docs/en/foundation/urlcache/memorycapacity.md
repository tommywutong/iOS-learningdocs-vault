---
title: memoryCapacity
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcache/memorycapacity
source_url: 'https://developer.apple.com/documentation/foundation/urlcache/memorycapacity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcache/memorycapacity.json'
content_hash: 'sha256:07a6e2e9dca6e5cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCache](../urlcache.md)

# memoryCapacity

<sub>Instance Property</sub>

The capacity of the in-memory cache, in bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var memoryCapacity: Int { get set }
```

## Discussion

At the time this property is set, the in-memory cache will truncate its contents to the size given, if necessary.

## See Also

### Getting and setting in-memory cache properties

- [currentMemoryUsage](currentmemoryusage.md) — The current size of the in-memory cache, in bytes.
