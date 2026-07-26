---
title: appleITTLeft
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionregion/appleittleft
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionregion/appleittleft'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionregion/appleittleft.json'
content_hash: 'sha256:64824191d1996331'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionRegion](../avcaptionregion.md)

# appleITTLeft

<sub>Type Property</sub>

The left region for iTT format captions.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class var appleITTLeft: AVCaptionRegion { get }
```

## Discussion

This region occupies the left 15% of the display area, and it uses a TBRL layout where a line progresses from top to bottom and the block extends from right to left. Lines are left justified.

## See Also

### Accessing defined regions

- [appleITTTopRegion](appleitttop.md) — The top region for iTT format captions.
- [appleITTBottomRegion](appleittbottom.md) — The bottom region for iTT format captions.
- [appleITTRightRegion](appleittright.md) — The right region for iTT format captions.
- [subRipTextBottomRegion](subriptextbottom.md) — The bottom caption region for SubRip Text (SRT) format captions.
