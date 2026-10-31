---
title: 'getPixelBufferPixelFormat:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+（10.9 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/getpixelbufferpixelformat:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/getpixelbufferpixelformat:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/getpixelbufferpixelformat%3A.json'
content_hash: 'sha256:cccb02e1651b9700'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# getPixelBufferPixelFormat:

<sub>实例方法</sub>

<sub>macOS</sub>

```objc
- (void) getPixelBufferPixelFormat:(OSType *) pixelFormatOut;
```

## 参数

- `pixelFormatOut` — 传递给 renderIntoPixelBuffer:forTime: 的 CVPixelBufferRef 实例所使用的像素格式。

## 讨论

此方法是可选的。如果已实现，会在 setVideoDataSource: 之后调用一次。
