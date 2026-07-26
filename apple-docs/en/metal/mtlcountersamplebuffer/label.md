---
title: label
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcountersamplebuffer/label
source_url: 'https://developer.apple.com/documentation/metal/mtlcountersamplebuffer/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcountersamplebuffer/label.json'
content_hash: 'sha256:8e9aecb86baae17a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounterSampleBuffer](../mtlcountersamplebuffer.md)

# label

<sub>Instance Property</sub>

A string that identifies the counter sample buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String { get }
```

## Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [Naming resources and commands](../../xcode/naming-resources-and-commands.md).

## See Also

### Inspecting the counter sample buffer’s configuration

- [device](device.md) — The GPU device instance that owns the counter sample buffer.
- [sampleCount](samplecount.md) — The number of samples in the buffer.
