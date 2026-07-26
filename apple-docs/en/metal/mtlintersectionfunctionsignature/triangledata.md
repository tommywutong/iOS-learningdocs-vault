---
title: triangleData
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlintersectionfunctionsignature/triangledata
source_url: 'https://developer.apple.com/documentation/metal/mtlintersectionfunctionsignature/triangledata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlintersectionfunctionsignature/triangledata.json'
content_hash: 'sha256:804258ecd878a9c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIntersectionFunctionSignature](../mtlintersectionfunctionsignature.md)

# triangleData

<sub>Type Property</sub>

A flag indicating that function signature uses triangle data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var triangleData: MTLIntersectionFunctionSignature { get }
```

## Discussion

The corresponding MSL function needs to contain the `triangle_data` tag in its declaration.

## See Also

### Specifying the intersection function signature

- [MTLIntersectionFunctionSignatureInstancing](instancing.md) — A flag indicating that function signature uses instancing.
- [MTLIntersectionFunctionSignatureWorldSpaceData](worldspacedata.md) — A flag indicating that function signature uses world space data.
