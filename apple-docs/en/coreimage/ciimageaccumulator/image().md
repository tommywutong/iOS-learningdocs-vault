---
title: image()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageaccumulator/image()
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageaccumulator/image()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageaccumulator/image%28%29.json'
content_hash: 'sha256:d6893422d2eab132'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageAccumulator](../ciimageaccumulator.md)

# image()

<sub>Instance Method</sub>

Returns the current contents of the image accumulator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func image() -> CIImage
```

## Return Value

The  image object that represents the current contents of the image accumulator.

## See Also

### Obtaining Data From an Image Accumulator

- [extent](extent.md) — The extent of the image associated with the image accumulator.
- [format](format.md) — The pixel format of the image accumulator.
