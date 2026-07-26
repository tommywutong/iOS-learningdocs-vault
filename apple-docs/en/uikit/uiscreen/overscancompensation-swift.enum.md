---
title: UIScreen.OverscanCompensation
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/overscancompensation-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/overscancompensation-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/overscancompensation-swift.enum.json'
content_hash: 'sha256:fed50c26172feef2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# UIScreen.OverscanCompensation

<sub>Enumeration</sub>

Describes different techniques for compensating for pixel loss at the edge of the screen.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
enum OverscanCompensation
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIScreenOverscanCompensationScale](overscancompensation-swift.enum/scale.md) — The final composited framebuffer for the screen is scaled so that all pixels lie in the area visible on the screen.
- [UIScreenOverscanCompensationInsetBounds](overscancompensation-swift.enum/insetbounds.md) — The screen bounds are reduced in size so that all pixels in the framebuffer are visible on the screen.
- [UIScreenOverscanCompensationNone](overscancompensation-swift.enum/none.md) — No scaling occurs. Use [overscanCompensationInsets](overscancompensationinsets.md) to get the insets required to avoid clipping.
- [UIScreenOverscanCompensationInsetApplicationFrame](overscancompensation-swift.enum/insetapplicationframe.md) — The application frame is reduced in size to compensate for overscan. Content drawn outside the application frame may be clipped. _(deprecated)_

### Initializers

- [init(rawValue:)](<overscancompensation-swift.enum/init(rawvalue_).md>)

## See Also

### Managing overscan compensation

- [overscanCompensationInsets](overscancompensationinsets.md) — The edge inset values needed to avoid clipping the rectangle.
- [overscanCompensation](overscancompensation-swift.property.md) — For an external screen, this property sets the desired technique to compensate for overscan.
