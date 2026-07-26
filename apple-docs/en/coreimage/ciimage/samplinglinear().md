---
title: samplingLinear()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimage/samplinglinear()
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/samplinglinear()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/samplinglinear%28%29.json'
content_hash: 'sha256:4a94ff1f3bc27f6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# samplingLinear()

<sub>Instance Method</sub>

Create an image by changing the receiver’s sample mode to bilinear interpolation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func samplingLinear() -> CIImage
```

## Return Value

An autoreleased [CIImage](../ciimage.md) instance with a bilinear sampling.

## See Also

### Sampling the Image

- [- imageBySamplingNearest](<samplingnearest().md>) — Create an image by changing the receiver’s sample mode to nearest neighbor.
