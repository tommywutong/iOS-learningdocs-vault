---
title: activityType
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivity/activitytype-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiactivity/activitytype-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivity/activitytype-swift.property.json'
content_hash: 'sha256:8a96656bd6b8a7d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivity](../uiactivity.md)

# activityType

<sub>Instance Property</sub>

The type of service being provided.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var activityType: UIActivity.ActivityType? { get }
```

## Discussion

The default value is `nil`. Subclasses may override this property to return a custom activity type that’s reported to the [completionWithItemsHandler](../uiactivityviewcontroller/completionwithitemshandler-swift.property.md) completion handler.

## See Also

### Getting the activity information

- [activityCategory](activitycategory.md) — The category of the activity, which may be used to group activities in the UI.
- [Category](category.md) — An enumeration that defines categories of activities.
- [ActivityType](activitytype-swift.struct.md) — A structure that describes the types of activities for which the system has built-in support.
- [activityTitle](activitytitle.md) — A user-readable string that describes the service.
- [activityImage](activityimage.md) — An image that identifies the service to the user.
