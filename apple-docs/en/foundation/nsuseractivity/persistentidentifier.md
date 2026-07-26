---
title: persistentIdentifier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.15+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/persistentidentifier
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/persistentidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/persistentidentifier.json'
content_hash: 'sha256:13cf8936c70cecd3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# persistentIdentifier

<sub>Instance Property</sub>

A unique and persistent value you use to identify the activity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var persistentIdentifier: NSUserActivityPersistentIdentifier? { get set }
```

## Discussion

Set this property to a value that identifies the user activity so you can later delete it with [+ deleteSavedUserActivitiesWithPersistentIdentifiers:completionHandler:](<deletesaveduseractivities(withpersistentidentifiers_completionhandler_).md>). For example, if the user checks the weather for Cupertino each morning from home, the weather app sets the persistent identifier to the city name (Cupertino). When the user deletes Cupertino from the weather app, the app deletes the user activity associated with the identifier, “Cupertino”.

```swift
let userActivity = NSUserActivity(activityType: WeatherLookup.userActivityType)
userActivity.persistentIdentifier = "Cupertino"
```

## See Also

### Describing the activity

- [activityType](activitytype.md) — The user activity object’s activity type.
- [title](title.md) — An optional, user-visible title for this activity, such as a document name or web page title.
- [keywords](keywords.md) — A set of localized keywords that can help users find the activity in search results.
- [NSUserActivityPersistentIdentifier](../nsuseractivitypersistentidentifier.md) — The type that defines a persistent identifier value for an activity.
- [contentAttributeSet](contentattributeset.md) — A set of properties that describe the activity.
