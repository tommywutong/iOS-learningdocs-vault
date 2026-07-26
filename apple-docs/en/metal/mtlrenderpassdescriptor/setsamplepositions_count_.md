---
title: 'setSamplePositions:count:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrenderpassdescriptor/setsamplepositions:count:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/setsamplepositions:count:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassdescriptor/setsamplepositions%3Acount%3A.json'
content_hash: 'sha256:f5a4b5c27cf05115'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md)

# setSamplePositions:count:

<sub>Instance Method</sub>

Sets the programmable sample positions for a render pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setSamplePositions:(const MTLSamplePosition *) positions count:(NSUInteger) count;
```

## Parameters

- `positions` — An array of programmable sample positions for the render pass.

- `count` — The number of elements, which needs to match the render pass sample count, or `0` to disable custom sample positions.

## Discussion

Programmable sample positions need to be floating-point values in the `[0.0, 1.0)` range along each axis, with the origin `(0,0)` defined at the top-left corner. Values can be set from `0/16` up to `15/16`, inclusive, in 1`/16` increments along each axis.

If the value of `count` is `0`, the GPU uses the default sample positions for the render pass.

> [!note] Note
> Call the [- supportsTextureSampleCount:](<../mtldevice/supportstexturesamplecount(__).md>) method to determine whether the device object supports a specific sample count.

## See Also

### Using programmable sample positions

- [MTLSamplePositionMake](<../mtlsamplepositionmake(____).md>) — Returns a new sample position on a subpixel grid.
- [getSamplePositions:count:](getsamplepositions_count_.md) — Retrieves the programmable sample positions set for a render pass.
