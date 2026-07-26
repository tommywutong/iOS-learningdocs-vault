---
title: CGBitmapContextCreateAdaptive
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgbitmapcontextcreateadaptive
source_url: 'https://developer.apple.com/documentation/coregraphics/cgbitmapcontextcreateadaptive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgbitmapcontextcreateadaptive.json'
content_hash: 'sha256:64f7a517c2c0ba8f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGBitmapContextCreateAdaptive

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGContextRefCGBitmapContextCreateAdaptive(size_t width, size_t height, CFDictionaryRef auxiliaryInfo, bool (^onResolve)(const CGContentInfo *, CGBitmapParameters *), CGRenderingBufferProviderRef (^onAllocate)(const CGContentInfo *, const CGBitmapParameters *), void (^onFree)(CGRenderingBufferProviderRef , const CGContentInfo *, const CGBitmapParameters *), void (^onError)(CFErrorRef , const CGContentInfo *, const CGBitmapParameters *));
```
