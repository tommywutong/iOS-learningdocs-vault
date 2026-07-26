---
title: 'restoreUserActivityState(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponder/restoreuseractivitystate(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/restoreuseractivitystate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/restoreuseractivitystate%28_%3A%29.json'
content_hash: 'sha256:107a9f383dcbe557'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# restoreUserActivityState(_:)

<sub>Instance Method</sub>

Restores the state needed to continue the given user activity.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func restoreUserActivityState(_ activity: NSUserActivity)
```

## Parameters

- `activity` — The user activity to be continued.

## Discussion

Subclasses override this method to restore the responder’s state with the given user activity. The system calls it on any objects passed to the restoration handler given to [- application:continueUserActivity:restorationHandler:](<../uiapplicationdelegate/application(__continue_restorationhandler_).md>). The override should use the state data contained in the given user activity’s `userInfo` dictionary to restore the object.

You may also call this method directly if the app delegate chooses not to use the restoration handler.

## See Also

### Supporting user activities

- [userActivity](useractivity.md) — An object encapsulating a user activity supported by this responder.
- [- updateUserActivityState:](<updateuseractivitystate(__).md>) — Updates the state of the given user activity.
