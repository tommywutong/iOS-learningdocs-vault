---
title: 'deleteSavedUserActivities(withPersistentIdentifiers:completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsuseractivity/deletesaveduseractivities(withpersistentidentifiers:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/deletesaveduseractivities(withpersistentidentifiers:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/deletesaveduseractivities%28withpersistentidentifiers%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:e9eb430c51c71221'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# deleteSavedUserActivities(withPersistentIdentifiers:completionHandler:)

<sub>Type Method</sub>

Deletes user activities created by your app that have the specified persistent identifiers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
class func deleteSavedUserActivities(withPersistentIdentifiers persistentIdentifiers: [NSUserActivityPersistentIdentifier], completionHandler handler: @escaping @Sendable () -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
class func deleteSavedUserActivities(withPersistentIdentifiers persistentIdentifiers: [NSUserActivityPersistentIdentifier]) async
```

## Parameters

- `persistentIdentifiers` — The list of persistent identifiers that the system uses to determine which user activities to delete.

- `handler` — The block that the system invokes after deleting the user activities. Wait for the system to call this block to ensure that the system deletes the activities (or marks them for deletion).

## Discussion

Deletes user activities with a persistent identifier matching any identifier in the `persistentIdentifiers` array.

## See Also

### Registering and invalidating activities

- [- becomeCurrent](<becomecurrent().md>) — Marks the activity as currently in use by the user.
- [- resignCurrent](<resigncurrent().md>) — Marks this activity object as inactive without invalidating it.
- [- invalidate](<invalidate().md>) — Invalidates an activity and marks it as no longer eligible for continuation.
- [needsSave](needssave.md) — A Boolean value that indicates whether the state of the activity needs to be updated.
- [+ deleteAllSavedUserActivitiesWithCompletionHandler:](<deleteallsaveduseractivities(completionhandler_).md>) — Deletes all user activities created by your app.
