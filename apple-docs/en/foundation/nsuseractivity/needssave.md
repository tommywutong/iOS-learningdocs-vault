---
title: needsSave
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/needssave
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/needssave'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/needssave.json'
content_hash: 'sha256:94cdc28d4241689a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# needsSave

<sub>Instance Property</sub>

A Boolean value that indicates whether the state of the activity needs to be updated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var needsSave: Bool { get set }
```

## Discussion

If [true](../../swift/true.md), the delegate for this user activity receives a [- userActivityWillSave:](<../nsuseractivitydelegate/useractivitywillsave(__).md>) callback before the activity is sent for continuation on another device.

## See Also

### Registering and invalidating activities

- [- becomeCurrent](<becomecurrent().md>) — Marks the activity as currently in use by the user.
- [- resignCurrent](<resigncurrent().md>) — Marks this activity object as inactive without invalidating it.
- [- invalidate](<invalidate().md>) — Invalidates an activity and marks it as no longer eligible for continuation.
- [+ deleteAllSavedUserActivitiesWithCompletionHandler:](<deleteallsaveduseractivities(completionhandler_).md>) — Deletes all user activities created by your app.
- [+ deleteSavedUserActivitiesWithPersistentIdentifiers:completionHandler:](<deletesaveduseractivities(withpersistentidentifiers_completionhandler_).md>) — Deletes user activities created by your app that have the specified persistent identifiers.
