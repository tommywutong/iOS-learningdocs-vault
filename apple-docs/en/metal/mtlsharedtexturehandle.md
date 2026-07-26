---
title: MTLSharedTextureHandle
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsharedtexturehandle
source_url: 'https://developer.apple.com/documentation/metal/mtlsharedtexturehandle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsharedtexturehandle.json'
content_hash: 'sha256:0853c0a454f2bb02'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLSharedTextureHandle

<sub>Class</sub>

A texture handle that can be shared across process address space boundaries.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLSharedTextureHandle
```

## Overview

`MTLSharedTextureHandle` objects may be passed between processes using XPC connections and then used to create a reference to the texture in another process. The texture in the other process needs to be created using the same [MTLDevice](mtldevice.md) on which the shared texture was originally created. To identify which device it was created on, you can use the [device](mtlsharedtexturehandle/device.md) property of the `MTLSharedTextureHandle` object.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Identifying the shared texture handle

- [device](mtlsharedtexturehandle/device.md) — The device object that created the texture.
- [label](mtlsharedtexturehandle/label.md) — A string that identifies the texture.

### Initializers

- [init(coder:)](<mtlsharedtexturehandle/init(coder_).md>)

## See Also

### Texture basics

- [Understanding color-renderable pixel format sizes](understanding-color-renderable-pixel-format-sizes.md) — Know the size limits of color render targets in Apple GPUs based on the target’s pixel format.
- [Optimizing texture data](optimizing-texture-data.md) — Optimize a texture’s data to improve GPU or CPU access.
- [MTLTexture](mtltexture.md) — A resource that holds formatted image data.
- [MTLTextureCompressionType](mtltexturecompressiontype.md)
- [MTLTextureDescriptor](mtltexturedescriptor.md) — An instance that you use to configure new Metal texture instances.
- [MTKTextureLoader](../metalkit/mtktextureloader.md) — An object that creates textures from existing data in common image formats.
- [MTLPixelFormat](mtlpixelformat.md) — The data formats that describe the organization and characteristics of individual pixels in a texture.
