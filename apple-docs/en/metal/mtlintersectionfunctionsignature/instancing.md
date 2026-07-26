---
title: instancing
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlintersectionfunctionsignature/instancing
source_url: 'https://developer.apple.com/documentation/metal/mtlintersectionfunctionsignature/instancing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlintersectionfunctionsignature/instancing.json'
content_hash: 'sha256:993e94f09bf522f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIntersectionFunctionSignature](../mtlintersectionfunctionsignature.md)

# instancing

<sub>Type Property</sub>

A flag indicating that function signature uses instancing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var instancing: MTLIntersectionFunctionSignature { get }
```

## Discussion

The corresponding MSL function needs to contain the `instancing` tag in its declaration.

## See Also

### Specifying the intersection function signature

- [MTLIntersectionFunctionSignatureTriangleData](triangledata.md) — A flag indicating that function signature uses triangle data.
- [MTLIntersectionFunctionSignatureWorldSpaceData](worldspacedata.md) — A flag indicating that function signature uses world space data.
