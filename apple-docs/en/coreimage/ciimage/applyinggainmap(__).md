---
title: 'applyingGainMap(_:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/applyinggainmap(_:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/applyinggainmap(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/applyinggainmap%28_%3A%29.json'
content_hash: 'sha256:3682d294eb887a7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# applyingGainMap(_:)

<sub>Instance Method</sub>

Create an image that applies a gain map Core Image image to the received Core Image image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func applyingGainMap(_ gainmap: CIImage) -> CIImage
```

## Return Value

An autoreleased [CIImage](../ciimage.md) instance or the received image.

## Discussion

The gain map image can be obtained by creating a [CIImage](../ciimage.md) instance from `NSURL`/`NSData` and setting the [kCIImageAuxiliaryHDRGainMap](../ciimageoption/auxiliaryhdrgainmap.md) option set to `@YES`.

If the gain map [CIImage](../ciimage.md) instance doesn’t have the needed [properties](properties.md) metadata, the received image will be returned as-is.

## See Also

### Instance Methods

- [- imageByApplyingGainMap:headroom:](<applyinggainmap(__headroom_).md>) — Create an image that applies a gain map Core Image image with a specified headroom to the received Core Image image.
