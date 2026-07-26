---
title: 'supportsFamily(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/supportsfamily(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/supportsfamily(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/supportsfamily%28_%3A%29.json'
content_hash: 'sha256:4152ebdbf7f91ec0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# supportsFamily(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the GPU device supports the feature set of a specific GPU family.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func supportsFamily(_ gpuFamily: MTLGPUFamily) -> Bool
```

## Parameters

- `gpuFamily` — An [MTLGPUFamily](../mtlgpufamily.md) instance.

## See Also

### Checking a GPU device’s feature support

- [MTLGPUFamily](../mtlgpufamily.md) — Represents the functionality for families of GPUs.
- [- supportsFeatureSet:](<supportsfeatureset(__).md>) — Returns a Boolean value that indicates whether the GPU device supports a specific feature set. _(deprecated)_
- [MTLFeatureSet](../mtlfeatureset.md) — The device feature sets that define specific platform, hardware, and software configurations. _(deprecated)_
