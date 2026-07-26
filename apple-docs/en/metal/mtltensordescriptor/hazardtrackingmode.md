---
title: hazardTrackingMode
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltensordescriptor/hazardtrackingmode
source_url: 'https://developer.apple.com/documentation/metal/mtltensordescriptor/hazardtrackingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensordescriptor/hazardtrackingmode.json'
content_hash: 'sha256:f60d9666571c25d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensorDescriptor](../mtltensordescriptor.md)

# hazardTrackingMode

<sub>Instance Property</sub>

A value that configures the hazard tracking of tensors you create with this descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var hazardTrackingMode: MTLHazardTrackingMode { get set }
```

## Discussion

The default value of this property is [MTLHazardTrackingModeDefault](../mtlhazardtrackingmode/default.md).
