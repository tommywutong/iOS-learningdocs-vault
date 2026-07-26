---
title: 'init(cglContext:options:)'
framework: Core Animation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.5+（10.14 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/quartzcore/carenderer/init(cglcontext:options:)-1l3m2'
source_url: 'https://developer.apple.com/documentation/quartzcore/carenderer/init(cglcontext:options:)-1l3m2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/carenderer/init%28cglcontext%3Aoptions%3A%29-1l3m2.json'
content_hash: 'sha256:28bec22d8f7301aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CARenderer](../carenderer.md)

# init(cglContext:options:)

<sub>Initializer</sub>

Creates and returns a `CARenderer` instance with the render target specified by the Core OpenGL context.

> [!warning] Deprecated
> OpenGL is deprecated. (Define GL_SILENCE_DEPRECATION to silence these warnings)

<sub>Mac Catalyst, macOS</sub>

```swift
init(cglContext ctx: UnsafeMutableRawPointer, options dict: [AnyHashable : Any]? = nil)
```

## Parameters

- `ctx` — A Core OpenGL render context that is used as the render target.

- `dict` — A dictionary of optional parameters.

## Return Value

A new instance of `CARenderer` that will use `ctx` as the render target.

## See Also

### Creating a Renderer

- [+ rendererWithMTLTexture:options:](<init(mtltexture_options_)-1cr0b.md>) — Creates a layer renderer from a Metal texture.
