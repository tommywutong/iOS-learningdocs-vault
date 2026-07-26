---
title: userDidTakeScreenshotNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/userdidtakescreenshotnotification
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/userdidtakescreenshotnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/userdidtakescreenshotnotification.json'
content_hash: 'sha256:89634c63e3062486'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# userDidTakeScreenshotNotification

<sub>Type Property</sub>

A notification that posts when a person takes a screenshot on the device.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let userDidTakeScreenshotNotification: NSNotification.Name
```

## Discussion

This notification doesn’t contain a `userInfo` dictionary. This notification posts after the screenshot is taken.
