---
title: activityType
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/activitytype
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/activitytype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/activitytype.json'
content_hash: 'sha256:b7e5b63a9c302ce6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# activityType

<sub>Instance Property</sub>

The user activity object’s activity type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var activityType: String { get }
```

## Discussion

This property is set at initialization time and can’t be changed later. Typically, you specify activity type strings using a reverse-DNS format that uniquely identifies the activity.

## See Also

### Describing the activity

- [title](title.md) — An optional, user-visible title for this activity, such as a document name or web page title.
- [keywords](keywords.md) — A set of localized keywords that can help users find the activity in search results.
- [persistentIdentifier](persistentidentifier.md) — A unique and persistent value you use to identify the activity.
- [NSUserActivityPersistentIdentifier](../nsuseractivitypersistentidentifier.md) — The type that defines a persistent identifier value for an activity.
- [contentAttributeSet](contentattributeset.md) — A set of properties that describe the activity.
