---
title: NSCacheDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscachedelegate
source_url: 'https://developer.apple.com/documentation/foundation/nscachedelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscachedelegate.json'
content_hash: 'sha256:359f1d1545be185e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCacheDelegate

<sub>Protocol</sub>

The delegate of an [NSCache](nscache.md) object implements this protocol to perform specialized actions when an object is about to be evicted or removed from the cache.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSCacheDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to Object Eviction

- [- cache:willEvictObject:](<nscachedelegate/cache(__willevictobject_).md>) — Called when an object is about to be evicted or removed from the cache.

## See Also

### Managing the Delegate

- [delegate](nscache/delegate.md) — The cache’s delegate.
