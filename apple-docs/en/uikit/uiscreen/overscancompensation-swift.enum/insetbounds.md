---
title: UIScreen.OverscanCompensation.insetBounds
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/overscancompensation-swift.enum/insetbounds
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/overscancompensation-swift.enum/insetbounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/overscancompensation-swift.enum/insetbounds.json'
content_hash: 'sha256:90e0c8fdcf5dc9a2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIScreen](../../uiscreen.md) · [OverscanCompensation](../overscancompensation-swift.enum.md)

# UIScreen.OverscanCompensation.insetBounds

<sub>Case</sub>

The screen bounds are reduced in size so that all pixels in the framebuffer are visible on the screen.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
case insetBounds
```

## See Also

### Constants

- [UIScreenOverscanCompensationScale](scale.md) — The final composited framebuffer for the screen is scaled so that all pixels lie in the area visible on the screen.
- [UIScreenOverscanCompensationNone](none.md) — No scaling occurs. Use [overscanCompensationInsets](../overscancompensationinsets.md) to get the insets required to avoid clipping.
- [UIScreenOverscanCompensationInsetApplicationFrame](insetapplicationframe.md) — The application frame is reduced in size to compensate for overscan. Content drawn outside the application frame may be clipped. _(deprecated)_
