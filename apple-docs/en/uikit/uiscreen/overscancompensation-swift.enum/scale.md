---
title: UIScreen.OverscanCompensation.scale
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/overscancompensation-swift.enum/scale
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/overscancompensation-swift.enum/scale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/overscancompensation-swift.enum/scale.json'
content_hash: 'sha256:19e49516e878e70e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIScreen](../../uiscreen.md) · [OverscanCompensation](../overscancompensation-swift.enum.md)

# UIScreen.OverscanCompensation.scale

<sub>Case</sub>

The final composited framebuffer for the screen is scaled so that all pixels lie in the area visible on the screen.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
case scale
```

## See Also

### Constants

- [UIScreenOverscanCompensationInsetBounds](insetbounds.md) — The screen bounds are reduced in size so that all pixels in the framebuffer are visible on the screen.
- [UIScreenOverscanCompensationNone](none.md) — No scaling occurs. Use [overscanCompensationInsets](../overscancompensationinsets.md) to get the insets required to avoid clipping.
- [UIScreenOverscanCompensationInsetApplicationFrame](insetapplicationframe.md) — The application frame is reduced in size to compensate for overscan. Content drawn outside the application frame may be clipped. _(deprecated)_
