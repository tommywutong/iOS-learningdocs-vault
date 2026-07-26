---
title: UIWindowScenePushPlacement
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 2.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscenepushplacement-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscenepushplacement-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscenepushplacement-swift.struct.json'
content_hash: 'sha256:0a8136064c2182b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIWindowScenePushPlacement

<sub>Structure</sub>

A placement that indicates the system needs to present the window by pushing it onto another window.

<sub>visionOS</sub>

```swift
struct UIWindowScenePushPlacement
```

## Overview

Use this type of placement to push a new scene in place of an existing scene. The new scene appears in the same position as the original scene, hiding it. Closing the new scene makes the original scene reappear.

The following code shows how to launch a new scene in place of an original scene:

```swift
extension NSUserActivity {
    static let MyNewSceneActivityType = "com.example.my-activity-type"
}

func presentNewScene() {
    let options = UIWindowScene.ActivationRequestOptions()
    
    // Create the placement and specify which scene session you want to target.
    options.placement = UIWindowScenePushPlacement(target: originalScene.session)

    // Specify the activity type for the app delegate to launch the corresponding scene.
    let request = UISceneSessionActivationRequest(
        role: .windowApplication,
        userActivity: NSUserActivity(activityType: NSUserActivity.MyNewSceneActivityType),
        options: options
    )

    UIApplication.shared.activateSceneSession(for: request) { error in
        print(error)
    }
}
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [UIWindowScenePlacement](uiwindowsceneplacement-swift.protocol.md)

## Topics

### Creating a push placement

- [init(target:)](<uiwindowscenepushplacement-swift.struct/init(target_).md>) — Creates a push placement.

## See Also

### Positioning windows

- [placement](uiwindowscene/activationrequestoptions/placement.md) — The placement you prefer when the system activates the window scene.
- [UIWindowScenePlacement](uiwindowsceneplacement-swift.protocol.md) — The placement of a window scene in the workspace.
- [UIWindowSceneProminentPlacement](uiwindowsceneprominentplacement-swift.struct.md) — A placement that indicates the system should present the window more prominently than others in the space.
- [UIWindowSceneStandardPlacement](uiwindowscenestandardplacement-swift.struct.md) — A placement that indicates the system should present the window using the default style of the system in the space.
