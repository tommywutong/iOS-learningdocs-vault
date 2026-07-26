---
title: MTLResourceViewPoolDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresourceviewpooldescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlresourceviewpooldescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresourceviewpooldescriptor.json'
content_hash: 'sha256:4e0b93d32cf354d2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLResourceViewPoolDescriptor

<sub>Class</sub>

Provides parameters for creating a resource view pool.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLResourceViewPoolDescriptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [label](mtlresourceviewpooldescriptor/label.md) — Assigns an optional label you to the resource view pool for debugging purposes.
- [resourceViewCount](mtlresourceviewpooldescriptor/resourceviewcount.md) — Configures the number of resource views with which Metal creates the resource view pool.

## See Also

### View pools

- [MTLResourceViewPool](mtlresourceviewpool.md) — Contains views over resources of a specific type, and allows you to manage those views.
- [MTLTextureViewPool](mtltextureviewpool.md) — A pool of lightweight texture views.
- [MTLTextureViewDescriptor](mtltextureviewdescriptor.md)
