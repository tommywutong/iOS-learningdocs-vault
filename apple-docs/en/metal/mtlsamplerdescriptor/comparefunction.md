---
title: compareFunction
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsamplerdescriptor/comparefunction
source_url: 'https://developer.apple.com/documentation/metal/mtlsamplerdescriptor/comparefunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsamplerdescriptor/comparefunction.json'
content_hash: 'sha256:41ca9a104f53cbea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSamplerDescriptor](../mtlsamplerdescriptor.md)

# compareFunction

<sub>Instance Property</sub>

The sampler comparison function used when performing a sample compare operation on a depth texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var compareFunction: MTLCompareFunction { get set }
```

## Discussion

The default value is [MTLCompareFunctionNever](../mtlcomparefunction/never.md).

The [MTLFeatureSet_iOS_GPUFamily3_v1](../mtlfeatureset/ios_gpufamily3_v1.md) and [MTLFeatureSet_iOS_GPUFamily1_v1](../mtlfeatureset/ios_gpufamily1_v1.md) feature sets allow you to define a framework-side sampler comparison function for an [MTLSamplerState](../mtlsamplerstate.md) instance. All feature sets support shader-side sampler comparison functions, as described in the [Metal Shading Language Specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).

## See Also

### Declaring the depth comparison mode

- [MTLCompareFunction](../mtlcomparefunction.md) — Options used to specify how a sample compare operation should be performed on a depth texture.
