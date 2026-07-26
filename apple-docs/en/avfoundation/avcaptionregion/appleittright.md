---
title: appleITTRight
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionregion/appleittright
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionregion/appleittright'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionregion/appleittright.json'
content_hash: 'sha256:9fd790bb7b7d6996'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionRegion](../avcaptionregion.md)

# appleITTRight

<sub>Type Property</sub>

The right region for iTT format captions.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class var appleITTRight: AVCaptionRegion { get }
```

## Discussion

This region occupies the right 15% of the display area, and it uses a TBRL layout where a line progresses from top to bottom and the block extends from right to left. Lines are right justified.

## See Also

### Accessing defined regions

- [appleITTTopRegion](appleitttop.md) — The top region for iTT format captions.
- [appleITTBottomRegion](appleittbottom.md) — The bottom region for iTT format captions.
- [appleITTLeftRegion](appleittleft.md) — The left region for iTT format captions.
- [subRipTextBottomRegion](subriptextbottom.md) — The bottom caption region for SubRip Text (SRT) format captions.
