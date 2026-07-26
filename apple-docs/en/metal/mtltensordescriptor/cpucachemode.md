---
title: cpuCacheMode
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltensordescriptor/cpucachemode
source_url: 'https://developer.apple.com/documentation/metal/mtltensordescriptor/cpucachemode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensordescriptor/cpucachemode.json'
content_hash: 'sha256:bc5a2d4f57af9b8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensorDescriptor](../mtltensordescriptor.md)

# cpuCacheMode

<sub>Instance Property</sub>

A value that configures the cache mode of CPU mapping of tensors you create with this descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var cpuCacheMode: MTLCPUCacheMode { get set }
```

## Discussion

The default value of this property is [MTLCPUCacheModeDefaultCache](../mtlcpucachemode/defaultcache.md).
