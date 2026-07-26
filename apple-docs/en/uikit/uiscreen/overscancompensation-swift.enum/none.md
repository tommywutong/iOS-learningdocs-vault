---
title: UIScreen.OverscanCompensation.none
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/overscancompensation-swift.enum/none
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/overscancompensation-swift.enum/none'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/overscancompensation-swift.enum/none.json'
content_hash: 'sha256:d8bb30a0b54fdebe'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIScreen](../../uiscreen.md) · [OverscanCompensation](../overscancompensation-swift.enum.md)

# UIScreen.OverscanCompensation.none

<sub>Case</sub>

No scaling occurs. Use [overscanCompensationInsets](../overscancompensationinsets.md) to get the insets required to avoid clipping.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
case none
```

## See Also

### Constants

- [UIScreenOverscanCompensationScale](scale.md) — The final composited framebuffer for the screen is scaled so that all pixels lie in the area visible on the screen.
- [UIScreenOverscanCompensationInsetBounds](insetbounds.md) — The screen bounds are reduced in size so that all pixels in the framebuffer are visible on the screen.
- [UIScreenOverscanCompensationInsetApplicationFrame](insetapplicationframe.md) — The application frame is reduced in size to compensate for overscan. Content drawn outside the application frame may be clipped. _(deprecated)_
