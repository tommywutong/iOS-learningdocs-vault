---
title: iosurfacePlane
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltexture/iosurfaceplane
source_url: 'https://developer.apple.com/documentation/metal/mtltexture/iosurfaceplane'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexture/iosurfaceplane.json'
content_hash: 'sha256:350043d5fffd2539'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTexture](../mtltexture.md)

# iosurfacePlane

<sub>Instance Property</sub>

The number of a plane within the underlying surface instance for the texture, if applicable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var iosurfacePlane: Int { get }
```

## Discussion

The plane number applies to the [iosurfacePlane](iosurfaceplane.md) property when it isn’t `nil`. The property’s value defaults to `0` for textures that don’t come from an [IOSurface](../../iosurface/iosurface.md) instance.

## See Also

### Getting information about the IOSurface the texture was created from

- [iosurface](iosurface.md) — A reference to the underlying surface instance for the texture, if applicable.
