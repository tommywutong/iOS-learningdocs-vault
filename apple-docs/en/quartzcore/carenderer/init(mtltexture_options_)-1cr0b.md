---
title: 'init(mtlTexture:options:)'
framework: Core Animation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/carenderer/init(mtltexture:options:)-1cr0b'
source_url: 'https://developer.apple.com/documentation/quartzcore/carenderer/init(mtltexture:options:)-1cr0b'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/carenderer/init%28mtltexture%3Aoptions%3A%29-1cr0b.json'
content_hash: 'sha256:45e47d3356714c6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CARenderer](../carenderer.md)

# init(mtlTexture:options:)

<sub>Initializer</sub>

Creates a layer renderer from a Metal texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(mtlTexture tex: any MTLTexture, options dict: [AnyHashable : Any]? = nil)
```

## See Also

### Creating a Renderer

- [+ rendererWithCGLContext:options:](<init(cglcontext_options_)-1l3m2.md>) — Creates and returns a `CARenderer` instance with the render target specified by the Core OpenGL context. _(deprecated)_
