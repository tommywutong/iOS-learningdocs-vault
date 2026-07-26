---
title: renderSize
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.11+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasynchronousciimagefilteringrequest/rendersize
source_url: 'https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/rendersize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasynchronousciimagefilteringrequest/rendersize.json'
content_hash: 'sha256:23fc489b9b4da4f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsynchronousCIImageFilteringRequest](../avasynchronousciimagefilteringrequest.md)

# renderSize

<sub>Instance Property</sub>

The width and height, in pixels, of the frame being processed.

> [!warning] Deprecated
> Use AVCIImageFilteringParameters instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var renderSize: CGSize { get }
```

## Discussion

You can use this property if you need to work with Core Image filters that apply transforms to the image.

## See Also

### Getting contextual information for filtering

- [compositionTime](compositiontime.md) — The time in the video composition corresponding to the frame being processed. _(deprecated)_
