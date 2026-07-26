---
title: 'scene(_:continue:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscenedelegate/scene(_:continue:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscenedelegate/scene(_:continue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenedelegate/scene%28_%3Acontinue%3A%29.json'
content_hash: 'sha256:d9ff0710c2de8548'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneDelegate](../uiscenedelegate.md)

# scene(_:continue:)

<sub>Instance Method</sub>

Tells the delegate to handle the specified Handoff-related activity.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func scene(_ scene: UIScene, continue userActivity: NSUserActivity)
```

## Parameters

- `scene` — The scene handling the activity.

- `userActivity` — The object containing the activity-related data. Use the information in this object to continue the user’s activity in your scene.

## Discussion

Use this method to update the specified scene with the data from the provided activity object. UIKit calls this method on your app’s main thread only after it receives all of the data for an activity object, which might originate from a different device.

## See Also

### Continuing user activities

- [- scene:willContinueUserActivityWithType:](<scene(__willcontinueuseractivitywithtype_).md>) — Tells the delegate that it’s about to receive Handoff-related data.
- [- scene:didFailToContinueUserActivityWithType:error:](<scene(__didfailtocontinueuseractivitywithtype_error_).md>) — Tells the delegate that the activity couldn’t be continued.
