---
title: appleITTTop
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionregion/appleitttop
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionregion/appleitttop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionregion/appleitttop.json'
content_hash: 'sha256:8b6ec845b838eb7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionRegion](../avcaptionregion.md)

# appleITTTop

<sub>Type Property</sub>

The top region for iTT format captions.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class var appleITTTop: AVCaptionRegion { get }
```

## Discussion

This region is available when working with iTT captions. It occupies the top 15% of the display area, and it uses a LRTB layout where a line progresses from left to right and the block extends from top to bottom. Lines are top justified.

## See Also

### Accessing defined regions

- [appleITTBottomRegion](appleittbottom.md) — The bottom region for iTT format captions.
- [appleITTLeftRegion](appleittleft.md) — The left region for iTT format captions.
- [appleITTRightRegion](appleittright.md) — The right region for iTT format captions.
- [subRipTextBottomRegion](subriptextbottom.md) — The bottom caption region for SubRip Text (SRT) format captions.
