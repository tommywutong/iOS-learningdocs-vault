---
title: 'scene(_:willContinueUserActivityWithType:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscenedelegate/scene(_:willcontinueuseractivitywithtype:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscenedelegate/scene(_:willcontinueuseractivitywithtype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenedelegate/scene%28_%3Awillcontinueuseractivitywithtype%3A%29.json'
content_hash: 'sha256:74bcc456fd555b3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneDelegate](../uiscenedelegate.md)

# scene(_:willContinueUserActivityWithType:)

<sub>Instance Method</sub>

Tells the delegate that it’s about to receive Handoff-related data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func scene(_ scene: UIScene, willContinueUserActivityWithType userActivityType: String)
```

## Parameters

- `scene` — The scene handling the activity.

- `userActivityType` — The type of activity to continue.

## Discussion

Use this method to prepare to handle an activity with the specified type. After this method returns, UIKit provides feedback to the user that your scene is handling the activity.

## See Also

### Continuing user activities

- [- scene:continueUserActivity:](<scene(__continue_).md>) — Tells the delegate to handle the specified Handoff-related activity.
- [- scene:didFailToContinueUserActivityWithType:error:](<scene(__didfailtocontinueuseractivitywithtype_error_).md>) — Tells the delegate that the activity couldn’t be continued.
