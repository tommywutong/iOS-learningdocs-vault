---
title: 'getOpenGLBufferContext:pixelFormat:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/getopenglbuffercontext:pixelformat:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/getopenglbuffercontext:pixelformat:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/getopenglbuffercontext%3Apixelformat%3A.json'
content_hash: 'sha256:097c30afc84a343d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# getOpenGLBufferContext:pixelFormat:

<sub>Instance Method</sub>

<sub>macOS</sub>

```objc
- (void) getOpenGLBufferContext:(CGLContextObj*) contextOut pixelFormat:(CGLPixelFormatObj*) pixelFormatOut;
```

## Parameters

- `contextOut` — The OpenGL context to be used for the CVOpenGLBufferRef instances passed to renderIntoOpenGLBuffer:onScreen:forTime:.

- `pixelFormatOut` — The OpenGL pixel format to be used for the CVOpenGLBufferRef instances passed to renderIntoOpenGLBuffer:onScreen:forTime:.

## Discussion

This method is optional. Called once after setVideoDataSource:, if implemented.
