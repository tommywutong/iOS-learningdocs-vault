---
title: 'supportsFeatureSet(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtldevice/supportsfeatureset(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/supportsfeatureset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/supportsfeatureset%28_%3A%29.json'
content_hash: 'sha256:5d24bf058bba6137'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# supportsFeatureSet(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the GPU device supports a specific feature set.

> [!warning] Deprecated
> Use the [- supportsFamily:](<supportsfamily(__).md>) method instead if your app is running on an OS that supports that method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func supportsFeatureSet(_ featureSet: MTLFeatureSet) -> Bool
```

## Parameters

- `featureSet` — An [MTLFeatureSet](../mtlfeatureset.md) instance.

## See Also

### Related Documentation

- [Detecting GPU features and Metal software versions](../detecting-gpu-features-and-metal-software-versions.md) — Use the device object’s properties to determine how you perform tasks in Metal.

### Checking a GPU device’s feature support

- [- supportsFamily:](<supportsfamily(__).md>) — Returns a Boolean value that indicates whether the GPU device supports the feature set of a specific GPU family.
- [MTLGPUFamily](../mtlgpufamily.md) — Represents the functionality for families of GPUs.
- [MTLFeatureSet](../mtlfeatureset.md) — The device feature sets that define specific platform, hardware, and software configurations. _(deprecated)_
