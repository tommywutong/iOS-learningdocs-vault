---
title: insetApplicationFrame
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+（9.0 起废弃）, iPadOS 5.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiscreen/overscancompensation-swift.enum/insetapplicationframe
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/overscancompensation-swift.enum/insetapplicationframe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/overscancompensation-swift.enum/insetapplicationframe.json'
content_hash: 'sha256:7076c640482c5d72'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIScreen](../../uiscreen.md) · [OverscanCompensation](../overscancompensation-swift.enum.md)

# insetApplicationFrame

<sub>Type Property</sub>

The application frame is reduced in size to compensate for overscan. Content drawn outside the application frame may be clipped.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
static var insetApplicationFrame: UIScreen.OverscanCompensation { get }
```

## See Also

### Constants

- [UIScreenOverscanCompensationScale](scale.md) — The final composited framebuffer for the screen is scaled so that all pixels lie in the area visible on the screen.
- [UIScreenOverscanCompensationInsetBounds](insetbounds.md) — The screen bounds are reduced in size so that all pixels in the framebuffer are visible on the screen.
- [UIScreenOverscanCompensationNone](none.md) — No scaling occurs. Use [overscanCompensationInsets](../overscancompensationinsets.md) to get the insets required to avoid clipping.
