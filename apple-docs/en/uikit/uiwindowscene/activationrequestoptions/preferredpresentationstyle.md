---
title: preferredPresentationStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+（17.0 起废弃）, iPadOS 15.0+（17.0 起废弃）, Mac Catalyst 15.0+（17.0 起废弃）, tvOS 15.0+（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwindowscene/activationrequestoptions/preferredpresentationstyle
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/activationrequestoptions/preferredpresentationstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/activationrequestoptions/preferredpresentationstyle.json'
content_hash: 'sha256:8f7f01700e385817'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWindowScene](../../uiwindowscene.md) · [ActivationRequestOptions](../activationrequestoptions.md)

# preferredPresentationStyle

<sub>Instance Property</sub>

The presentation style of the window scene.

> [!warning] Deprecated
> Use [placement](placement.md) (Swift) or [placement](../../uiwindowsceneactivationrequestoptions/placement.md) (Objective-C) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var preferredPresentationStyle: UIWindowScene.PresentationStyle { get set }
```

## Discussion

The presentation style determines how the system displays the new window scene relative to other scenes in the workspace. The default style is [UIWindowScenePresentationStyleAutomatic](../presentationstyle/automatic.md).

## See Also

### Deprecated

- [UIWindowSceneReplacePlacement](../../uiwindowscenereplaceplacement-swift.struct.md) _(deprecated)_
