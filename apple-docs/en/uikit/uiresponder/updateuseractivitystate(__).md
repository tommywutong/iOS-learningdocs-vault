---
title: 'updateUserActivityState(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponder/updateuseractivitystate(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/updateuseractivitystate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/updateuseractivitystate%28_%3A%29.json'
content_hash: 'sha256:8e68edf1e0109b75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# updateUserActivityState(_:)

<sub>Instance Method</sub>

Updates the state of the given user activity.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func updateUserActivityState(_ activity: NSUserActivity)
```

## Parameters

- `activity` — The user activity to be updated.

## Discussion

Subclasses override this method to update the state of the given user activity. You should add state representing the user’s activity into the [NSUserActivity](../../foundation/nsuseractivity.md) object using its [addUserInfoEntries(from:)](<../../foundation/nsuseractivity/adduserinfoentries(from_).md>) method. When the state is dirty, you should set the [needsSave](../../foundation/nsuseractivity/needssave.md) property of the [NSUserActivity](../../foundation/nsuseractivity.md) to [true](../../swift/true.md), and this method will be called at an appropriate time.

When an [NSUserActivity](../../foundation/nsuseractivity.md) object managed by UIKit is updated, an empty `userInfo` dictionary is given to the [NSUserActivity](../../foundation/nsuseractivity.md) object, and all of the objects associated with the [NSUserActivity](../../foundation/nsuseractivity.md) are then sent an [- updateUserActivityState:](<updateuseractivitystate(__).md>) message.

## See Also

### Supporting user activities

- [userActivity](useractivity.md) — An object encapsulating a user activity supported by this responder.
- [- restoreUserActivityState:](<restoreuseractivitystate(__).md>) — Restores the state needed to continue the given user activity.
