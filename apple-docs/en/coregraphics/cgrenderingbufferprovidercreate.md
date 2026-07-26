---
title: CGRenderingBufferProviderCreate
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgrenderingbufferprovidercreate
source_url: 'https://developer.apple.com/documentation/coregraphics/cgrenderingbufferprovidercreate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgrenderingbufferprovidercreate.json'
content_hash: 'sha256:b588aa83dafc03a7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGRenderingBufferProviderCreate

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGRenderingBufferProviderRefCGRenderingBufferProviderCreate(void *info, size_t size, void * (^lockPointer)(void *info), void (^unlockPointer)(void *info, void *pointer), void (^releaseInfo)(void *info));
```
