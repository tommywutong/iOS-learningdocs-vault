---
title: 'encode(with:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptionregion/encode(with:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionregion/encode(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionregion/encode%28with%3A%29.json'
content_hash: 'sha256:be2c0c8659501271'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionRegion](../avcaptionregion.md)

# encode(with:)

<sub>Instance Method</sub>

Encodes the region using the specified encoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func encode(with encoder: NSCoder)
```

## Parameters

- `encoder` — An encoder instance to use.

## Discussion

This method throws an exception if the caption region’s [size](size.md) has different units for [width](../avcaptionsize/width.md) and [height](../avcaptionsize/height.md), or if the units are unrecognizeable.

## See Also

### Processing regions

- [- mutableCopyWithZone:](<mutablecopy(with_).md>) — Creates a mutable copy of a caption region.
- [- isEqual:](<isequal(__).md>) — Returns a Boolean value that indicates whether an object equals another.
