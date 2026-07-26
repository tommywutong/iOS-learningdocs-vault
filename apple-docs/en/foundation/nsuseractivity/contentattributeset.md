---
title: contentAttributeSet
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/contentattributeset
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/contentattributeset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/contentattributeset.json'
content_hash: 'sha256:0da156ba4d1e6583'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# contentAttributeSet

<sub>Instance Property</sub>

A set of properties that describe the activity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@NSCopying var contentAttributeSet: CSSearchableItemAttributeSet? { get set }
```

## Discussion

A [CSSearchableItemAttributeSet](../../corespotlight/cssearchableitemattributeset.md) object encapsulates the set of properties you want to display for a searchable activity.

## See Also

### Describing the activity

- [activityType](activitytype.md) — The user activity object’s activity type.
- [title](title.md) — An optional, user-visible title for this activity, such as a document name or web page title.
- [keywords](keywords.md) — A set of localized keywords that can help users find the activity in search results.
- [persistentIdentifier](persistentidentifier.md) — A unique and persistent value you use to identify the activity.
- [NSUserActivityPersistentIdentifier](../nsuseractivitypersistentidentifier.md) — The type that defines a persistent identifier value for an activity.
