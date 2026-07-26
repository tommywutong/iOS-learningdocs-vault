---
title: keywords
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/keywords
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/keywords'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/keywords.json'
content_hash: 'sha256:ce3a089263c29fe1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# keywords

<sub>Instance Property</sub>

A set of localized keywords that can help users find the activity in search results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var keywords: Set<String> { get set }
```

## Discussion

The default value of this property is `nil`. The system indexes the keywords you provide.

## See Also

### Describing the activity

- [activityType](activitytype.md) — The user activity object’s activity type.
- [title](title.md) — An optional, user-visible title for this activity, such as a document name or web page title.
- [persistentIdentifier](persistentidentifier.md) — A unique and persistent value you use to identify the activity.
- [NSUserActivityPersistentIdentifier](../nsuseractivitypersistentidentifier.md) — The type that defines a persistent identifier value for an activity.
- [contentAttributeSet](contentattributeset.md) — A set of properties that describe the activity.
