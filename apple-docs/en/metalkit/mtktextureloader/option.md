---
title: MTKTextureLoader.Option
framework: MetalKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.0+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metalkit/mtktextureloader/option
source_url: 'https://developer.apple.com/documentation/metalkit/mtktextureloader/option'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metalkit/mtktextureloader/option.json'
content_hash: 'sha256:c8fdf73de44a3910'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MetalKit](../../metalkit.md) · [MTKTextureLoader](../mtktextureloader.md)

# MTKTextureLoader.Option

<sub>Structure</sub>

Keys and values used to specify loading options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct Option
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating Texture Loading Options

- [init(rawValue:)](<option/init(rawvalue_).md>) — Creates a texture loader option from a raw string value.

### Specifying Mipmap Options

- [MTKTextureLoaderOptionAllocateMipmaps](option/allocatemipmaps.md) — A key used to specify whether the texture loader should allocate memory for mipmaps in the texture.
- [MTKTextureLoaderOptionGenerateMipmaps](option/generatemipmaps.md) — A key used to specify whether the texture loader should generate mipmaps for the texture.

### Specifying Resource Options

- [MTKTextureLoaderOptionTextureCPUCacheMode](option/texturecpucachemode.md) — A key used to specify the CPU cache mode for the texture.
- [MTKTextureLoaderOptionTextureStorageMode](option/texturestoragemode.md) — A key used to specify the storage mode for the texture.
- [MTKTextureLoaderOptionTextureUsage](option/textureusage.md) — A key used to specify the intended usage of the texture.

### Specifying Origin Information

- [MTKTextureLoaderOptionOrigin](option/origin.md) — A key used to specify when to flip the pixel coordinates of the texture.
- [Origin](origin.md) — Options for specifying when to flip the pixel coordinates of the texture.

### Specifying Cube Layout

- [MTKTextureLoaderOptionCubeLayout](option/cubelayout.md) — A key used to specify how cube texture data is arranged in the source image.
- [CubeLayout](cubelayout.md) — Options for specifying how cube texture data is arranged in the source image.

### Specifying sRGB Options

- [MTKTextureLoaderOptionSRGB](option/srgb.md) — A key used to specify whether the texture data is stored as sRGB image data.

### Type Properties

- [MTKTextureLoaderOptionLoadAsArray](option/loadasarray.md)
