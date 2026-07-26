---
title: perform()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivity/perform()
source_url: 'https://developer.apple.com/documentation/uikit/uiactivity/perform()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivity/perform%28%29.json'
content_hash: 'sha256:ab9fc2cde26a4664'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivity](../uiactivity.md)

# perform()

<sub>Instance Method</sub>

Performs the service when no custom view controller is provided.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func perform()
```

## Discussion

The default implementation of this method does nothing. If your service doesn’t provide any custom UI using the [activityViewController](activityviewcontroller.md) method, override this method and use it to perform the activity. Your activity must operate on the data items received in the [- prepareWithActivityItems:](<prepare(withactivityitems_).md>) method.

This method is called on your app’s main thread. If your app can complete the activity quickly on the main thread, do so and call the [- activityDidFinish:](<activitydidfinish(__).md>) method when it’s done. If performing the activity might take some time, use this method to start the work in the background and then exit without calling [- activityDidFinish:](<activitydidfinish(__).md>) from this method. When your background work has completed, call [- activityDidFinish:](<activitydidfinish(__).md>). You must call [- activityDidFinish:](<activitydidfinish(__).md>) on the main thread.

## See Also

### Performing the activity

- [- canPerformWithActivityItems:](<canperform(withactivityitems_).md>) — Queries whether the service can act on the specified data items.
- [- prepareWithActivityItems:](<prepare(withactivityitems_).md>) — Prepares your service to act on the specified data.
- [activityViewController](activityviewcontroller.md) — The view controller to present to the user.
- [- activityDidFinish:](<activitydidfinish(__).md>) — Notifies the system that your activity object has completed its work.
