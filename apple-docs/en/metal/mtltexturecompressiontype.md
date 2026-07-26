---
title: MTLTextureCompressionType
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.5+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltexturecompressiontype
source_url: 'https://developer.apple.com/documentation/metal/mtltexturecompressiontype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexturecompressiontype.json'
content_hash: 'sha256:990ce552d7a19d70'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTextureCompressionType

<sub>Enumeration</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLTextureCompressionType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [MTLTextureCompressionTypeLossless](mtltexturecompressiontype/lossless.md)
- [MTLTextureCompressionTypeLossy](mtltexturecompressiontype/lossy.md)

### Initializers

- [init(rawValue:)](<mtltexturecompressiontype/init(rawvalue_).md>)

## See Also

### Texture basics

- [Understanding color-renderable pixel format sizes](understanding-color-renderable-pixel-format-sizes.md) — Know the size limits of color render targets in Apple GPUs based on the target’s pixel format.
- [Optimizing texture data](optimizing-texture-data.md) — Optimize a texture’s data to improve GPU or CPU access.
- [MTLTexture](mtltexture.md) — A resource that holds formatted image data.
- [MTLTextureDescriptor](mtltexturedescriptor.md) — An instance that you use to configure new Metal texture instances.
- [MTKTextureLoader](../metalkit/mtktextureloader.md) — An object that creates textures from existing data in common image formats.
- [MTLSharedTextureHandle](mtlsharedtexturehandle.md) — A texture handle that can be shared across process address space boundaries.
- [MTLPixelFormat](mtlpixelformat.md) — The data formats that describe the organization and characteristics of individual pixels in a texture.
