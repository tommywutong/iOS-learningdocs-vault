---
title: device
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcountersamplebuffer/device
source_url: 'https://developer.apple.com/documentation/metal/mtlcountersamplebuffer/device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcountersamplebuffer/device.json'
content_hash: 'sha256:1ed4e0730da2c79d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounterSampleBuffer](../mtlcountersamplebuffer.md)

# device

<sub>Instance Property</sub>

The GPU device instance that owns the counter sample buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var device: any MTLDevice { get }
```

## Discussion

You can store a GPU device’s counter set data only with a counter sample buffer that you create from the same device.

## See Also

### Inspecting the counter sample buffer’s configuration

- [label](label.md) — A string that identifies the counter sample buffer.
- [sampleCount](samplecount.md) — The number of samples in the buffer.
