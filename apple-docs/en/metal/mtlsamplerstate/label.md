---
title: label
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsamplerstate/label
source_url: 'https://developer.apple.com/documentation/metal/mtlsamplerstate/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsamplerstate/label.json'
content_hash: 'sha256:b001275f0ac76d99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSamplerState](../mtlsamplerstate.md)

# label

<sub>Instance Property</sub>

A string that identifies the sampler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String? { get }
```

## Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [Naming resources and commands](../../xcode/naming-resources-and-commands.md).

## See Also

### Identifying the sampler

- [device](device.md) — The device object that created the sampler.
