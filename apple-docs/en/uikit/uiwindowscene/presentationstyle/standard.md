---
title: UIWindowScene.PresentationStyle.standard
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+（17.0 起废弃）, iPadOS 15.0+（17.0 起废弃）, Mac Catalyst 15.0+（17.0 起废弃）, tvOS 15.0+（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwindowscene/presentationstyle/standard
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/presentationstyle/standard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/presentationstyle/standard.json'
content_hash: 'sha256:08dc06515ebbbaea'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWindowScene](../../uiwindowscene.md) · [PresentationStyle](../presentationstyle.md)

# UIWindowScene.PresentationStyle.standard

<sub>Case</sub>

The default style of the system.

> [!warning] Deprecated
> For more information, see [PresentationStyle](../presentationstyle.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case standard
```

## Discussion

On iPad, the system displays the window scene in Split View, side-by-side with the scene that originated the request for the new scene.

## See Also

### Constants

- [UIWindowScenePresentationStyleAutomatic](automatic.md) — The system determines the most appropriate style. _(deprecated)_
- [UIWindowScenePresentationStyleProminent](prominent.md) — Presents prominently above others in the current space. _(deprecated)_
