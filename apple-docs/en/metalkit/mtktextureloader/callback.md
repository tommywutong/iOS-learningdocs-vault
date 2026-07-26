---
title: MTKTextureLoader.Callback
framework: MetalKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.0+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metalkit/mtktextureloader/callback
source_url: 'https://developer.apple.com/documentation/metalkit/mtktextureloader/callback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metalkit/mtktextureloader/callback.json'
content_hash: 'sha256:9c8f9e31dac77361'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MetalKit](../../metalkit.md) · [MTKTextureLoader](../mtktextureloader.md)

# MTKTextureLoader.Callback

<sub>Type Alias</sub>

The signature for the block executed after an asynchronous loading operation for a single texture has completed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
typealias Callback = ((any MTLTexture)?, (any Error)?) -> Void
```

## Discussion

The block parameters are defined as follows:

- **texture** — A [MTLTexture](../../metal/mtltexture.md) object, or `nil` if an error occurred.
- **error** — If the operation was successful, this value is `nil`; otherwise, this parameter holds an [NSError](../../foundation/nserror.md) object that describes the problem that occurred.

## See Also

### Completing a Texture Loading Operation

- [ArrayCallback](arraycallback.md) — The signature for the block executed after an asynchronous loading operation for multiple textures has completed.
