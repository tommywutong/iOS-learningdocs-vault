---
title: evictsObjectsWithDiscardedContent
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscache/evictsobjectswithdiscardedcontent
source_url: 'https://developer.apple.com/documentation/foundation/nscache/evictsobjectswithdiscardedcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscache/evictsobjectswithdiscardedcontent.json'
content_hash: 'sha256:fa9178b95abfd197'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCache](../nscache.md)

# evictsObjectsWithDiscardedContent

<sub>Instance Property</sub>

Whether the cache will automatically evict discardable-content objects whose content has been discarded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var evictsObjectsWithDiscardedContent: Bool { get set }
```

## Discussion

If [true](../../swift/true.md), the cache will evict a discardable-content object after its content is discarded. If [false](../../swift/false.md), it will not. The default value is [true](../../swift/true.md).

## See Also

### Managing Discardable Content

- [NSDiscardableContent](../nsdiscardablecontent.md) — You implement this protocol when a class’s objects have subcomponents that can be discarded when not being used, thereby giving an application a smaller memory footprint.
