---
title: UIWindowScene.PresentationStyle.prominent
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+（17.0 起废弃）, iPadOS 15.0+（17.0 起废弃）, Mac Catalyst 15.0+（17.0 起废弃）, tvOS 15.0+（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwindowscene/presentationstyle/prominent
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/presentationstyle/prominent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/presentationstyle/prominent.json'
content_hash: 'sha256:0dbf8724210a2d86'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWindowScene](../../uiwindowscene.md) · [PresentationStyle](../presentationstyle.md)

# UIWindowScene.PresentationStyle.prominent

<sub>Case</sub>

Presents prominently above others in the current space.

> [!warning] Deprecated
> For more information, see [PresentationStyle](../presentationstyle.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case prominent
```

## Discussion

On iPad, the system displays the window scene modally, centered and elevated above the existing workspace. You should dedicate the scene to specific content within your app, like a document or file, and include buttons to close the scene.

## See Also

### Constants

- [UIWindowScenePresentationStyleAutomatic](automatic.md) — The system determines the most appropriate style. _(deprecated)_
- [UIWindowScenePresentationStyleStandard](standard.md) — The default style of the system. _(deprecated)_
