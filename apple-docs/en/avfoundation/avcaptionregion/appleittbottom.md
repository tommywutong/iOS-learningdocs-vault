---
title: appleITTBottom
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionregion/appleittbottom
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionregion/appleittbottom'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionregion/appleittbottom.json'
content_hash: 'sha256:725b2f07ebd1b2e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionRegion](../avcaptionregion.md)

# appleITTBottom

<sub>Type Property</sub>

The bottom region for iTT format captions.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class var appleITTBottom: AVCaptionRegion { get }
```

## Discussion

This region occupies the bottom 15% of the display area, and it uses a LRTB layout where a line progresses from left to right and the block extends from top to bottom. Lines are bottom justified.

## See Also

### Accessing defined regions

- [appleITTTopRegion](appleitttop.md) — The top region for iTT format captions.
- [appleITTLeftRegion](appleittleft.md) — The left region for iTT format captions.
- [appleITTRightRegion](appleittright.md) — The right region for iTT format captions.
- [subRipTextBottomRegion](subriptextbottom.md) — The bottom caption region for SubRip Text (SRT) format captions.
