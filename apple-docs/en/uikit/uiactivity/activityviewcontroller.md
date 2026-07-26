---
title: activityViewController
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivity/activityviewcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uiactivity/activityviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivity/activityviewcontroller.json'
content_hash: 'sha256:1163da3312eaf0f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivity](../uiactivity.md)

# activityViewController

<sub>Instance Property</sub>

The view controller to present to the user.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var activityViewController: UIViewController? { get }
```

## Discussion

Subclasses that provide additional UI using a view controller can override this method to return that view controller. If this method returns a valid object, the system presents the returned view controller modally instead of calling the [- performActivity](<perform().md>) method.

Your custom view controller should provide a view with your custom UI and should handle any user interactions inside those views. Upon completing the activity, don’t dismiss the view controller yourself. Instead, call the [- activityDidFinish:](<activitydidfinish(__).md>) method and let the system dismiss it for you.

## See Also

### Performing the activity

- [- canPerformWithActivityItems:](<canperform(withactivityitems_).md>) — Queries whether the service can act on the specified data items.
- [- prepareWithActivityItems:](<prepare(withactivityitems_).md>) — Prepares your service to act on the specified data.
- [- performActivity](<perform().md>) — Performs the service when no custom view controller is provided.
- [- activityDidFinish:](<activitydidfinish(__).md>) — Notifies the system that your activity object has completed its work.
