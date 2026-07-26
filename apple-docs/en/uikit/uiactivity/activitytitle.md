---
title: activityTitle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivity/activitytitle
source_url: 'https://developer.apple.com/documentation/uikit/uiactivity/activitytitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivity/activitytitle.json'
content_hash: 'sha256:e820ea1522d68a39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivity](../uiactivity.md)

# activityTitle

<sub>Instance Property</sub>

A user-readable string that describes the service.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var activityTitle: String? { get }
```

## Return Value

A string that describes the service.

## Discussion

The default value is `nil`. Subclasses must override this property to return a user-readable string that describes the service. The string you return should be localized.

## See Also

### Getting the activity information

- [activityCategory](activitycategory.md) — The category of the activity, which may be used to group activities in the UI.
- [Category](category.md) — An enumeration that defines categories of activities.
- [activityType](activitytype-swift.property.md) — The type of service being provided.
- [ActivityType](activitytype-swift.struct.md) — A structure that describes the types of activities for which the system has built-in support.
- [activityImage](activityimage.md) — An image that identifies the service to the user.
