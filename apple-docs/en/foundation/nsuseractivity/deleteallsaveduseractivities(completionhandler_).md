---
title: 'deleteAllSavedUserActivities(completionHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsuseractivity/deleteallsaveduseractivities(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/deleteallsaveduseractivities(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/deleteallsaveduseractivities%28completionhandler%3A%29.json'
content_hash: 'sha256:9dc7e3aa8c468549'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# deleteAllSavedUserActivities(completionHandler:)

<sub>Type Method</sub>

Deletes all user activities created by your app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
class func deleteAllSavedUserActivities(completionHandler handler: @escaping @Sendable () -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
class func deleteAllSavedUserActivities() async
```

## Parameters

- `handler` — The block that the system invokes after deleting the user activities. Wait for the system to call this block to ensure that the system deletes the activities (or marks them for deletion).

## Discussion

Deletes all user activities stored by Core Spotlight or donated as Siri shortcuts.

## See Also

### Registering and invalidating activities

- [- becomeCurrent](<becomecurrent().md>) — Marks the activity as currently in use by the user.
- [- resignCurrent](<resigncurrent().md>) — Marks this activity object as inactive without invalidating it.
- [- invalidate](<invalidate().md>) — Invalidates an activity and marks it as no longer eligible for continuation.
- [needsSave](needssave.md) — A Boolean value that indicates whether the state of the activity needs to be updated.
- [+ deleteSavedUserActivitiesWithPersistentIdentifiers:completionHandler:](<deletesaveduseractivities(withpersistentidentifiers_completionhandler_).md>) — Deletes user activities created by your app that have the specified persistent identifiers.
