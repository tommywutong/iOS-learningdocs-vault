---
title: UIInterfaceOrientation.portraitUpsideDown
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiinterfaceorientation/portraitupsidedown
source_url: 'https://developer.apple.com/documentation/uikit/uiinterfaceorientation/portraitupsidedown'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinterfaceorientation/portraitupsidedown.json'
content_hash: 'sha256:9285ce6dd807b472'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIInterfaceOrientation](../uiinterfaceorientation.md)

# UIInterfaceOrientation.portraitUpsideDown

<sub>Case</sub>

The device is in portrait mode but is upside down, with the device upright and the Home button at the top.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case portraitUpsideDown
```

## Discussion

[UIViewController](../uiviewcontroller.md) doesn’t support this case on devices without a Home button.

## See Also

### Orientations

- [UIInterfaceOrientationUnknown](unknown.md) — The orientation of the device is unknown.
- [UIInterfaceOrientationPortrait](portrait.md) — The device is in portrait mode, with the device upright and the Home button on the bottom.
- [UIInterfaceOrientationLandscapeLeft](landscapeleft.md) — The device is in landscape mode, with the device upright and the Home button on the left.
- [UIInterfaceOrientationLandscapeRight](landscaperight.md) — The device is in landscape mode, with the device upright and the Home button on the right.
