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
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# getOpenGLBufferContext:pixelFormat:

<sub>实例方法</sub>

<sub>macOS</sub>

```objc
- (void) getOpenGLBufferContext:(CGLContextObj*) contextOut pixelFormat:(CGLPixelFormatObj*) pixelFormatOut;
```

## 参数

- `contextOut` — 传递给 renderIntoOpenGLBuffer:onScreen:forTime: 的 CVOpenGLBufferRef 实例所使用的 OpenGL 上下文。

- `pixelFormatOut` — 传递给 renderIntoOpenGLBuffer:onScreen:forTime: 的 CVOpenGLBufferRef 实例所使用的 OpenGL 像素格式。

## 讨论

此方法是可选的。如果已实现，会在 setVideoDataSource: 之后调用一次。
