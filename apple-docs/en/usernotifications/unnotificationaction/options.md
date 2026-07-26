---
title: options
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationaction/options
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationaction/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationaction/options.json'
content_hash: 'sha256:fb63d86fe1ffb428'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationAction](../unnotificationaction.md)

# options

<sub>Instance Property</sub>

The behaviors associated with the action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var options: UNNotificationActionOptions { get }
```

## Discussion

You app should define options for an action when your app requires the corresponding behavior.

## See Also

### Getting Options

- [UNNotificationActionOptions](../unnotificationactionoptions.md) — The behaviors you can apply to an action.
