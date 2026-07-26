---
title: 'canPerform(withActivityItems:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiactivity/canperform(withactivityitems:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactivity/canperform(withactivityitems:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivity/canperform%28withactivityitems%3A%29.json'
content_hash: 'sha256:2c7f7c8dc70896a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivity](../uiactivity.md)

# canPerform(withActivityItems:)

<sub>Instance Method</sub>

Queries whether the service can act on the specified data items.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func canPerform(withActivityItems activityItems: [Any]) -> Bool
```

## Parameters

- `activityItems` — An array of objects of varying types. These are the data objects on which the service would act.

## Return Value

[true](../../swift/true.md) if your service can act on the specified data items or [false](../../swift/false.md) if it cannot.

## Discussion

The default implementation of this method returns [false](../../swift/false.md). Subclasses must override it and return [true](../../swift/true.md) if the data in the `activityItems` parameter can be operated on by your service. Your implementation should check the types of the objects in the array and use that information to determine if your service can act on the corresponding data.

The [UIActivityViewController](../uiactivityviewcontroller.md) object calls this method when determining which services to show to the user.

## See Also

### Performing the activity

- [- prepareWithActivityItems:](<prepare(withactivityitems_).md>) — Prepares your service to act on the specified data.
- [activityViewController](activityviewcontroller.md) — The view controller to present to the user.
- [- performActivity](<perform().md>) — Performs the service when no custom view controller is provided.
- [- activityDidFinish:](<activitydidfinish(__).md>) — Notifies the system that your activity object has completed its work.
