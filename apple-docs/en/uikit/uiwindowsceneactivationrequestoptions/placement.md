---
title: placement
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowsceneactivationrequestoptions/placement
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowsceneactivationrequestoptions/placement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowsceneactivationrequestoptions/placement.json'
content_hash: 'sha256:361d8f265496eab3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [ActivationRequestOptions](../uiwindowscene/activationrequestoptions.md)

# placement

<sub>Instance Property</sub>

The placement you prefer when the system activates the window scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, nullable) UIWindowScenePlacement * placement;
```

## Discussion

Provide a scene placement to influence how the system positions the scene on activation. Set the value to `nil` to indicate that the system should determine the most appropriate placement.

## See Also

### Positioning windows

- [UIWindowScenePlacement](../uiwindowsceneplacement-c.class.md) — The placement of a window scene in the workspace.
- [UIWindowSceneProminentPlacement](../uiwindowsceneprominentplacement-c.class.md) — A placement that indicates the system should present the window more prominently than others in the space.
- [UIWindowSceneStandardPlacement](../uiwindowscenestandardplacement-c.class.md) — A placement that indicates the system should present the window using the default style of the system in the space.
- [UIWindowScenePushPlacement](../uiwindowscenepushplacement-c.class.md) — A placement that indicates the system needs to present the window by pushing it onto another window.
