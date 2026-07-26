---
title: invalidate()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/invalidate()
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/invalidate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/invalidate%28%29.json'
content_hash: 'sha256:70b67a9e2290904c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# invalidate()

<sub>Instance Method</sub>

Invalidates an activity and marks it as no longer eligible for continuation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func invalidate()
```

## Discussion

Call this method when the user stops engaging in the associated activity and that activity is no longer available. For example, you might call this method when the user closes the window associated with the activity. After calling this method on a user activity object, calling the [- becomeCurrent](<becomecurrent().md>) method on that object has no effect.

## See Also

### Registering and invalidating activities

- [- becomeCurrent](<becomecurrent().md>) — Marks the activity as currently in use by the user.
- [- resignCurrent](<resigncurrent().md>) — Marks this activity object as inactive without invalidating it.
- [needsSave](needssave.md) — A Boolean value that indicates whether the state of the activity needs to be updated.
- [+ deleteAllSavedUserActivitiesWithCompletionHandler:](<deleteallsaveduseractivities(completionhandler_).md>) — Deletes all user activities created by your app.
- [+ deleteSavedUserActivitiesWithPersistentIdentifiers:completionHandler:](<deletesaveduseractivities(withpersistentidentifiers_completionhandler_).md>) — Deletes user activities created by your app that have the specified persistent identifiers.
