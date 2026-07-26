---
title: 'activityDidFinish(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiactivity/activitydidfinish(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactivity/activitydidfinish(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivity/activitydidfinish%28_%3A%29.json'
content_hash: 'sha256:001df582bbd89a9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivity](../uiactivity.md)

# activityDidFinish(_:)

<sub>Instance Method</sub>

Notifies the system that your activity object has completed its work.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func activityDidFinish(_ completed: Bool)
```

## Parameters

- `completed` — Specify [true](../../swift/true.md) if the service executed to completion or [false](../../swift/false.md) if the service was canceled or didn’t finish because of an error.

## Discussion

This method dismisses the sharing interface provided by the [UIActivityViewController](../uiactivityviewcontroller.md) object. If you provided a view controller using the [activityViewController](activityviewcontroller.md) method, this method dismisses that view controller too.

You must call this method after completing the work associated with this object’s service. This is true regardless of whether you used the [activityViewController](activityviewcontroller.md) or [- performActivity](<perform().md>) method to initiate the service. When calling the method, use the Boolean value to indicate whether the service completed successfully.

This method must be called on the main thread.

## See Also

### Performing the activity

- [- canPerformWithActivityItems:](<canperform(withactivityitems_).md>) — Queries whether the service can act on the specified data items.
- [- prepareWithActivityItems:](<prepare(withactivityitems_).md>) — Prepares your service to act on the specified data.
- [activityViewController](activityviewcontroller.md) — The view controller to present to the user.
- [- performActivity](<perform().md>) — Performs the service when no custom view controller is provided.
