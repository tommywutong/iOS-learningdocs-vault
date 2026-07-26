---
title: NSUserActivityPersistentIdentifier
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivitypersistentidentifier
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivitypersistentidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivitypersistentidentifier.json'
content_hash: 'sha256:41f76a38ba65544b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUserActivityPersistentIdentifier

<sub>Type Alias</sub>

The type that defines a persistent identifier value for an activity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias NSUserActivityPersistentIdentifier = String
```

## Discussion

In Objective-C, [NSUserActivity](nsuseractivity.md) persistent identifiers are a type alias of [NSString](nsstring.md). In Swift, [NSUserActivity](nsuseractivity.md) persistent identifiers use the [NSUserActivityPersistentIdentifier](nsuseractivitypersistentidentifier.md) structure.

## See Also

### Describing the activity

- [activityType](nsuseractivity/activitytype.md) — The user activity object’s activity type.
- [title](nsuseractivity/title.md) — An optional, user-visible title for this activity, such as a document name or web page title.
- [keywords](nsuseractivity/keywords.md) — A set of localized keywords that can help users find the activity in search results.
- [persistentIdentifier](nsuseractivity/persistentidentifier.md) — A unique and persistent value you use to identify the activity.
- [contentAttributeSet](nsuseractivity/contentattributeset.md) — A set of properties that describe the activity.
