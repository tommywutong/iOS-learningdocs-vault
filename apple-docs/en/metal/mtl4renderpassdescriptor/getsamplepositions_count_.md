---
title: 'getSamplePositions:count:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4renderpassdescriptor/getsamplepositions:count:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4renderpassdescriptor/getsamplepositions:count:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4renderpassdescriptor/getsamplepositions%3Acount%3A.json'
content_hash: 'sha256:2754217a34271ee8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderPassDescriptor](../mtl4renderpassdescriptor.md)

# getSamplePositions:count:

<sub>Instance Method</sub>

Retrieves the previously-configured custom sample positions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (NSUInteger) getSamplePositions:(MTLSamplePosition *) positions count:(NSUInteger) count;
```

## Parameters

- `positions` — The destination array where Metal stores [MTLSamplePosition](../mtlsampleposition.md) instances.

- `count` — Number of [MTLSamplePosition](../mtlsampleposition.md) instances in the array. This array needs to be large enough to store all sample positions.

## Return Value

The number of previously-configured custom sample positions.

## Discussion

This method stores the app’s last set custom sample positions into an output array. Metal only modifies the array when the `count` parameter consists of a length sufficient to store the number of sample positions.
