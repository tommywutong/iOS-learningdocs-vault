---
title: MTLResourceViewPool
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresourceviewpool
source_url: 'https://developer.apple.com/documentation/metal/mtlresourceviewpool'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresourceviewpool.json'
content_hash: 'sha256:7867afee42441240'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLResourceViewPool

<sub>Protocol</sub>

Contains views over resources of a specific type, and allows you to manage those views.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLResourceViewPool : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [MTLTextureViewPool](mtltextureviewpool.md)

## Topics

### Instance Properties

- [baseResourceID](mtlresourceviewpool/baseresourceid.md) — Obtains the resource ID corresponding to the resource view at index 0 in this resource view pool.
- [device](mtlresourceviewpool/device.md) — Obtains a reference to the GPU device this pool belongs to.
- [label](mtlresourceviewpool/label.md) — Queries the optional debug label of this resource view pool.
- [resourceViewCount](mtlresourceviewpool/resourceviewcount.md) — Queries the number of resource views that this pool contains.

### Instance Methods

- [copyResourceViews(sourcePool:sourceRange:destinationIndex:)](<mtlresourceviewpool/copyresourceviews(sourcepool_sourcerange_destinationindex_).md>) — Copies a range of resource views from a source view pool to a destination location in this view pool.

## See Also

### View pools

- [MTLResourceViewPoolDescriptor](mtlresourceviewpooldescriptor.md) — Provides parameters for creating a resource view pool.
- [MTLTextureViewPool](mtltextureviewpool.md) — A pool of lightweight texture views.
- [MTLTextureViewDescriptor](mtltextureviewdescriptor.md)
