---
title: resignCurrent()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/resigncurrent()
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/resigncurrent()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/resigncurrent%28%29.json'
content_hash: 'sha256:54fa163c20d949cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# resignCurrent()

<sub>Instance Method</sub>

Marks this activity object as inactive without invalidating it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resignCurrent()
```

## Discussion

Calling this method marks the user activity as no longer current, but doesn’t invalidate it entirely. You can call this method when you want to stop advertising the activity for continuation and search indexing only temporarily. You may call [- becomeCurrent](<becomecurrent().md>) later to restore this object as the current activity.

## See Also

### Registering and invalidating activities

- [- becomeCurrent](<becomecurrent().md>) — Marks the activity as currently in use by the user.
- [- invalidate](<invalidate().md>) — Invalidates an activity and marks it as no longer eligible for continuation.
- [needsSave](needssave.md) — A Boolean value that indicates whether the state of the activity needs to be updated.
- [+ deleteAllSavedUserActivitiesWithCompletionHandler:](<deleteallsaveduseractivities(completionhandler_).md>) — Deletes all user activities created by your app.
- [+ deleteSavedUserActivitiesWithPersistentIdentifiers:completionHandler:](<deletesaveduseractivities(withpersistentidentifiers_completionhandler_).md>) — Deletes user activities created by your app that have the specified persistent identifiers.
