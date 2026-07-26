---
title: becomeCurrent()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/becomecurrent()
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/becomecurrent()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/becomecurrent%28%29.json'
content_hash: 'sha256:b75c1bccb3d7dc07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# becomeCurrent()

<sub>Instance Method</sub>

Marks the activity as currently in use by the user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func becomeCurrent()
```

## Discussion

Call this method to let the system know that the user is performing the associated activity. The system makes this object the current user activity object, which makes it available for Handoff and search indexing. If another user activity object was previously active, that object is made inactive.

Don’t call this method when providing a user activity object for a Siri request. Siri holds on to user activity objects and passes them along to your app automatically in response to specific events.

If you previously called the [- invalidate](<invalidate().md>) method on the current object, calling this method has no effect.

## See Also

### Registering and invalidating activities

- [- resignCurrent](<resigncurrent().md>) — Marks this activity object as inactive without invalidating it.
- [- invalidate](<invalidate().md>) — Invalidates an activity and marks it as no longer eligible for continuation.
- [needsSave](needssave.md) — A Boolean value that indicates whether the state of the activity needs to be updated.
- [+ deleteAllSavedUserActivitiesWithCompletionHandler:](<deleteallsaveduseractivities(completionhandler_).md>) — Deletes all user activities created by your app.
- [+ deleteSavedUserActivitiesWithPersistentIdentifiers:completionHandler:](<deletesaveduseractivities(withpersistentidentifiers_completionhandler_).md>) — Deletes user activities created by your app that have the specified persistent identifiers.
