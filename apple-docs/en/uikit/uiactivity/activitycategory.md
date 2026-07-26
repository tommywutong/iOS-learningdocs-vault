---
title: activityCategory
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivity/activitycategory
source_url: 'https://developer.apple.com/documentation/uikit/uiactivity/activitycategory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivity/activitycategory.json'
content_hash: 'sha256:ad11db706fad6261'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivity](../uiactivity.md)

# activityCategory

<sub>Type Property</sub>

The category of the activity, which may be used to group activities in the UI.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class var activityCategory: UIActivity.Category { get }
```

## Return Value

The assigned category of the activity. The default implementation returns [UIActivityCategoryAction](category/action.md).

## Discussion

Override this property to define a different activity category for your custom activity.

## See Also

### Getting the activity information

- [Category](category.md) — An enumeration that defines categories of activities.
- [activityType](activitytype-swift.property.md) — The type of service being provided.
- [ActivityType](activitytype-swift.struct.md) — A structure that describes the types of activities for which the system has built-in support.
- [activityTitle](activitytitle.md) — A user-readable string that describes the service.
- [activityImage](activityimage.md) — An image that identifies the service to the user.
