---
title: userActivity
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder/useractivity
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/useractivity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/useractivity.json'
content_hash: 'sha256:866842242e4681c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# userActivity

<sub>Instance Property</sub>

An object encapsulating a user activity supported by this responder.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var userActivity: NSUserActivity? { get set }
```

## Discussion

By setting the [userActivity](useractivity.md) property on a responder, the [NSUserActivity](../../foundation/nsuseractivity.md) object becomes managed by UIKit. User activities managed by UIKit are saved automatically at appropriate times. You can lazily add state data representing the user’s activity using the [- updateUserActivityState:](<updateuseractivitystate(__).md>) override. Multiple responders can share a single [NSUserActivity](../../foundation/nsuseractivity.md) instance, in which case they all get an [- updateUserActivityState:](<updateuseractivitystate(__).md>) callback.

> [!note] Note
> Prior to invoking [- updateUserActivityState:](<updateuseractivitystate(__).md>) on all of the associated objects, the `userInfo` dictionary for the [NSUserActivity](../../foundation/nsuseractivity.md) object is cleared.

A responder object can set its [userActivity](useractivity.md) property to `nil` if it no longer wants to participate. Any [NSUserActivity](../../foundation/nsuseractivity.md) objects that are managed by UIKit but which have no associated responders (or documents) are automatically invalidated.

## See Also

### Supporting user activities

- [- restoreUserActivityState:](<restoreuseractivitystate(__).md>) — Restores the state needed to continue the given user activity.
- [- updateUserActivityState:](<updateuseractivitystate(__).md>) — Updates the state of the given user activity.
