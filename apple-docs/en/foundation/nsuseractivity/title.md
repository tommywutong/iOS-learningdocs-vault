---
title: title
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/title
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/title'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/title.json'
content_hash: 'sha256:50df531dd792e9a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# title

<sub>Instance Property</sub>

An optional, user-visible title for this activity, such as a document name or web page title.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var title: String? { get set }
```

## Discussion

Always specify a title string for activity objects that are eligible for searches, and it’s recommended that you include a title string for all user activity objects. For search-related user activity objects, this string is displayed in the search results.

## See Also

### Describing the activity

- [activityType](activitytype.md) — The user activity object’s activity type.
- [keywords](keywords.md) — A set of localized keywords that can help users find the activity in search results.
- [persistentIdentifier](persistentidentifier.md) — A unique and persistent value you use to identify the activity.
- [NSUserActivityPersistentIdentifier](../nsuseractivitypersistentidentifier.md) — The type that defines a persistent identifier value for an activity.
- [contentAttributeSet](contentattributeset.md) — A set of properties that describe the activity.
