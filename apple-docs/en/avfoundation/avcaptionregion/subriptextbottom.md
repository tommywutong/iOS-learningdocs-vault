---
title: subRipTextBottom
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionregion/subriptextbottom
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionregion/subriptextbottom'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionregion/subriptextbottom.json'
content_hash: 'sha256:5ec6643f9688c737'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionRegion](../avcaptionregion.md)

# subRipTextBottom

<sub>Type Property</sub>

The bottom caption region for SubRip Text (SRT) format captions.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class var subRipTextBottom: AVCaptionRegion { get }
```

## Discussion

This region is suitable for SRT format, and it occupies the entire video display area. The region uses a [AVCaptionRegionWritingModeLeftToRightAndTopToBottom](writingmode-swift.enum/lefttorightandtoptobottom.md) writing mode, where a line progresses left to right and the block extends from top to bottom. The system stacks each line of text with bottom justification.

## See Also

### Accessing defined regions

- [appleITTTopRegion](appleitttop.md) — The top region for iTT format captions.
- [appleITTBottomRegion](appleittbottom.md) — The bottom region for iTT format captions.
- [appleITTLeftRegion](appleittleft.md) — The left region for iTT format captions.
- [appleITTRightRegion](appleittright.md) — The right region for iTT format captions.
