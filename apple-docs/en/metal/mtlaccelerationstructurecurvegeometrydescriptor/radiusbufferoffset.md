---
title: radiusBufferOffset
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/radiusbufferoffset
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/radiusbufferoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/radiusbufferoffset.json'
content_hash: 'sha256:03f74ff9bef6bf23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureCurveGeometryDescriptor](../mtlaccelerationstructurecurvegeometrydescriptor.md)

# radiusBufferOffset

<sub>Instance Property</sub>

The offset, in bytes, to the radius data in the buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var radiusBufferOffset: Int { get set }
```

## Discussion

The offset needs to be a multiple of the radius format you configure with the [radiusFormat](radiusformat.md) property. You also need to align the offset to both the radius format’s size and the platform’s buffer alignment requirement.
