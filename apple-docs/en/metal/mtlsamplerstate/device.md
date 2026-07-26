---
title: device
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsamplerstate/device
source_url: 'https://developer.apple.com/documentation/metal/mtlsamplerstate/device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsamplerstate/device.json'
content_hash: 'sha256:b50eed8f0fef1a28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSamplerState](../mtlsamplerstate.md)

# device

<sub>Instance Property</sub>

The device object that created the sampler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var device: any MTLDevice { get }
```

## Discussion

A sampler is always associated with the [MTLDevice](../mtldevice.md) that created it and can be used only with that device.

## See Also

### Identifying the sampler

- [label](label.md) — A string that identifies the sampler.
