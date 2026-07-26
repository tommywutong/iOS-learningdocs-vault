---
title: 'contextWithCGLContext:pixelFormat:options:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.4+（10.6 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/coreimage/cicontext/contextwithcglcontext:pixelformat:options:'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/contextwithcglcontext:pixelformat:options:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/contextwithcglcontext%3Apixelformat%3Aoptions%3A.json'
content_hash: 'sha256:52b729db2cd2cb41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# contextWithCGLContext:pixelFormat:options:

<sub>Type Method</sub>

Creates a Core Image context from a CGL context, using the specified options and pixel format object.

> [!warning] Deprecated
> Instead use [+ contextWithCGLContext:pixelFormat:colorSpace:options:](<init(cglcontext_pixelformat_colorspace_options_)-6rp6d.md>).

<sub>macOS</sub>

```objc
+ (CIContext *) contextWithCGLContext:(CGLContextObj) cglctx pixelFormat:(CGLPixelFormatObj) pixelFormat options:(NSDictionary<NSString *,id> *) options;
```

## Parameters

- `cglctx` — A CGL context (`CGLContextObj` object) obtain by calling the CGL function `CGLCreateContext`.

- `pixelFormat` — A CGL pixel format object (`CGLPixelFormatObj` object) created by calling the CGL function `CGLChoosePixelFormat`. This argument must be the same pixel format object used to create the CGL context. The pixel format object must be valid for the lifetime of the Core Image context. Don’t release the pixel format object until after you release the Core Image context.

- `options` — A dictionary that contains color space information. You can provide the keys [kCIContextOutputColorSpace](../cicontextoption/outputcolorspace.md) or [kCIContextWorkingColorSpace](../cicontextoption/workingcolorspace.md) along with a [CGColorSpace](../../coregraphics/cgcolorspace.md) object for each color space.

## See Also

### Related Documentation

- [+ contextWithCGContext:options:](<init(cgcontext_options_)-6p78w.md>) — Creates a Core Image context from a Quartz context, using the specified options.

### Deprecated

- [+ contextWithCGLContext:pixelFormat:colorSpace:options:](<init(cglcontext_pixelformat_colorspace_options_)-6rp6d.md>) — Creates a Core Image context from a CGL context, using the specified options, color space, and pixel format object. _(deprecated)_
- [+ contextWithEAGLContext:](<init(eaglcontext_)-8ajef.md>) — Creates a Core Image context from an EAGL context. _(deprecated)_
- [+ contextWithEAGLContext:options:](<init(eaglcontext_options_)-6uyqj.md>) — Creates a Core Image context from an EAGL context using the specified options. _(deprecated)_
- [- createCGLayerWithSize:info:](<createcglayer(with_info_).md>) — Creates a CGLayer object from the provided parameters. _(deprecated)_
- [- drawImage:atPoint:fromRect:](<draw(__at_from_).md>) — Renders a region of an image to a point in the context destination. _(deprecated)_
