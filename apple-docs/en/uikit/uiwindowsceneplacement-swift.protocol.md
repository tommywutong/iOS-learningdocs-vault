---
title: UIWindowScenePlacement
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowsceneplacement-swift.protocol
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowsceneplacement-swift.protocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowsceneplacement-swift.protocol.json'
content_hash: 'sha256:10ef56e2a21960b6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIWindowScenePlacement

<sub>Protocol</sub>

The placement of a window scene in the workspace.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol UIWindowScenePlacement : Hashable
```

## Relationships

- **Inherits From**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

- **Conforming Types**: [UIWindowSceneProminentPlacement](uiwindowsceneprominentplacement-swift.struct.md), [UIWindowScenePushPlacement](uiwindowscenepushplacement-swift.struct.md), [UIWindowSceneReplacePlacement](uiwindowscenereplaceplacement-swift.struct.md), [UIWindowSceneStandardPlacement](uiwindowscenestandardplacement-swift.struct.md)

## Topics

### Positioning windows

- [prominent()](<uiwindowsceneplacement-swift.protocol/prominent().md>) — Creates a placement that indicates the system should present the window more prominently than others in the space.
- [standard()](<uiwindowsceneplacement-swift.protocol/standard().md>) — Creates a placement that indicates the system should present the window using the default style of the system in the space.

### Type Methods

- [push(onto:)](<uiwindowsceneplacement-swift.protocol/push(onto_).md>)
- [replacing(_:)](<uiwindowsceneplacement-swift.protocol/replacing(__).md>) _(deprecated)_

## See Also

### Positioning windows

- [placement](uiwindowscene/activationrequestoptions/placement.md) — The placement you prefer when the system activates the window scene.
- [UIWindowSceneProminentPlacement](uiwindowsceneprominentplacement-swift.struct.md) — A placement that indicates the system should present the window more prominently than others in the space.
- [UIWindowSceneStandardPlacement](uiwindowscenestandardplacement-swift.struct.md) — A placement that indicates the system should present the window using the default style of the system in the space.
- [UIWindowScenePushPlacement](uiwindowscenepushplacement-swift.struct.md) — A placement that indicates the system needs to present the window by pushing it onto another window.
