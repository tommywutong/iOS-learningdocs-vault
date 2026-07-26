---
title: 'getDefaultSamplePositions:count:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/getdefaultsamplepositions:count:'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/getdefaultsamplepositions:count:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/getdefaultsamplepositions%3Acount%3A.json'
content_hash: 'sha256:31b9ded53756efb0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# getDefaultSamplePositions:count:

<sub>Instance Method</sub>

Retrieves the default sample positions for a specific sample count.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) getDefaultSamplePositions:(MTLSamplePosition *) positions count:(NSUInteger) count;
```

## Parameters

- `positions` — A pointer to a destination C array of [MTLSamplePosition](../mtlsampleposition.md) instances — with at least `count` elements — the method writes the default positions to.

- `count` — The number of points a GPU can sample from a texture. Ensure the GPU can support the `count` value by first calling the device’s [- supportsTextureSampleCount:](<supportstexturesamplecount(__).md>) method.

## Discussion

The default sample positions are the same on all GPUs that support programmable sample positions (see [programmableSamplePositionsSupported](areprogrammablesamplepositionssupported.md)).

> [!note] Note
> GPUs that don’t support programmable sample positions may have different default sample positions that you can’t retrieve.

The default sample position for GPUs that can sample one time is at the pixel’s center.

![](../../../../attachments/b82e8ada6eb98fc644df94e8d27c8eb1/positioning-samples-programmatically-2@2x.png)

<sub>Normalized coordinate system diagram that shows a subpixel grid with one point at the center, with coordinates zero-.5, zero-0.5.</sub>

The default sample positions for GPUs that can sample two times have locations in the center of the pixel’s second quadrant and fourth quadrants.

![](../../../../attachments/0326b2b19119cd5568f173d4087b10c4/getDefaultSamplePositions-2@2x.png)

<sub>Normalized coordinate system diagram that shows a subpixel grid with two points, one located at zero-.25, zero-0.25. and the other at zero-.75, zero-0.75.</sub>

The default sample positions for GPUs that can sample four times have one location in each of the pixel’s quadrants. Each location is at the center of one of that quadrant’s subquadrants.

![](../../../../attachments/75241ff22d0b2ee42446c2860eca985d/getDefaultSamplePositions-3@2x.png)

<sub>Normalized coordinate system diagram that shows a subpixel grid with four points. Each of the pixel’s four quadrants contains one point.</sub>

The default sample positions for GPUs that can sample eight times have two locations in each of the pixel’s quadrants.

![](../../../../attachments/b0987ba0ce96b5853f689931e9496f22/getDefaultSamplePositions-4@2x.png)

<sub>Normalized coordinate system diagram that shows a subpixel grid with four points. Each of the pixel’s four quadrants contains two points. </sub>

The table lists the indices and default locations for GPUs that support 1, 2, 4, or 8 sample positions.

| Sample count | Position indices | Subpixel coordinates |
|---|---|---|
| 1 | 0 | (0.5, 0.5) |
| 2 | 0 ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 1 | (0.75, 0.75) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (0.25, 0.25) |
| 4 | 0 ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 1 ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 2 ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 3 | (0.375, 0.125) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (0.875, 0.375) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (0.125, 0.625) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (0.625, 0.875) |
| 8 | 0 ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 1 ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 2 ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 3 ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 4 ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 5 ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 6 ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 7 | (0.5625, 0.3125) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (0.4375, 0.6875) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (0.8125, 0.5625) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (0.3125, 0.1875) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (0.1875, 0.8125) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (0.0625, 0.4375) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (0.6875, 0.9375) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (0.9375, 0.0625) |

## See Also

### Creating samplers

- [- supportsTextureSampleCount:](<supportstexturesamplecount(__).md>) — Returns a Boolean value that indicates whether the GPU can sample a texture with a specific number of sample points.
- [- newSamplerStateWithDescriptor:](<makesamplerstate(descriptor_).md>) — Creates a sampler state instance.
