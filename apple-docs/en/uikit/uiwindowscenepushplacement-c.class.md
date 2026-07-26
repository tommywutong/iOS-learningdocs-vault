---
title: UIWindowScenePushPlacement
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [visionOS 2.0+]
languages: [occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscenepushplacement-c.class
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscenepushplacement-c.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscenepushplacement-c.class.json'
content_hash: 'sha256:c39d9e28075ef7e0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIWindowScenePushPlacement

<sub>Class</sub>

A placement that indicates the system needs to present the window by pushing it onto another window.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UIWindowScenePushPlacement : UIWindowScenePlacement
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

- **Inherits From**: [UIWindowScenePlacement](uiwindowsceneplacement-c.class.md)

## Topics

### Replacing a scene

- [placementTargetingSceneSession:](uiwindowscenepushplacement-c.class/placementtargetingscenesession_.md) — Presents the activated scene in place of the specified scene session’s scene, placing the original scene in the background.

## See Also

### Positioning windows

- [placement](uiwindowsceneactivationrequestoptions/placement.md) — The placement you prefer when the system activates the window scene.
- [UIWindowScenePlacement](uiwindowsceneplacement-c.class.md) — The placement of a window scene in the workspace.
- [UIWindowSceneProminentPlacement](uiwindowsceneprominentplacement-c.class.md) — A placement that indicates the system should present the window more prominently than others in the space.
- [UIWindowSceneStandardPlacement](uiwindowscenestandardplacement-c.class.md) — A placement that indicates the system should present the window using the default style of the system in the space.
