---
title: 'getSamplePositions:count:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrenderpassdescriptor/getsamplepositions:count:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/getsamplepositions:count:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassdescriptor/getsamplepositions%3Acount%3A.json'
content_hash: 'sha256:e15db35bf50eeb40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassDescriptor](../mtlrenderpassdescriptor.md)

# getSamplePositions:count:

<sub>Instance Method</sub>

Retrieves the programmable sample positions set for a render pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (NSUInteger) getSamplePositions:(MTLSamplePosition *) positions count:(NSUInteger) count;
```

## Parameters

- `positions` — A pointer to a destination array of sample positions where Metal writes the programmable sample positions.

- `count` — The number of programmable sample positions to retrieve.

## Return Value

The total number of programmable sample positions set for the render pass.

## Discussion

The value of `count` needs to be equal to the number of programmable sample positions set by a previous call to the [setSamplePositions:count:](setsamplepositions_count_.md) method (the `count` parameter). Also, the `positions` array needs to contain at least as many elements as the value of `count`.

If you don’t know the correct value for `count`, you may query this method by passing a `nil` array for `positions` and a `0` value for `count`. This method returns the number of programmable sample positions that are currently set.

## See Also

### Using programmable sample positions

- [MTLSamplePositionMake](<../mtlsamplepositionmake(____).md>) — Returns a new sample position on a subpixel grid.
- [setSamplePositions:count:](setsamplepositions_count_.md) — Sets the programmable sample positions for a render pass.
