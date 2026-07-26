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
doc_path: /documentation/uikit/uiactivityitemprovider/activitytype
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemprovider/activitytype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemprovider/activitytype.json'
content_hash: 'sha256:c8db6068fe4167b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityItemProvider](../uiactivityitemprovider.md)

# activityType

<sub>Instance Property</sub>

The type of the activity object that is expecting the data.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var activityType: UIActivity.ActivityType? { get }
```

## Discussion

The value of this property is `nil` until the user selects an activity. At that time, the value is set and the provider object is submitted to a queue for execution. Thus, you should access this value only after your object’s [item](item.md) method is called.

## See Also

### Accessing the provider attributes

- [item](item.md) — Generates and returns the actual data-bearing object.
- [placeholderItem](placeholderitem.md) — The placeholder object you specified at initialization time.
