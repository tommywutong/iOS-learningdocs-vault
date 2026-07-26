---
title: placement
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/activationrequestoptions/placement
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/activationrequestoptions/placement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/activationrequestoptions/placement.json'
content_hash: 'sha256:e3efe8581c496ebc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWindowScene](../../uiwindowscene.md) · [ActivationRequestOptions](../activationrequestoptions.md)

# placement

<sub>Instance Property</sub>

The placement you prefer when the system activates the window scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency var placement: (any UIWindowScenePlacement)? { get set }
```

## Discussion

Provide a scene placement to influence how the system positions the scene on activation. Set the value to `nil` to indicate that the system should determine the most appropriate placement.

## See Also

### Positioning windows

- [UIWindowScenePlacement](../../uiwindowsceneplacement-swift.protocol.md) — The placement of a window scene in the workspace.
- [UIWindowSceneProminentPlacement](../../uiwindowsceneprominentplacement-swift.struct.md) — A placement that indicates the system should present the window more prominently than others in the space.
- [UIWindowSceneStandardPlacement](../../uiwindowscenestandardplacement-swift.struct.md) — A placement that indicates the system should present the window using the default style of the system in the space.
- [UIWindowScenePushPlacement](../../uiwindowscenepushplacement-swift.struct.md) — A placement that indicates the system needs to present the window by pushing it onto another window.
