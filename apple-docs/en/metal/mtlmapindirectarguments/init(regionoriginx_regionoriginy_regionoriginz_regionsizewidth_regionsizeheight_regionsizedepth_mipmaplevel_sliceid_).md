---
title: 'init(regionOriginX:regionOriginY:regionOriginZ:regionSizeWidth:regionSizeHeight:regionSizeDepth:mipMapLevel:sliceId:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlmapindirectarguments/init(regionoriginx:regionoriginy:regionoriginz:regionsizewidth:regionsizeheight:regionsizedepth:mipmaplevel:sliceid:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlmapindirectarguments/init(regionoriginx:regionoriginy:regionoriginz:regionsizewidth:regionsizeheight:regionsizedepth:mipmaplevel:sliceid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlmapindirectarguments/init%28regionoriginx%3Aregionoriginy%3Aregionoriginz%3Aregionsizewidth%3Aregionsizeheight%3Aregionsizedepth%3Amipmaplevel%3Asliceid%3A%29.json'
content_hash: 'sha256:2a947b354217426e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLMapIndirectArguments](../mtlmapindirectarguments.md)

# init(regionOriginX:regionOriginY:regionOriginZ:regionSizeWidth:regionSizeHeight:regionSizeDepth:mipMapLevel:sliceId:)

<sub>Initializer</sub>

Returns a new data layout for mapping sparse texture regions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(regionOriginX: UInt32, regionOriginY: UInt32, regionOriginZ: UInt32, regionSizeWidth: UInt32, regionSizeHeight: UInt32, regionSizeDepth: UInt32, mipMapLevel: UInt32, sliceId: UInt32)
```

## Parameters

- `regionOriginX` — The x coordinate of the region to change, measured in tile coordinates.

- `regionOriginY` — The y coordinate of the region to change, measured in tile coordinates.

- `regionOriginZ` — The z coordinate of the region to change, measured in tile coordinates.

- `regionSizeWidth` — The width of the region, measured in tile coordinates.

- `regionSizeHeight` — The height of the region, measured in tile coordinates.

- `regionSizeDepth` — The depth of the region, measured in tile coordinates.

- `mipMapLevel` — The mipmap to change.

- `sliceId` — The texture slice to change.

## See Also

### Creating indirect mapping arguments

- [init()](<init().md>) — Returns a default data layout for mapping sparse texture regions.
