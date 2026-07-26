---
title: MTKTextureLoader.ArrayCallback
framework: MetalKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metalkit/mtktextureloader/arraycallback
source_url: 'https://developer.apple.com/documentation/metalkit/mtktextureloader/arraycallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metalkit/mtktextureloader/arraycallback.json'
content_hash: 'sha256:8e678b3cf0c9628e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MetalKit](../../metalkit.md) · [MTKTextureLoader](../mtktextureloader.md)

# MTKTextureLoader.ArrayCallback

<sub>Type Alias</sub>

The signature for the block executed after an asynchronous loading operation for multiple textures has completed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
typealias ArrayCallback = ([any MTLTexture], (any Error)?) -> Void
```

## Discussion

The block parameters are defined as follows:

- **textures** — An array of [MTLTexture](../../metal/mtltexture.md) objects whose order corresponds to the requested textures. If an error occurs when loading a texture, an [NSNull](../../foundation/nsnull.md) object occupies its place in the array.
- **error** — If all texture loading operations were successful, this value is `nil`; otherwise, this parameter holds an [NSError](../../foundation/nserror.md) object that describes the first problem that occurred. (Which element in the input array the error corresponds to is undefined.)

## See Also

### Completing a Texture Loading Operation

- [Callback](callback.md) — The signature for the block executed after an asynchronous loading operation for a single texture has completed.
