---
title: 'setSamplePositions(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, macOS 10.13+, tvOS 11.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrenderpassdescriptor/setsamplepositions(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/setsamplepositions(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassdescriptor/setsamplepositions%28_%3A%29.json'
content_hash: 'sha256:90471026818da943'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md)

# setSamplePositions(_:)

<sub>Instance Method</sub>

Sets the programmable sample positions for a render pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setSamplePositions(_ positions: [MTLSamplePosition])
```

## Parameters

- `positions` — An array of programmable sample positions for the render pass with the the same number of elements as the render pass sample count, or an empty array to disable custom sample positions.

## Discussion

Programmable sample positions need to be floating-point values in the `[0.0, 1.0)` range along each axis, with the origin `(0,0)` defined at the top-left corner. Values can be set from `0/16` up to `15/16`, inclusive, in `1/16` increments along each axis.

If the length of the array is `0`, the GPU uses the default sample positions for the render pass.

> [!note] Note
> Call the [- supportsTextureSampleCount:](<../mtldevice/supportstexturesamplecount(__).md>) method to determine whether the device object supports a specific sample count.

## See Also

### Using programmable sample positions

- [MTLSamplePositionMake](<../mtlsamplepositionmake(____).md>) — Returns a new sample position on a subpixel grid.
- [getSamplePositions()](<getsamplepositions().md>) — Returns the programmable sample positions set for a render pass.
