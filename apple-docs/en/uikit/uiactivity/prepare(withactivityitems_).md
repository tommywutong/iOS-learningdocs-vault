---
title: 'prepare(withActivityItems:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiactivity/prepare(withactivityitems:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactivity/prepare(withactivityitems:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivity/prepare%28withactivityitems%3A%29.json'
content_hash: 'sha256:0aea8418579d7006'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivity](../uiactivity.md)

# prepare(withActivityItems:)

<sub>Instance Method</sub>

Prepares your service to act on the specified data.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func prepare(withActivityItems activityItems: [Any])
```

## Parameters

- `activityItems` — An array of objects of varying types. These are the data objects on which to act.

## Discussion

The default implementation of this method does nothing. This method is called after the user has selected your service but before your service is asked to perform its action. Subclasses should override this method and use it to store a reference to the data items in the `activityItems` parameter. In addition, if the implementation of your service requires displaying additional UI to the user, you can use this method to prepare your view controller object and make it available from the [activityViewController](activityviewcontroller.md) method.

## See Also

### Performing the activity

- [- canPerformWithActivityItems:](<canperform(withactivityitems_).md>) — Queries whether the service can act on the specified data items.
- [activityViewController](activityviewcontroller.md) — The view controller to present to the user.
- [- performActivity](<perform().md>) — Performs the service when no custom view controller is provided.
- [- activityDidFinish:](<activitydidfinish(__).md>) — Notifies the system that your activity object has completed its work.
