---
title: maxThreadgroupMemoryLength
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/maxthreadgroupmemorylength
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/maxthreadgroupmemorylength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/maxthreadgroupmemorylength.json'
content_hash: 'sha256:065587e67e7a703a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# maxThreadgroupMemoryLength

<sub>Instance Property</sub>

The maximum threadgroup memory available to a compute kernel, in bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxThreadgroupMemoryLength: Int { get }
```

## See Also

### Checking compute support

- [maxThreadsPerThreadgroup](maxthreadsperthreadgroup.md) — The maximum number of threads along each dimension of a threadgroup.
