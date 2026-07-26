---
title: notificationResponse
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/connectionoptions/notificationresponse
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/connectionoptions/notificationresponse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/connectionoptions/notificationresponse.json'
content_hash: 'sha256:71ef019905618199'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIScene](../../uiscene.md) · [ConnectionOptions](../connectionoptions.md)

# notificationResponse

<sub>Instance Property</sub>

A person’s response to one of your app’s notifications.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var notificationResponse: UNNotificationResponse? { get }
```

## Discussion

When UIKit connects a scene in order to process a notification, it puts the response object in this property. Use the information in this object to configure your scene. If a person selected one of the notification’s actions, perform that action.
