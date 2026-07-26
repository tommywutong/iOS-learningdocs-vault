---
title: 'scene(_:didFailToContinueUserActivityWithType:error:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscenedelegate/scene(_:didfailtocontinueuseractivitywithtype:error:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscenedelegate/scene(_:didfailtocontinueuseractivitywithtype:error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenedelegate/scene%28_%3Adidfailtocontinueuseractivitywithtype%3Aerror%3A%29.json'
content_hash: 'sha256:5d9a20391adb2c38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneDelegate](../uiscenedelegate.md)

# scene(_:didFailToContinueUserActivityWithType:error:)

<sub>Instance Method</sub>

Tells the delegate that the activity couldn’t be continued.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func scene(_ scene: UIScene, didFailToContinueUserActivityWithType userActivityType: String, error: any Error)
```

## Parameters

- `scene` — The scene handling the activity.

- `userActivityType` — The type of the activity that failed.

- `error` — An error object indicating the reason for the failure.

## Discussion

Use this method to let the user know that the specified activity couldn’t be completed. If you don’t implement this method, UIKit displays an error to the user with an appropriate message about the reason for the failure.

## See Also

### Continuing user activities

- [- scene:willContinueUserActivityWithType:](<scene(__willcontinueuseractivitywithtype_).md>) — Tells the delegate that it’s about to receive Handoff-related data.
- [- scene:continueUserActivity:](<scene(__continue_).md>) — Tells the delegate to handle the specified Handoff-related activity.
