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
doc_path: /documentation/metal/mtlsamplerdescriptor/label
source_url: 'https://developer.apple.com/documentation/metal/mtlsamplerdescriptor/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsamplerdescriptor/label.json'
content_hash: 'sha256:781e1e1a887584e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSamplerDescriptor](../mtlsamplerdescriptor.md)

# label

<sub>Instance Property</sub>

A string that identifies the sampler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String? { get set }
```

## Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [Naming resources and commands](../../xcode/naming-resources-and-commands.md).
