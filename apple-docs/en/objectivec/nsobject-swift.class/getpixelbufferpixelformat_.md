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
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# getPixelBufferPixelFormat:

<sub>Instance Method</sub>

<sub>macOS</sub>

```objc
- (void) getPixelBufferPixelFormat:(OSType *) pixelFormatOut;
```

## Parameters

- `pixelFormatOut` — The pixel format to be used for the CVPixelBufferRef instances passed to renderIntoPixelBuffer:forTime:.

## Discussion

This method is optional. Called once after setVideoDataSource:, if implemented.
