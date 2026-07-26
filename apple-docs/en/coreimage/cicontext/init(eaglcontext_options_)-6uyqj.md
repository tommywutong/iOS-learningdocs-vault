---
title: 'init(eaglContext:options:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+（12.0 起废弃）, iPadOS 5.0+（12.0 起废弃）, tvOS（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coreimage/cicontext/init(eaglcontext:options:)-6uyqj'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/init(eaglcontext:options:)-6uyqj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/init%28eaglcontext%3Aoptions%3A%29-6uyqj.json'
content_hash: 'sha256:c85cfcdefdf739ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# init(eaglContext:options:)

<sub>Initializer</sub>

Creates a Core Image context from an EAGL context using the specified options.

> [!warning] Deprecated
> Core Image OpenGLES API deprecated. (Define CI_SILENCE_GL_DEPRECATION to silence these warnings)

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
init(eaglContext: EAGLContext, options: [CIContextOption : Any]? = nil)
```

## Parameters

- `eaglContext` — The EAGL context to render to.

- `options` — A dictionary that contains options for creating a [CIContext](../cicontext.md) object. You can pass any of the keys defined in [CIContextOption](../cicontextoption.md) along with the appropriate value.

## Return Value

A Core Image context that targets OpenGL ES.

## Discussion

The OpenGL ES context must support OpenGL ES 2.0. All drawing performed using the methods listed in Drawing Images is rendered directly into the context.

## See Also

### Deprecated

- [+ contextWithCGLContext:pixelFormat:colorSpace:options:](<init(cglcontext_pixelformat_colorspace_options_)-6rp6d.md>) — Creates a Core Image context from a CGL context, using the specified options, color space, and pixel format object. _(deprecated)_
- [+ contextWithEAGLContext:](<init(eaglcontext_)-8ajef.md>) — Creates a Core Image context from an EAGL context. _(deprecated)_
- [init(forOfflineGPUAtIndex:)](<init(forofflinegpuatindex_).md>) — Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display. _(deprecated)_
- [init(forOfflineGPUAtIndex:colorSpace:options:sharedContext:)](<init(forofflinegpuatindex_colorspace_options_sharedcontext_).md>) — Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display, with the specified options. _(deprecated)_
- [- createCGLayerWithSize:info:](<createcglayer(with_info_).md>) — Creates a CGLayer object from the provided parameters. _(deprecated)_
- [- drawImage:atPoint:fromRect:](<draw(__at_from_).md>) — Renders a region of an image to a point in the context destination. _(deprecated)_
