---
title: iosurface
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltexture/iosurface
source_url: 'https://developer.apple.com/documentation/metal/mtltexture/iosurface'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexture/iosurface.json'
content_hash: 'sha256:0946ac03f427964b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTexture](../mtltexture.md)

# iosurface

<sub>Instance Property</sub>

A reference to the underlying surface instance for the texture, if applicable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var iosurface: IOSurfaceRef? { get }
```

## Discussion

The property’s value is `nil` for textures that don’t come from an [IOSurface](../../iosurface/iosurface.md) instance.

## See Also

### Getting information about the IOSurface the texture was created from

- [iosurfacePlane](iosurfaceplane.md) — The number of a plane within the underlying surface instance for the texture, if applicable.
