---
title: isDepthWriteEnabled
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldepthstencildescriptor/isdepthwriteenabled
source_url: 'https://developer.apple.com/documentation/metal/mtldepthstencildescriptor/isdepthwriteenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldepthstencildescriptor/isdepthwriteenabled.json'
content_hash: 'sha256:f49e4cf9ae0e80f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDepthStencilDescriptor](../mtldepthstencildescriptor.md)

# isDepthWriteEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether depth values can be written to the depth attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isDepthWriteEnabled: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md), which indicates the depth attachment is read-only.

## See Also

### Specifying depth operations

- [depthCompareFunction](depthcomparefunction.md) — The comparison that is performed between a fragment’s depth value and the depth value in the attachment, which determines whether to discard the fragment.
