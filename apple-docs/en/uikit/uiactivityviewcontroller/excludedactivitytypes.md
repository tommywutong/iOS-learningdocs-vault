---
title: excludedActivityTypes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityviewcontroller/excludedactivitytypes
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/excludedactivitytypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityviewcontroller/excludedactivitytypes.json'
content_hash: 'sha256:a1105991ee6906b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityViewController](../uiactivityviewcontroller.md)

# excludedActivityTypes

<sub>Instance Property</sub>

The list of services that should not be displayed.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var excludedActivityTypes: [UIActivity.ActivityType]? { get set }
```

## Discussion

This property contains an array of strings, each of which corresponds to the value you would find in the [activityType](../uiactivity/activitytype-swift.property.md) parameter of a [UIActivity](../uiactivity.md) object. Each string you specify indicates a service that you do not want displayed to the user. You might exclude services that you feel are not suitable for the content you are providing. For example, you might not want to allow the user to print a specific image. If the value of this property is `nil`, no services are excluded.

This value of this property is `nil` by default.
