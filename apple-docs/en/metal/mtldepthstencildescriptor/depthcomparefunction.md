---
title: depthCompareFunction
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldepthstencildescriptor/depthcomparefunction
source_url: 'https://developer.apple.com/documentation/metal/mtldepthstencildescriptor/depthcomparefunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldepthstencildescriptor/depthcomparefunction.json'
content_hash: 'sha256:c3e87f0569f3dded'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDepthStencilDescriptor](../mtldepthstencildescriptor.md)

# depthCompareFunction

<sub>Instance Property</sub>

The comparison that is performed between a fragment’s depth value and the depth value in the attachment, which determines whether to discard the fragment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var depthCompareFunction: MTLCompareFunction { get set }
```

## Discussion

The default value is [MTLCompareFunctionAlways](../mtlcomparefunction/always.md), which indicates that the depth test always passes and the fragment remains a candidate to replace the data at the specified location. For more information on possible values, see [MTLCompareFunction](../mtlcomparefunction.md).

## See Also

### Related Documentation

- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)

### Specifying depth operations

- [depthWriteEnabled](isdepthwriteenabled.md) — A Boolean value that indicates whether depth values can be written to the depth attachment.
