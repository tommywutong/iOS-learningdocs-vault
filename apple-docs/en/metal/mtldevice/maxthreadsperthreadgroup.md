---
title: maxThreadsPerThreadgroup
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/maxthreadsperthreadgroup
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/maxthreadsperthreadgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/maxthreadsperthreadgroup.json'
content_hash: 'sha256:626f315ef8328b09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# maxThreadsPerThreadgroup

<sub>Instance Property</sub>

The maximum number of threads along each dimension of a threadgroup.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxThreadsPerThreadgroup: MTLSize { get }
```

## Discussion

This property reports the maximum thread group size the device can support for a trivial shader. This size isn’t guaranteed for all shaders. For the actual thread group size of a specific compute shader, see the [maxTotalThreadsPerThreadgroup](../mtlcomputepipelinestate/maxtotalthreadsperthreadgroup.md) property of your compute pipeline state.

For more information on the specific threadgroup limits of each GPU family, see the Metal feature set tables:

- [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf)
- [Metal feature set tables (Numbers)](https://developer.apple.com/metal/metal-feature-set-tables.zip)

## See Also

### Checking compute support

- [maxThreadgroupMemoryLength](maxthreadgroupmemorylength.md) — The maximum threadgroup memory available to a compute kernel, in bytes.
