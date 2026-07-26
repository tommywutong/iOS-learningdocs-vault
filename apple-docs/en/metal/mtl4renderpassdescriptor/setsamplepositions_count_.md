---
title: 'setSamplePositions:count:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4renderpassdescriptor/setsamplepositions:count:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4renderpassdescriptor/setsamplepositions:count:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4renderpassdescriptor/setsamplepositions%3Acount%3A.json'
content_hash: 'sha256:ed414e75aebafb42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderPassDescriptor](../mtl4renderpassdescriptor.md)

# setSamplePositions:count:

<sub>Instance Method</sub>

Configures the custom sample positions to use in MSAA rendering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setSamplePositions:(const MTLSamplePosition *) positions count:(NSUInteger) count;
```

## Parameters

- `positions` — Array of [MTLSamplePosition](../mtlsampleposition.md) instances.

- `count` — Number of [MTLSamplePosition](../mtlsampleposition.md) instances in the array. This value needs to be a valid sample count, or `0` to disable custom sample positions.
