---
title: 'applyingGainMap(_:headroom:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/applyinggainmap(_:headroom:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/applyinggainmap(_:headroom:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/applyinggainmap%28_%3Aheadroom%3A%29.json'
content_hash: 'sha256:43f815affb99311d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# applyingGainMap(_:headroom:)

<sub>Instance Method</sub>

Create an image that applies a gain map Core Image image with a specified headroom to the received Core Image image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func applyingGainMap(_ gainmap: CIImage, headroom: Float) -> CIImage
```

## Parameters

- `gainmap` — The gain map [CIImage](../ciimage.md) instance to apply to the receiver.

- `headroom` — A float value that specify how much headroom the resulting image should have. The headroom value will be limited to between 1.0 (i.e. SDR) and the full headroom allowed by the gain map.

## Return Value

An autoreleased [CIImage](../ciimage.md) instance or the received image.

## See Also

### Instance Methods

- [- imageByApplyingGainMap:](<applyinggainmap(__).md>) — Create an image that applies a gain map Core Image image to the received Core Image image.
